#!/usr/bin/env python3
# ECB oracle: encrypt(pt) = AES-ECB_K(pt || FLAG) 를 무제한 호출 가능.
# ECB 는 동일 블록이 동일 ct 로 나오는 성질을 이용해 플래그를 한 바이트씩 뽑아낸다.
#
# 공격 아이디어 (byte-at-a-time):
#   i 번째 플래그 바이트를 알아낼 때:
#     - 패딩 "A"*(15-(i%16)) 를 입력하면 오라클이 encrypt 하는 문자열은
#         "A"*(15-r) || FLAG[0..i-1] || FLAG[i] || ...
#       이 때 q = i//16 번째 블록은 정확히 "?? || FLAG[i]" 가 들어감.
#     - 다음으로 pad || known || b 를 넣으면 같은 블록 위치가
#         "?? || b"
#       가 되어 b == FLAG[i] 일 때만 ct 일치.
#
# 블록 하나당 최대 256번 질의.

import time

import requests

URL = "https://aes.cryptohack.org/ecb_oracle/encrypt/"
BLOCK = 16
session = requests.Session()


# 서버가 가끔 JSON 대신 에러 페이지를 뱉어서 retry 몇번 붙임
def encrypt(data: bytes) -> bytes:
    for _ in range(5):
        try:
            r = session.get(URL + data.hex() + "/", timeout=10)
            return bytes.fromhex(r.json()["ciphertext"])
        except Exception:
            time.sleep(1)
    raise RuntimeError("oracle failed")


known = b""
while True:
    i = len(known)
    r = i % BLOCK
    p = BLOCK - 1 - r
    if p == 0:
        # pad 가 빈 문자열이 되면 URL 이 깨져서 서버가 에러. 한 블록 더 붙여서 피함
        p = BLOCK
    pad = b"A" * p
    q = (p + i) // BLOCK
    sl = slice(q * BLOCK, (q + 1) * BLOCK)

    # 정답 블록: pad 만 보내서 q 번째 블록을 따둠
    target = encrypt(pad)[sl]

    # 후보 바이트 하나씩 넣어 맞춰봄
    for b in range(256):
        guess = pad + known + bytes([b])
        if encrypt(guess)[sl] == target:
            known += bytes([b])
            print(f"[{len(known):3d}] {known}")
            break
    else:
        # 매칭 실패 -> 끝까지 옴 (PKCS7 패딩 영역 진입)
        break

    if known.endswith(b"}"):
        break

print("\nflag:", known.decode())
