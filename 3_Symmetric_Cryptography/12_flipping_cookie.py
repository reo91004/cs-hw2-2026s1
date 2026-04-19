#!/usr/bin/env python3
# CBC bit-flipping.
# CBC 복호화: p_1 = DEC_K(c_1) XOR IV
# 그래서 IV 의 i 번째 바이트를 뒤집으면 p_1 의 i 번째 바이트가 같은 XOR 만큼 뒤집힌다.
# 다른 블록들은 영향 없음 (CBC 의 오류 전파 특성상 c_1 을 건드렸으면 그 다음 블록까지 망가졌을 텐데,
# IV 는 c_0 역할이라 block 1 만 영향).
#
# cookie 원본: "admin=False;expiry=..."
#   블록 1 (16B): "admin=False;expi"
#
# 목표: split(b";") 결과에 b"admin=True" 가 들어가야 함.
#   블록 1 을 "admin=True;;expi" 로 만들면 split -> ["admin=True", "", "expi..."] 에 원하는 값 포함.
#   (True 는 4글자, False 는 5글자라 한 글자가 남음 -> e 위치를 ; 로 바꿔서 빈 필드 생성)
#
# 전략: flip_mask = 원본 블록1 XOR 목표 블록1, new_iv = iv XOR flip_mask.

import requests

URL = "https://aes.cryptohack.org/flipping_cookie"
BLOCK = 16

# Step 1. get_cookie: iv || ct 로 반환 (둘 다 hex)
r = requests.get(f"{URL}/get_cookie/").json()
cookie = bytes.fromhex(r["cookie"])
iv, ct = cookie[:BLOCK], cookie[BLOCK:]

# Step 2. 블록 1 의 원본과 목표 bytes 정하기
orig = b"admin=False;expi"
target = b"admin=True;;expi"

# Step 3. 각 바이트 XOR 차이 계산 -> IV 에 적용
flip = bytes(a ^ b for a, b in zip(orig, target))
new_iv = bytes(a ^ b for a, b in zip(iv, flip))

# Step 4. 위조된 cookie 로 check_admin 호출
r2 = requests.get(f"{URL}/check_admin/{ct.hex()}/{new_iv.hex()}/").json()
print(r2)
