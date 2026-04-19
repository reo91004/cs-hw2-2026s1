#!/usr/bin/env python3
# p*u + q*v = gcd(p, q) 만족하는 u, v 중 작은 쪽 제출
# p = 26513, q = 32321 (둘 다 소수 -> gcd = 1)


# Step 1. 확장 유클리드 호제법
# 일반 유클리드랑 비슷한데 (u, v)도 같이 끌고 감.
# 재귀 관점: gcd(a,b) = gcd(b, a%b) 이고
#   b*u' + (a%b)*v' = g  가 재귀로 풀리면
#   a%b = a - (a//b)*b 대입해서
#   a*v' + b*(u' - (a//b)*v') = g   -> 새 u = v', 새 v = u' - (a//b)*v'
def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0  # a*1 + 0*0 = a
    g, u1, v1 = ext_gcd(b, a % b)
    return g, v1, u1 - (a // b) * v1


# Step 2. 간단 검증, 3*u + 5*v = 1 나와야 함
g, u, v = ext_gcd(3, 5)
assert g == 1 and 3 * u + 5 * v == 1

p, q = 26513, 32321
g, u, v = ext_gcd(p, q)
print(f"gcd = {g}")
print(f"u = {u}, v = {v}")
print(f"검증: p*u + q*v = {p*u + q*v}")

# 둘 중 작은 쪽
ans = min(u, v)
print(f"answer: {ans}")
