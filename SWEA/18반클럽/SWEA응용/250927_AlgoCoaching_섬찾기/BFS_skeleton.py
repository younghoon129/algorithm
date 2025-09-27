import sys
sys.stdin = open('island_input.txt')


def find_island(island, x, y):
    pass

n, m = map(int, input().split())  # 섬의 크기 입력
arr = [list(map(int, input())) for _ in range(n)]  # 섬의 상태 입력 받기
island_cnt = 0  # 섬의 개수

print(island_cnt)  # 섬의 개수 출력
