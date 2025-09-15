# for t in range(1, 11):

num = int(input())
tree = []
def get_node(self, index):
    if index < len(self.tree):
        return self.tree[index]
    return None
for n in range(num):
    box = list(map(str, input().split()))
    while len(tree) <= num:
        tree.append(None)
    tree[int(box[0])] = box[1]
tree.pop(0)

class TreeNode:
    def __init__(self, key):
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드
        self.val = key  # 노드의 값

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)  # 왼쪽 서브트리 방문
        print(root.val)  # 현재 노드 방문
        inorder_traversal(root.right)  # 오른쪽 서브트리 방문

# 트리 생성
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)

print(inorder_traversal(root))


# 8
# 1 W 2 3
# 2 F 4 5
# 3 R 6 7
# 4 O 8
# 5 T
# 6 A
# 7 E
# 8 S