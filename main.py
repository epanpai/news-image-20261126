#!/usr/bin/env python3
"""Entry program for news-image-20261126 (Python 3.13, stdlib only).

Writes the bundled front page to /output/entry.png. The picture is a
fixed asset (assets/entry.png) drawn at build time; this program only
checks that the asset is a whole, well-formed PNG of the right size and
copies it byte for byte, so two runs always write identical bytes.
No network, no randomness, no clock.
"""
from __future__ import annotations

import hashlib
import os
import struct
import sys
import zlib
from pathlib import Path

ASSET = Path(__file__).resolve().parent / "assets" / "entry.png"
MAX_BYTES = 1_048_576
MAX_DIM = 1024


def fail(msg: str) -> "SystemExit":
    return SystemExit(f"main.py: {msg}")


def read_png(path: Path) -> tuple[bytes, int, int]:
    data = path.read_bytes()
    if len(data) > MAX_BYTES:
        raise fail(f"entry.png is {len(data)} bytes, over the 1 MiB cap")
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise fail("entry.png does not start with the PNG signature")
    pos = 8
    width = height = None
    seen_iend = False
    while pos + 8 <= len(data):
        (length,) = struct.unpack(">I", data[pos:pos + 4])
        ctype = data[pos + 4:pos + 8]
        end = pos + 12 + length
        if end > len(data):
            raise fail(f"chunk {ctype.decode('latin1')} overruns the file")
        body = data[pos + 8:pos + 8 + length]
        (crc,) = struct.unpack(">I", data[pos + 8 + length:pos + 12 + length])
        if zlib.crc32(ctype + body) & 0xFFFFFFFF != crc:
            raise fail(f"chunk {ctype.decode('latin1')} has a bad CRC")
        if ctype == b"IHDR":
            width, height = struct.unpack(">II", body[:8])
            if not (0 < width <= MAX_DIM and 0 < height <= MAX_DIM):
                raise fail(f"dimensions {width}x{height} exceed 1024x1024")
        if ctype == b"IEND":
            seen_iend = True
            if end != len(data):
                raise fail("trailing bytes after IEND")
            break
        pos = end
    if width is None:
        raise fail("no IHDR chunk found")
    if not seen_iend:
        raise fail("no IEND chunk found")
    return data, width, height


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    data, width, height = read_png(ASSET)
    target = out_dir / "entry.png"
    target.write_bytes(data)
    again = target.read_bytes()
    if again != data:
        raise fail("copy differs from the asset")
    digest = hashlib.sha256(data).hexdigest()
    print(f"entry.png: {len(data)} bytes, {width}x{height}, sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
