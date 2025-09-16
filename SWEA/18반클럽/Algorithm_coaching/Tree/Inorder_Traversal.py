class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
def inoder_ans(root):
    global ans
    if root:
        inoder_ans(root.left)
        ans += tree[root.value]
        inoder_ans(root.right)
T = 10

for t in range(1, T+1):
    n = int(input())
    tree = [[] for _ in range(n+1)]
    child = [[] for _ in range(n+1)]
    for i in range(n):
        box = list(map(str, input().split()))
        idx = int(box[0])
        val = box[1]

        tree[idx] = val

        for j in range(2, len(box)):
            child[idx].append(int(box[j]))
    #---------------------------------------- 부모 자식 위치, 값 받음

    words = [None] + [TreeNode(i) for i in range(1, n+1)]

    # ---------------------------------------- 부모 자식 자리 세팅

    for i in range(1, n+1):
        kids = child[i]
        if len(kids) >= 1:
            words[i].left = words[kids[0]]
        if len(kids) == 2:
            words[i].right = words[kids[1]]
    # ----------------------------------------- 부모 자식 세팅

    root_idx = 1
    ans = ''
    inoder_ans(words[root_idx])

    print(f"#{t} {ans}")