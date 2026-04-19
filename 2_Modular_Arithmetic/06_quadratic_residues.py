#!/usr/bin/env python3
# p=29, ints=[14, 6, 11] 중 quadratic residue 인 것 찾고 그 제곱근 두 개 중 작은 쪽 제출

p = 29
ints = [14, 6, 11]

# Step 1. 각 x 에 대해 a=1..p-1 돌려서 a^2 ≡ x mod p 되는 a 수집.
# residue 면 a, p-a 두 해 존재 (힌트: a^2 = (-a)^2).
for x in ints:
    roots = [a for a in range(1, p) if (a * a) % p == x]
    print(f"x = {x}: roots = {roots}")

# Step 2. residue 인 애의 작은 root 제출.
for x in ints:
    roots = [a for a in range(1, p) if (a * a) % p == x]
    if roots:
        print(f"answer: x={x}, smaller root = {min(roots)}")
