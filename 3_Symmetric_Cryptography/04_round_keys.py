#!/usr/bin/env python3
# AddRoundKey: state 와 round_key 를 원소별로 XOR 하는 것
# 결과 matrix 를 다시 bytes 로 바꾸면 플래그.

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    return [[a ^ b for a, b in zip(sr, kr)] for sr, kr in zip(s, k)]


def matrix2bytes(m):
    return bytes(b for row in m for b in row)


out = add_round_key(state, round_key)
print(matrix2bytes(out).decode())
