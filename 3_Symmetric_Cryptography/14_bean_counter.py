#!/usr/bin/env python3
# StepUpCounter 버그: step_up=False 기본값으로 생성되면 increment 에서
#   newIV = hex(int(self.value, 16) - self.stup)  # stup=False 라 0 빼기
# 결국 counter 가 전혀 안 바뀜. 즉 모든 블록이 같은 keystream K 로 XOR 되는 1-time pad.
#
# 한 바이트라도 평문을 알면 K 를 복원할 수 있음.
# 다행히 원본이 PNG 파일 -> 첫 16바이트 헤더는 고정:
#   89 50 4E 47 0D 0A 1A 0A  (PNG signature, 8B)
#   00 00 00 0D 49 48 44 52  (IHDR 청크 길이 + 타입, 8B)
#
# K = ct[0:16] XOR png_header 로 복원 후 모든 블록에 XOR -> 원본 PNG 복원.
# flag 는 PNG 안에 이미지로 박혀 있음.

import requests

URL = "https://aes.cryptohack.org/bean_counter/encrypt/"
BLOCK = 16
OUT = "/Users/reo/Documents/Repository/cryptohack/3_Symmetric_Cryptography/bean_flag.png"

# Step 1. ct 받기
r = requests.get(URL).json()
ct = bytes.fromhex(r["encrypted"])

# Step 2. PNG 표준 헤더 16바이트로 keystream 복원
png_header = bytes.fromhex("89504E470D0A1A0A0000000D49484452")
K = bytes(a ^ b for a, b in zip(ct[:BLOCK], png_header))

# Step 3. 전체 ct 를 K 로 XOR (블록별로 동일 K 재사용)
pt = bytearray()
for i in range(0, len(ct), BLOCK):
    block = ct[i : i + BLOCK]
    pt += bytes(a ^ b for a, b in zip(block, K))

# Step 4. PNG 로 저장 -> 이미지 열어보면 flag
with open(OUT, "wb") as f:
    f.write(pt)

print(f"saved {len(pt)} bytes -> {OUT}")
print("open the png to read the flag")
