N,K = map(int,input().split())
A = list(map(int,input().split()))
left = A[0]
right = A[N-1]
while left < right:
    mid = (left + right)/2
    if mid>K:
        right = mid
    else:
        left = mid
if left == N:
    print(-1)
else:
    print(left)
