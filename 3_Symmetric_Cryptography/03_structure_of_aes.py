#!/usr/bin/env python3
# matrix2bytes 만 채우면 됨. 4x4 state matrix -> 16바이트
# 그냥 행 순서대로 flatten 하고 bytes() 에 넣으면 끝


def bytes2matrix(text):
    return [list(text[i : i + 4]) for i in range(0, len(text), 4)]


def matrix2bytes(matrix):
    return bytes(b for row in matrix for b in row)


matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix).decode())
