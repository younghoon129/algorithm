def dfs(self):
    pass


# for t in range(1, 11):
v, e = map(int, input().split())
visited = [False] * (v+1)
box = [[]*i for i in range(v+1)]
b_list = list(map(int, input().split()))
for i in range(0, len(b_list), 2):
    box[b_list[i]].append(b_list[i+1])
print(box)