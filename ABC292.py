#A
# S = input()
# print(S.upper())

#B
# N,Q = map(int,input().split())
# red = 0
# yellow = 0
# judge = [[] for _ in range(Q)]
# for i in range(Q):
#     event = list(map(int,input().split()))
#     judge[i].append(event)
#     if event[0]==1:
#         yellow += 1
#     elif event[0]==2:
#         red += 1
        
#     print(judge)

# n, q = map(int, input().split())
# P = [0]*n
# for _ in range(q):
#   e, x = map(int, input().split())
#   if e == 1:
#     P[x-1] += 1
#   elif e == 2:
#     P[x-1] = 2
#   else:
#     print('Yes' if P[x-1] == 2 else 'No')

#C
N = int(input())
list = []
for i in range(1,N):
    list.append(i)
print(list)
    