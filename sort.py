N = int(input())
R = list(map(int, input().split()))
for i in range(1,N):
    v = R[i]
    j = i-1
    while j >= 0 and R[j] > v:
        R[j+1] = R[j]
        j -= 1
    R[j+1] = v
print(R)
