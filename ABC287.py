#A
# N = int(input())
# n = 0
# s = 0
# for i in range(N):
#     S = input()
#     if S=="For":
#         n += 1
#     else:
#         s += 1
# if n>s:
#     print("Yes")
# else:
#     print("No")

#B
# N,M = map(int,input().split())
# s = []
# count = 0
# for i in range(N):
#     S = int(input())
#     s.append(S)
# for i in range(M):
#     T = int(input())
# for i in s:
#     print(i[:-1])
#     for n in range(T):
#         if i[3:]==str(n):
#             count += 1

# N, M = map(int, input().split())
# S = [input() for _ in range(N)]
# T = [input() for _ in range(M)]

# cnt = 0
# for s in S:
#     if s[3:] in T:
#         cnt += 1
# print(cnt)


#C
# def dfs(p,list,seen):
#     seen[p] = True
#     for v2 in list[p]:
#         if seen[v2]: continue
#         dfs(v2, list, seen)
#     return

# N,M = map(int,input().split())

# list = [[]for _ in range(N)]

# for i in range(M):
#     u,v = map(int,input().split())
#     list[u].append(v)
#     list[v].append(u)

# for p in range(N):
#    list[p].sort()

# seen = [False for i in range(N)]
# ans = 0
# for p in range(N):
#     if seen[p] == True:
#         ans += 1
# print(ans)