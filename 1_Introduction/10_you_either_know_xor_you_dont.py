#!/usr/bin/env python3

import sys
from Crypto.Util.number import *

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")


ct = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

# Step 1: 평문은 "crypto{"로 시작한다는 힌트 → 암호문 앞 7바이트와 XOR하면 키의 앞 7바이트가 나온다.
known = b"crypto{"
key_prefix = bytes(c ^ p for c, p in zip(ct, known))
print(f"[step1] recovered key prefix: {key_prefix}")  # -> b'myXORke'

# Step 2: prefix가 "myXORke" → 자연스럽게 "myXORkey"로 추정하고 반복키 XOR로 전체 복호화.
key = b"myXORkey"
pt = bytes(c ^ key[i % len(key)] for i, c in enumerate(ct))

print("Here is your flag:")
print(pt.decode())
