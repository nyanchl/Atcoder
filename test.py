A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sum = sum(A)
B_sum = sum(B)
ans = A_sum - B_sum + 1
print(ans)
