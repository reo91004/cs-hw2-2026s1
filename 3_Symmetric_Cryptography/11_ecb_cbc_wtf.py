#!/usr/bin/env python3
# encrypt_flag: CBC 모드로 flag 암호화 -> ct = iv || c1 || c2 || ...
# decrypt:      ECB 모드로 임의 ct 복호화 (같은 키).
# 키는 모르지만 두 모드가 같은 키를 공유하는 게 결정적 허점.
#
# CBC 복호화: p_i = DEC_K(c_i) XOR c_{i-1}    (c_0 = iv)
# ECB 복호화: p_i' = DEC_K(c_i)
# -> p_i = p_i' XOR c_{i-1}
#
# 따라서 c1..cn 을 ECB decrypt 로 받아온 뒤 각 블록을 이전 ct 블록과 XOR 하면 끝.

import requests

URL = "https://aes.cryptohack.org/ecbcbcwtf"
BLOCK = 16

# Step 1. CBC 로 암호화된 flag 받기
ct_hex = requests.get(f"{URL}/encrypt_flag/").json()["ciphertext"]
ct = bytes.fromhex(ct_hex)
iv, body = ct[:BLOCK], ct[BLOCK:]

# Step 2. body 를 ECB 로 decrypt (iv 는 빼고 보냄 - decrypt 는 key 만 씀)
ecb_hex = requests.get(f"{URL}/decrypt/{body.hex()}/").json()["plaintext"]
ecb_pt = bytes.fromhex(ecb_hex)

# Step 3. 각 블록을 이전 ct 블록 (첫 블록은 iv) 과 XOR
prev = iv
flag = b""
for i in range(0, len(ecb_pt), BLOCK):
    block = ecb_pt[i : i + BLOCK]
    flag += bytes(a ^ b for a, b in zip(block, prev))
    prev = body[i : i + BLOCK]

print(flag.decode(errors="replace"))
