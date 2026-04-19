#!/usr/bin/env python3

import sys
from Crypto.Util.number import *

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")


ct = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for k in range(256):
    pt = bytes(b ^ k for b in ct)
    if pt.startswith(b"crypto{"):
        print("Here is your flag:")
        print(pt.decode())
        print(f"(key byte: {k:#x})")
        break
