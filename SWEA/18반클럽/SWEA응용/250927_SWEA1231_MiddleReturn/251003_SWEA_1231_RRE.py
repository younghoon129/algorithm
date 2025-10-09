import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\SWEA응용\\250927_SWEA1231_MiddleReturn\\MiddleReturn_input.txt', 'r')

class TreeNodes:
    def __init__(self, key):
        self.left = None
        self.value = key
        self.right = None

def re(root):
    global result
    if root:
        re(root.left)
        result += word[root.value]
        re(root.right)

tc = 1
for t in range(1, tc+1):

    n = int(input())
    word = ['' for _ in range(n+1)]
    nl = [[] for _ in range(n+1)]
    for i in range(n):
        
        box = list(map(str, input().split()))
        word[int(box[0])] = box[1]
        for j in range(2, len(box)):
            nl[int(box[0])].append(int(box[j]))


    wl = [None] + [TreeNodes(i) for i in range(1, n+1)]

    for k in range(1, len(nl)):
        if len(nl[k]) >= 1:
            wl[k].left = wl[nl[k][0]]
        if len(nl[k]) == 2:
            wl[k].right = wl[nl[k][1]]
    
    st = 1
    result = ''
    re(wl[st])

    print(result)