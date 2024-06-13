N = int(input())
A = list(map(str,input().split()))
flag = True
while flag:
    flag = False
    for i in range(N-1,0,-1):
        if A[i] < A[i-1]:
            flag = True
            A[i],A[i-1] = A[i-1],A[i]
print(B)
