#A
# K = int(input())
# english = ["A", "B", "C", "D", "E", "F","G","H", "I", "J", "K", "L", "M", "N","O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"]
# list = []
# for i in range(K):
#     list.append(english[i])
# ls = ''.join(list)
# print(ls)

#B
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())

#     # 頂点 A から頂点 B への辺を張る
    G[A].append(B)
print(G[A])
# # 頂点 v ごとに、終点頂点を番号順にして出力
# for v in range(N):
#     # 番号順に
#     G[v].sort()

#     # 頂点 v の隣接リストの頂点を順に出力
#     for to in G[v]:
#         print(to, end=' ')
#     print()