

# idx : 현재 선택중인 직원
# per : 여태 직원들의 성공 확률값의 합
def search(idx, per):
    global result
    if result >= per:
        return
    if idx == N:
        result = max(result, per)
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = True
        search(idx+1, per*arr[idx][i])
        visited[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] /= 100
    visited = [0] * N
    result = 0  # 나올 수 있는 최대 성공률
    search(0, 1)
    print(f"#{tc}")