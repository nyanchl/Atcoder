def rec(v ,G ,seen):
    seen[v] = True
    for v2 in G[v]:
        if seen[v2]: continue
        rec(v2, G, seen)
    return
        

N,M = map(int,input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
seen = [False for i in range(N)]
print(G)

rec(0 ,G ,seen)

ans = 'Yes'

for v in range(N):
    if seen[v] == False: ans = 'No'
print(ans)
