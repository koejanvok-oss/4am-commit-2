#!/usr/bin/env python3
"""Write the 4AM commit message to /output/entry.txt."""

import os

ENTRY = "4am: I wrote the bug, I found the bug, I fixed the bug — I am the bug"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
