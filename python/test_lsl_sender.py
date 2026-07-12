from __future__ import annotations

import math
import random
import time

from pylsl import StreamInfo, StreamOutlet, local_clock


def main() -> None:
    info = StreamInfo(
        name="EEG_RV_TestStream",
        type="EEG",
        channel_count=4,
        nominal_srate=100,
        channel_format="float32",
        source_id="eeg-rv-python-test",
    )

    outlet = StreamOutlet(info)
    print("Enviando stream LSL 'EEG_RV_TestStream' a 100 Hz. Pressione Ctrl+C para parar.")

    start_time = time.time()
    sample_interval = 0.01

    try:
        while True:
            t = time.time() - start_time
            sample = [
                math.sin(2 * math.pi * 10 * t),
                math.sin(2 * math.pi * 12 * t),
                math.sin(2 * math.pi * 8 * t),
                random.uniform(-0.1, 0.1),
            ]
            outlet.push_sample(sample, local_clock())
            time.sleep(sample_interval)
    except KeyboardInterrupt:
        print("\nStream encerrado.")


if __name__ == "__main__":
    main()
