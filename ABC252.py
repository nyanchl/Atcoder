#B
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# ans = "No"
# for i in range(K):
#   if A[B[i]-1] == max(A):
#     ans = "Yes"
# print(ans)

#C
n = int(input())
s = [input() for _ in range(n)]
cnt = [[0 for _ in range(10)] for _ in range(10)]
for i in range(n):
  for j in range(10):
    cnt[int(s[i][j])][j] = cnt[int(s[i][j])][j] + 1
mx = [0 for i in range(10)]
for i in range(10):
  for j in range(10):
    mx[i] = max(mx[i], 10 * (cnt[i][j] - 1) + j)
print(min(mx))