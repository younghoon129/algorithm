# 문제: 삼성 영어 학원 반 배정
# 영어 학원에서 학생들을 개인별 능력치에 따라 A, B, C 세 반으로 배정하려고 한다.
# 두 개의 기준값 K1, K2를 정해 다음 규칙으로 배정한다.
#
# A반: 능력치가 K2 이상인 학생들
# B반: 능력치가 K1 이상이고 K2 미만인 학생들
# C반: 능력치가 K1 미만인 학생들
# 각 반의 인원은 최소 인원 L명 이상, 최대 인원 U명 이하여야 한다.
#
# 가능한 모든 K1, K2 배정 방법 중에서,
# 세 반 중에서 가장 많은 인원과 가장 적은 인원의 차이가 가장 작아지는 경우의 차이를 구하라.
# 만약 어떤 K1, K2로도 조건을 만족하는 배정이 불가능하다면 -1을 출력한다.
#
# 입력
# 첫 줄에 테스트 케이스 수 T가 주어진다.
# 이후 각 테스트 케이스마다 다음이 주어진다.
# 한 줄에 세 정수 N, L, U (학생 수, 한 반의 최소 인원, 한 반의 최대 인원)
# 다음 줄에 N개의 정수 (각 학생의 능력치)
# 출력
# 각 테스트 케이스마다 한 줄에 # 테스트케이스번호 결과값 형식으로 출력한다.

import sys
sys.stdin = open('SWEA_input.txt', 'r')

tc = int(input())

for t in range(1, tc+1):
    n, l, u = map(int, input().split())  # n = 학생 수, l = 최소, u = 최대
    box = list(map(int, input().split()))
    min_cnt = float('inf')
    cnt = -1
    max_num = 0
    min_num = float('inf')
    a = 0
    b = 0
    c = 0
    pl = set(box)
    result = []
    for o in pl:
        result.append(box.count(o))
    # print(result)
    for i in range(len(result)):
        a += result[i]
        if a < l: continue
        if a > u: break
        b = 0
        for j in range(i+1, len(result)):
            b += result[j]
            if b < l: continue
            if b > u: break
            c = 0
            for k in range(j+1, len(result)):
                c += result[k]
                if c < l: continue
                if c > u: break
            if l <= a <= u and l <= b <= u and l <= c <= u:
                max_num = max(a, b, c)
                min_num = min(a, b, c)
                cnt = max_num - min_num
                min_cnt = min(min_cnt, cnt)
    if min_cnt == float('inf'):
        print(-1)
    else:
        print(min_cnt)