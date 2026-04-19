#!/usr/bin/env python3
# OFB 는 키스트림을 iv 와 key 만으로 만든다 (플레인텍스트와 무관):
#   k_1 = ENC_K(iv), k_2 = ENC_K(k_1), ...
#   c_i = p_i XOR k_i
# 그래서 암호화 = 복호화. XOR 로 두 번 씌우면 원상복귀.
#
# 공격:
#   1. encrypt_flag 로 iv || ct 를 받는다 -> ct = flag XOR keystream
#   2. 같은 iv 로 encrypt(ct) 를 호출하면 서버는 ct 를 평문 취급해서 ct XOR keystream 을 반환
#      = flag XOR keystream XOR keystream = flag
#
# 서버가 encrypt 엔드포인트에서 키를 그대로 재사용하는 게 허점.

import requests

URL = "https://aes.cryptohack.org/symmetry"
BLOCK = 16

# Step 1. flag 암호문 얻기 (iv || ct)
r = requests.get(f"{URL}/encrypt_flag/").json()
blob = bytes.fromhex(r["ciphertext"])
iv, ct = blob[:BLOCK], blob[BLOCK:]

# Step 2. ct 를 평문처럼 다시 encrypt -> flag 나옴
r2 = requests.get(f"{URL}/encrypt/{ct.hex()}/{iv.hex()}/").json()
flag = bytes.fromhex(r2["ciphertext"])

print(flag.decode())
