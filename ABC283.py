#A
# A,B = map(int,input().split())
# ans = A
# for i in range(1,B):
#   ans *= A
# print(ans)

#B
# N = int(input())
# A = list(map(int,input().split()))
# Q = int(input())
# for n in range(Q):
#   query = list(map(int,input().split()))
#   if query[0]==2:
#     print(A[(query[1])-1])
#   elif query[0]==1:
#     A[(query[1])-1] = (query[2])