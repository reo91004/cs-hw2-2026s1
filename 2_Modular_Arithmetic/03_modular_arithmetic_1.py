#!/usr/bin/env python3
# 11 ≡ x mod 6
# 8146798528947 ≡ y mod 17
# 둘 중 작은 쪽 제출

# 그냥 % 연산자 돌리면 끝 (파이썬 %는 항상 0 이상 나머지라서 그대로 써도 됨)
x = 11 % 6
y = 8146798528947 % 17
print(f"x = {x}, y = {y}")

ans = min(x, y)
print(f"answer: {ans}")
