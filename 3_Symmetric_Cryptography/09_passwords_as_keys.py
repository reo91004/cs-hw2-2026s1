#!/usr/bin/env python3
# 서버가 /usr/share/dict/words 에서 단어 하나 뽑아 md5 해시를 AES-128-ECB 키로 씀.
# 단어가 ~235k 개뿐이라 전부 brute force 가능.
#
# 전략:
# 1. /encrypt_flag/ 를 한번 호출해서 flag ciphertext 를 얻는다 (여기선 화면에 나온 값 그대로 사용).
# 2. /usr/share/dict/words 의 각 단어 w 에 대해 key = md5(w) 로 AES-ECB decrypt.
# 3. 결과가 "crypto{" 로 시작하면 그게 정답.
#
# /decrypt/ 엔드포인트는 안 건드려도 됨 - 어차피 키를 몰라서 그냥 decrypt 하게 해주는 거고,
# 우리는 키 후보를 전부 시도할 수 있으니 서버 왕복 없이 로컬에서 끝남.

import hashlib
from Crypto.Cipher import AES

# 화면에 나온 encrypt_flag 결과 - 서버 프로세스가 유지되는 동안은 고정값
ct = bytes.fromhex("c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66")

# 서버랑 똑같이 /usr/share/dict/words 사용
with open("/usr/share/dict/words") as f:
    words = [w.strip() for w in f]

for w in words:
    key = hashlib.md5(w.encode()).digest()
    pt = AES.new(key, AES.MODE_ECB).decrypt(ct)
    if pt.startswith(b"crypto{"):
        flag = pt.split(b"}")[0] + b"}"
        print(f"keyword: {w}")
        print(f"flag: {flag.decode()}")
        break
else:
    print("not found - ciphertext 가 재생성됐을 수 있음. encrypt_flag 다시 호출 필요")
