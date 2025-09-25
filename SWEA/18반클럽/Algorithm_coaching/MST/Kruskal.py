class DisjointSet:
    def __init__(self, v):
        self.p = [0]* (len(v)+1)
        self.rank = [0]*(len(v)+1)
        pass

    def make_set(self, x):
        self.p[x] = x
        self.rank[x] = x
        

    def find_set(self, x):
        if self.p[x] != x:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]
        

    def union_set(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                self.p[px] = py
            elif self.rank[px] > self.rank[py]:
                self.p[py] = px
            else:
                self.p[py] = px
                self.rank[px] += 1



def mst_kruskal(vertices, edges):
    mst = []
    n = len(vertices)
    edges.sort(key=lambda x:x[2])
    ds = DisjointSet(vertices)
    for i in range(n+1):
        ds.make_set(i)
    for edge in edges:
        s, e, w = edge
        if ds.find_set(s) != ds.find_set(e):
            ds.union_set(s, e)
            mst.append(edge)
    return mst


# [시작정점, 도착정점, 가중치]
edges = [[1, 2, 1], [2, 3, 3], [1, 3, 2]]
vertices = [1, 2, 3]  # 정점 집합

result = mst_kruskal(vertices, edges)  # [[1, 2, 1], [1, 3, 2]]
print(result)


# 교재 간선 정보
edges = [
    (0, 1, 32),
    (0, 2, 31),
    (0, 5, 60),
    (0, 6, 51),
    (1, 2, 21),
    (2, 4, 46),
    (2, 6, 25),
    (3, 4, 34),
    (3, 5, 18),
    (4, 5, 40),
    (4, 6, 51),
]
vertices = list(range(7))  # 정점 집합

result = mst_kruskal(vertices, edges)
print(result) # [(3, 5, 18), (1, 2, 21), (2, 6, 25), (0, 2, 31), (3, 4, 34), (2, 4, 46)]