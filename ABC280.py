#C
# S = input()
# T = input()
# for i in range(len(S)):
#     if S[i] != T[i]:
#         print(i+1)

#A
count = 0
A,B = map(int,input().split())
for i in range(A):
    B = input()
    count += B.count("#")
print(count)