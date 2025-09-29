import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\SWEA응용\\250927_SWEA1231_MiddleReturn\\MiddleReturn_input.txt', 'r')

class TreeNode:
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

    



tc = 1  #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
for t in range(1, tc+1):
    n = int(input())  # 단어 갯수
    num = [[] for _ in range(n+1)]
    word = ['' for _ in range(n+1)]
    
    for i in range(n):
        box = list(map(str, input().split()))
        # print(int(box[0]))
        # print(word)
        word[int(box[0])] = box[1]
        for j in range(2, len(box)):
            num[int(box[0])].append(int(box[j]))
        
    wl = [None] + [TreeNode(i) for i in range(1, n+1)]

    for k in range(1, len(num)):
        if len(num[k]) >= 1:
            wl[k].left = wl[num[k][0]]
        if len(num[k]) == 2:
            wl[k].right = wl[num[k][1]]

    st = 1
    result = ''
    re(wl[st])

    print(result)
