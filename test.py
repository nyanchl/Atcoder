N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
count = 0
point= 0
for i,str in enumerate(A):
    if A[i] == B[i]:
        count += 1
    if str in B:
        point += 1
print(count)
print(point-count)