class DisjointSet:
    def __init__(self, v):
        self.p = [0]*(len(v))
        self.rank = [0]*(len(v))

    def make_set(self, x):
        self.p[x] = x
        self.rank[x] = 0

    def find_set(self, x):
        if self.p[x] != x:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

    def union_set(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.p[py] = px
            elif self.rank[px] < self.rank[py]:
                self.p[px] = py
            else:
                self.p[py] = px
                self.rank[px] += 1


def mst_kruskal(box, edges):
    mst = 0
    dj = DisjointSet(box)
    for i in range(len(box)):
        dj.make_set(i)
    edges.sort(key=lambda x: x[2])
    for edge in edges:
        s, e, w = edge
        if dj.find_set(s) != dj.find_set(e):
            dj.union_set(s, e)
            mst += w
    return mst


tc = int(input())
for t in range(1, tc+1):
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    box = list(range(n+1))
    result = mst_kruskal(box, edges)
    print(f"#{t} {result}")