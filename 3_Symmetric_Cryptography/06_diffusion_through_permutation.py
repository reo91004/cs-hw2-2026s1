#!/usr/bin/env python3
# ShiftRows / MixColumns 의 역연산으로 state 복구.
# 순서: inv_mix_columns -> inv_shift_rows -> bytes 변환.
#
# inv_shift_rows 는 shift_rows 의 반대로 돌리면 됨.
# shift_rows: row r 을 왼쪽으로 r 칸 (row-major 라 column 인덱스 기준) 이동.
# inv_shift_rows: 반대로 오른쪽으로 r 칸 이동.


def shift_rows(s):
    s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]


def inv_shift_rows(s):
    # col 1: 오른쪽 1칸 - shift_rows 의 역방향
    s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
    # col 2: 오른쪽 2칸 (= 왼쪽 2칸 과 동일)
    s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
    # col 3: 오른쪽 3칸 (= 왼쪽 1칸)
    s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]


# Rijndael GF 연산용 xtime
xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


def mix_single_column(a):
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)


def mix_columns(s):
    for i in range(4):
        mix_single_column(s[i])


def inv_mix_columns(s):
    for i in range(4):
        u = xtime(xtime(s[i][0] ^ s[i][2]))
        v = xtime(xtime(s[i][1] ^ s[i][3]))
        s[i][0] ^= u
        s[i][1] ^= v
        s[i][2] ^= u
        s[i][3] ^= v

    mix_columns(s)


def matrix2bytes(m):
    return bytes(b for row in m for b in row)


state = [
    [108, 106, 71, 86],
    [96, 62, 38, 72],
    [42, 184, 92, 209],
    [94, 79, 8, 54],
]

# 문제 지시대로: inv_mix_columns -> inv_shift_rows -> decode
inv_mix_columns(state)
inv_shift_rows(state)
print(matrix2bytes(state).decode())
