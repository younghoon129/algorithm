T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nodes = [[] for _ in range(N+1)]
    answer = 1
    visi = [False] * (N+1)
    def dfs(n, dist):
        global answer
        if visi[n]:
            return
        
        if not nodes[n]:
            answer = max(answer, dist)
            return

        for nxt_node in nodes[n]:
            if visi[nxt_node]:
                continue


    for _ in range(M):
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)
    
    for i in range(N):
        if nodes[i]:
            dfs(i, 0)
            break