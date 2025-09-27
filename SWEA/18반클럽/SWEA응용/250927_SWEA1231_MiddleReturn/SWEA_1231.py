import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\SWEA응용\\250927_SWEA1231_MiddleReturn\\MiddleReturn_input.txt', 'r')

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.value = key
        self.right = None

def mid(root):
    global result
    if root:
        mid(root.left)
        result += pl[root.value]
        mid(root.right)


tc = 1  # @@@@@@@@@@@@@@@바꾸기바꾸기@@@@@@@@@@@@@@@@@
for t in range(1, tc+1):
    n = int(input())
    pl = [[] for _ in range(n+1)]  # 단어들
    cl = [[] for _ in range(n+1)]  # 부모인덱스에 자식번호
    for i in range(n):
        box = list(map(str, input().split()))
        pl[int(box[0])]=box[1]
        for j in range(2, len(box)):
            cl[int(box[0])].append(int(box[j]))
    
    words = [None] + [TreeNode(i) for i in range(1, n+1)]
    
    for j in range(1, len(cl)):
        if len(cl[j]) >= 1:
            words[j].left = words[cl[j][0]]
        if len(cl[j]) == 2:
            words[j].right = words[cl[j][1]]
    
    st = 1
    result = ''
    mid(words[st])

    print(result)