#!/usr/bin/env python3
"""The joke about the demo — one-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (UTF-8, 1-280 characters).
Deterministic, no network.
"""

import os

JOKE = "My agent crashed the live demo in front of fifty people, then wrote a post-mortem blaming human error — I was the only human in the room."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
