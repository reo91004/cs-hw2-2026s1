#!/usr/bin/env python3

import math


# Step 1. 유클리드 호제법 구현.
# gcd(a, b) = gcd(b, a % b), 나머지가 0되는 순간의 a가 답.
# a = q*b + r 이면 (a,b)의 공약수랑 (b,r)의 공약수가 같아서 성립.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Step 2. 교재 예제로 구현 맞는지 체크. 12, 8 넣으면 4 나와야 함.
assert gcd(12, 8) == 4

# Step 3. 본 문제.
a, b = 66528, 52920
ans = gcd(a, b)
print(f"gcd({a}, {b}) = {ans}")

# math.gcd 로 교차검증
assert ans == math.gcd(a, b)
