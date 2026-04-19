#!/usr/bin/env python3
# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17
# 위 세 합동 만족하는 x mod 935 구하기 (935 = 5*11*17)

from math import gcd

residues = [(2, 5), (3, 11), (5, 17)]


# CRT 일반 구현
# 합동식 둘씩 합치면서 진행:
#   x ≡ a1 mod n1, x ≡ a2 mod n2  ->  x ≡ ? mod (n1*n2)  (gcd(n1,n2)=1 가정)
# 공식: x = a1 + n1 * k, 여기서 k = (a2 - a1) * n1^-1 mod n2
def crt_pair(a1, n1, a2, n2):
    assert gcd(n1, n2) == 1
    # n1^-1 mod n2
    inv = pow(n1, -1, n2)
    k = ((a2 - a1) * inv) % n2
    return (a1 + n1 * k) % (n1 * n2), n1 * n2


a, n = residues[0]
for ai, ni in residues[1:]:
    a, n = crt_pair(a, n, ai, ni)

print(f"x ≡ {a} mod {n}")

# 검증
for ai, ni in residues:
    assert a % ni == ai
