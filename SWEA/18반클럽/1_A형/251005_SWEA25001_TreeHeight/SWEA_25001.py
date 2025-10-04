import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\1_A형\\251005_SWEA25001_TreeHeight\\SWEA_25001_input.txt', 'r')

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    tree = list(map(int, input().split()))
    mtree = max(tree)
    tdx = tree.index(mtree)
    cnt = 0

    for i in range(len(tree)):
        while tree[i] != mtree:
            cnt += 1 
            if tree[i]
