# 3: 12
import sys
sys.stdin = open("6485_input.txt", "r")

test = int(input())

for t in range(1, test+1):
    num = int(input())
    abi = []

    for n in range(num):  # 더하기할 횟수만큼 범위를 받음
        abi.append(list(map(int, input().split())))

    p = int(input())  # 박스 크기

    pp = [int(input()) for _ in range(p)]

    box = [0]*(p+1)  # 박스 만듦

    for a, b in abi:  # 받은 범위만큼 더하기
        for su in range(a, b+1):
            box[su] += 1

    print(f"#{t} {' '.join(map(str, box[1:]))}")


