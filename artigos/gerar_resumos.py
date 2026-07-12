from __future__ import annotations

import argparse
import csv
import html
import re
from collections import Counter
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path


SUPPORTED_EXTENSIONS = {".txt", ".md", ".html", ".htm"}

STOPWORDS = {
    "a",
    "ao",
    "aos",
    "as",
    "com",
    "como",
    "da",
    "das",
    "de",
    "do",
    "dos",
    "e",
    "em",
    "entre",
    "for",
    "in",
    "into",
    "is",
    "na",
    "nas",
    "no",
    "nos",
    "o",
    "of",
    "os",
    "ou",
    "para",
    "por",
    "que",
    "se",
    "sem",
    "the",
    "to",
    "um",
    "uma",
    "umas",
    "uns",
}


class HTMLTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag in {"script", "style"}:
            self._skip_depth += 1
        if tag in {"p", "br", "li", "tr", "h1", "h2", "h3", "h4"}:
            self._parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self._skip_depth > 0:
            self._skip_depth -= 1
        if tag in {"p", "li", "tr"}:
            self._parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_depth == 0:
            self._parts.append(data)

    def text(self) -> str:
        return "".join(self._parts)


def parse_args() -> argparse.Namespace:
    base_dir = Path(__file__).resolve().parent
    return argparse.ArgumentParser(
        description="Gera resumos iniciais para arquivos de texto extraido."
    ).parse_args(namespace=argparse.Namespace(
        input_dir=base_dir / "01_extraidos",
        output_dir=base_dir / "02_resumos",
        index_file=base_dir / "03_planilhas" / "resumos_index.csv",
    ))


def strip_markdown(text: str) -> str:
    converted_lines: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped == "----":
            converted_lines.append("")
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if cells and all(set(cell) <= {":", "-"} for cell in cells):
                continue
            if len(cells) >= 2:
                converted_lines.append(f"{cells[0]}: {cells[1]}")
            else:
                converted_lines.append(" ".join(cells))
            continue
        converted_lines.append(line)

    text = "\n".join(converted_lines)
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text


def strip_html(text: str) -> str:
    parser = HTMLTextExtractor()
    parser.feed(text)
    return html.unescape(parser.text())


def normalize_whitespace(text: str) -> str:
    text = text.replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def remove_reference_section(text: str) -> str:
    markers = [
        r"^\s*##\s*bibliografia\s*$",
        r"^\s*##\s*refer[eê]ncias\s*$",
        r"^\s*bibliografia\s*$",
        r"^\s*refer[eê]ncias\s*$",
        r"^\s*references\s*$",
    ]
    for marker in markers:
        match = re.search(marker, text, flags=re.IGNORECASE | re.MULTILINE)
        if match:
            return text[:match.start()].strip()
    return text


def load_text(file_path: Path) -> str:
    raw = file_path.read_text(encoding="utf-8", errors="ignore")
    if file_path.suffix.lower() in {".html", ".htm"}:
        raw = strip_html(raw)
    else:
        raw = strip_markdown(raw)
    raw = remove_reference_section(raw)
    raw = re.sub(r"^\[\d+\]\s*$", "", raw, flags=re.MULTILINE)
    return normalize_whitespace(raw)


def extract_title(text: str, fallback: str) -> str:
    ignored_titles = {"tl;dr", "abstract", "resumo", "summary"}
    for line in text.splitlines():
        candidate = line.strip(" -\t")
        if len(candidate) >= 5 and candidate.lower() not in ignored_titles:
            return candidate
    return fallback


def split_sentences(text: str) -> list[str]:
    compact = re.sub(r"\s+", " ", text)
    pieces = re.split(r"(?<=[.!?])\s+", compact)
    return [p.strip() for p in pieces if len(p.strip()) > 30]


def tokenize(text: str) -> list[str]:
    words = re.findall(r"[A-Za-zÀ-ÿ0-9-]{3,}", text.lower())
    return [w for w in words if w not in STOPWORDS and not w.isdigit()]


def build_keywords(text: str, limit: int = 8) -> list[str]:
    counts = Counter(tokenize(text))
    return [word for word, _ in counts.most_common(limit)]


def score_sentences(sentences: list[str], counts: Counter) -> list[tuple[int, float]]:
    scored: list[tuple[int, float]] = []
    for index, sentence in enumerate(sentences):
        words = tokenize(sentence)
        if not words:
            continue
        score = sum(counts[word] for word in words) / max(len(words), 1)
        if 8 <= len(words) <= 40:
            score += 0.5
        scored.append((index, score))
    return scored


def summarize_text(text: str, max_sentences: int = 5) -> dict[str, object]:
    sentences = split_sentences(text)
    counts = Counter(tokenize(text))
    selected: list[str] = []

    if sentences:
        ranked = sorted(score_sentences(sentences, counts), key=lambda item: item[1], reverse=True)
        chosen_indexes = sorted(index for index, _ in ranked[:max_sentences])
        selected = [sentences[index] for index in chosen_indexes]

    if not selected and text:
        snippet = re.sub(r"\s+", " ", text)[:700].strip()
        if snippet:
            selected = [snippet]

    resumo_curto = " ".join(selected[:3]).strip()
    return {
        "resumo_curto": resumo_curto,
        "pontos_chave": selected,
        "palavras_chave": build_keywords(text),
    }


def write_summary(
    source_file: Path,
    output_dir: Path,
    summary_data: dict[str, object],
    title: str,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{source_file.stem}_resumo.md"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pontos = summary_data["pontos_chave"]
    palavras = summary_data["palavras_chave"]

    lines = [
        f"# Resumo de {source_file.stem}",
        "",
        f"- Arquivo origem: `{source_file.name}`",
        f"- Titulo identificado: {title}",
        f"- Gerado em: {timestamp}",
        "",
        "## Resumo breve",
        "",
        str(summary_data["resumo_curto"]) or "Resumo nao disponivel.",
        "",
        "## Pontos-chave",
        "",
    ]

    if pontos:
        for item in pontos:
            lines.append(f"- {item}")
    else:
        lines.append("- Nenhum ponto-chave identificado.")

    lines.extend([
        "",
        "## Palavras-chave",
        "",
        ", ".join(palavras) if palavras else "Sem palavras-chave identificadas.",
        "",
    ])

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def write_index(index_file: Path, rows: list[dict[str, str]]) -> None:
    index_file.parent.mkdir(parents=True, exist_ok=True)
    with index_file.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=[
                "arquivo_origem",
                "arquivo_resumo",
                "titulo_identificado",
                "palavras_chave",
                "resumo_breve",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    args = parse_args()
    input_dir: Path = args.input_dir
    output_dir: Path = args.output_dir
    index_file: Path = args.index_file

    files = sorted(
        path for path in input_dir.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    )

    rows: list[dict[str, str]] = []
    for file_path in files:
        text = load_text(file_path)
        title = extract_title(text, file_path.stem)
        summary_data = summarize_text(text)
        summary_path = write_summary(file_path, output_dir, summary_data, title)
        rows.append({
            "arquivo_origem": file_path.name,
            "arquivo_resumo": summary_path.name,
            "titulo_identificado": title,
            "palavras_chave": ", ".join(summary_data["palavras_chave"]),
            "resumo_breve": str(summary_data["resumo_curto"]),
        })

    write_index(index_file, rows)
    print(f"Arquivos processados: {len(rows)}")
    print(f"Resumos gravados em: {output_dir}")
    print(f"Indice CSV: {index_file}")


if __name__ == "__main__":
    main()
