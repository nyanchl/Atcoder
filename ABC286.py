#A
# N, P, Q, R, S = map(int, input().split())
# A = list(map(int, input().split()))
# ans = A.copy()
# ans[P - 1:Q] = A[R - 1:S]
# ans[R - 1:S] = A[P - 1:Q]
# print(*ans)

#B
N = int(input())
S = input()
str = []
str1 = []
for i in range(len(S)):
    print(i)
    str.append(i)
    if str=="na":
        str1 += "nya"