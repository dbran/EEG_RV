from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_MD = ROOT / "documentos" / "introducao" / "AVE" / "ave_summary.md"
TOPICOS_JSON = ROOT / "documentos" / "modelos" / "topicos_exemplo.json"
OUTPUT_MD = ROOT / "documentos" / "gerados" / "ave_documento_exemplo.md"


def carregar_topicos(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def construir_documento(source_text: str, topicos_cfg: dict) -> str:
    titulo = topicos_cfg.get("titulo", "Documento")
    subtitulo = topicos_cfg.get("subtitulo", "")
    topicos = topicos_cfg.get("topicos", [])

    linhas = [f"# {titulo}", ""]
    if subtitulo:
        linhas.extend([subtitulo, ""])

    linhas.extend(
        [
            "## Estrutura prevista",
            "",
        ]
    )
    for item in topicos:
        linhas.append(f"- {item}")
    linhas.extend(
        [
            "",
            "## Conteudo-base",
            "",
            source_text.strip(),
            "",
            "## Observacoes de geracao",
            "",
            "- Este arquivo foi montado automaticamente a partir de um texto em Markdown.",
            "- Se um template `.docx` for adicionado em `documentos/modelos/template_artigo.docx`, ele pode ser usado em uma etapa futura de exportacao.",
            "- Como `pandoc` nao esta instalado neste ambiente, esta etapa gera apenas a versao `.md` estruturada.",
            "",
        ]
    )
    return "\n".join(linhas)


def main() -> None:
    if not SOURCE_MD.exists():
        raise FileNotFoundError(f"Arquivo fonte nao encontrado: {SOURCE_MD}")
    if not TOPICOS_JSON.exists():
        raise FileNotFoundError(f"Arquivo de topicos nao encontrado: {TOPICOS_JSON}")

    source_text = SOURCE_MD.read_text(encoding="utf-8")
    topicos_cfg = carregar_topicos(TOPICOS_JSON)
    documento = construir_documento(source_text, topicos_cfg)

    OUTPUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_MD.write_text(documento, encoding="utf-8")
    print(f"Documento gerado em: {OUTPUT_MD}")


if __name__ == "__main__":
    main()
