#A
N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
ans = A.copy()
ans[P - 1:Q] = A[R - 1:S]
ans[R - 1:S] = A[P - 1:Q]
print(*ans)
