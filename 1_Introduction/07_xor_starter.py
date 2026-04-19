#!/usr/bin/env python3

import sys
from Crypto.Util.number import *

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

s = "label"
xored = "".join(chr(ord(c) ^ 13) for c in s)

print("Here is your flag:")
print(f"crypto{{{xored}}}")
