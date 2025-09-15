# # for t in range(1, 11):

# num = int(input())
# tree = []
# def get_node(self, index):
#     if index < len(self.tree):
#         return self.tree[index]
#     return None
# for n in range(num):
#     box = list(map(str, input().split()))
#     while len(tree) <= num:
#         tree.append(None)
#     tree[int(box[0])] = box[1]
# tree.pop(0)

# class TreeNode:
#     def __init__(self, key):
#         self.left = None  # 왼쪽 자식 노드
#         self.right = None  # 오른쪽 자식 노드
#         self.val = key  # 노드의 값

# def inorder_traversal(root):
#     if root:
#         inorder_traversal(root.left)  # 왼쪽 서브트리 방문
#         print(root.val)  # 현재 노드 방문
#         inorder_traversal(root.right)  # 오른쪽 서브트리 방문

# # 트리 생성
# tree = TreeNode(1)
# tree.left = TreeNode(2)
# tree.right = TreeNode(3)
# tree.left.left = TreeNode(4)
# tree.left.right = TreeNode(5)
# tree.right.left = TreeNode(6)
# tree.right.right = TreeNode(7)
# # tree.left.left.left = TreeNode(8)

# inorder_traversal(tree)


# 8
# 1 W 2 3
# 2 F 4 5
# 3 R 6 7
# 4 O 8
# 5 T
# 6 A
# 7 E
# 8 S
def inord(n):
    if n <= N:
        inord(n * 2)
        ans.append(lst[n])
        inord(n * 2 + 1)
 
T = 10
for test_case in range(1,T+1):
    N = int(input())
    lst = [0] * (N+1)
    for i in range(1,N+1):
        tlist = input().split()
        lst[i] = tlist[1]
    ans = []
    inord(1)
    print(f'#{test_case} {"".join(ans)}')