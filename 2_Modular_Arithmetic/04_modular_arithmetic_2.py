#!/usr/bin/env python3
# 273246787654^65536 mod 65537
# 65537은 소수, 지수 65536 = 65537 - 1 -> 페르마의 소정리
# Fermat's little: p 소수, gcd(a,p)=1 이면 a^(p-1) ≡ 1 mod p.
# 그래서 그냥 1 나올 것. 계산기도 필요없다고 문제에서 말함

a = 273246787654
p = 65537

# 먼저 gcd 확인해서 a 가 p 의 배수가 아닌지 체크 (배수면 0 나옴)
assert a % p != 0

ans = pow(a, p - 1, p)
print(f"{a}^{p-1} mod {p} = {ans}")
