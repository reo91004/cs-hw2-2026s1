#!/usr/bin/env python3
# 3 * d ≡ 1 mod 13 인 d (= 3^-1 mod 13) 구하기.
# 힌트가 "little theorem" -> 페르마의 소정리 쓰라는 얘기
# p 소수면 a^(p-1) ≡ 1 mod p 이므로 a * a^(p-2) ≡ 1.
# 즉 a^-1 = a^(p-2) mod p

a, p = 3, 13
d = pow(a, p - 2, p)
print(f"d = {d}")

# 검증
assert (a * d) % p == 1
