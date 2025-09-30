import sys
sys.stdin = open("C:\\Users\\user\\Desktop\\git\\algorism\\SWEA\\18반클럽\\IM_last\\250930_SWEA_test1\\test_input.txt", "r")

T = int(input())

# 한 반의 최소 인원, 최대 인원, 지금 현재 인원을 받아서 조건에 충족하는지 확인하는 함수
def OK(min, max, length):
    if min <= length <= max:
        return True

for tc in range(1, T + 1):
    N, L, U = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = float('inf')
    # 나오는 사람의 능력치를 중복되지 않게 담은 배열
    num_list = []
    for n in arr:
        if n not in num_list:
            num_list.append(n)
    print(f"num_list : {num_list}")
    # 위에서 만든 num_list로 가능한 모든 K1, K2 기준을 만들어보기
    for i in range(len(num_list)):
        for j in range(i, len(num_list)):
            K1, K2 = num_list[i], num_list[j]
            print(f"K1: {K1} K2: {K2}")
            # 반을 초기화하고 위에서 정해진 K1, K2 기준으로 한 명씩 배정해보기
            A = []
            B = []
            C = []
            for p in range(N):
                if arr[p] >= K2:
                    A.append(arr[p])
                elif K1 <= arr[p] < K2:
                    B.append(arr[p])
                elif arr[p] < K1:
                    C.append(arr[p])
            # 각 반의 학생수
            len_A = len(A)
            len_B = len(B)
            len_C = len(C)
            print(len_A, len_B, len_C)
            # 한 반의 최소, 최대 인원 조건이 맞게 잘 배정된 경우
            if OK(L, U, len_A) and OK(L, U, len_B) and OK(L, U, len_C):
                print(f"조건에 맞게 배정된 반:{A, B, C}")
                # 가장 많은 반의 인원 - 가장 적은 반의 인원
                diff = max(len_A, len_B, len_C) - min(len_A, len_B, len_C)
                # 최솟값 정답에 넣어놓기
                answer = min(answer, diff)
    # answer가 초기값 그대로면 가능한 반배정이 없으니까 -1
    if answer == float('inf'):
        answer = -1        
    print(f"#{tc} {answer}")