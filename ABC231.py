# #C
# N,Q = map(int,input().split())
# A = list(map(int,input().split()))
# A = sorted(A)
# for i in range(Q):
#     x = int(input())
#     left = 0
#     right = N
#     while (left != right):
#         mid = (left + right)//2
#         if (A[mid]>x):
#             right = mid
#         else:
#             left = mid+1
#     ans = left
#     print(N-ans)

N,Q = map(int,input().split())
A = list(map(int,input().split()))
A = sorted(A)
for i in range(Q):
    x = int(input())
    left = 0
    right = N
    while (left != right):
        mid = (left+right)//2
        if (A[mid]>x):
            right = mid
        else:
            left = mid+1
    ans = left
    print(N-ans)