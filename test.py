N = int(input())
R = list(map(int,input().split()))
for i in range(1,N):
    now_num = R[i]
    index = i - 1
    while index >= 0 and now_num <= R[index]:
        R[index+1] = R[index]
        index -= 1
    R[index+1] = now_num
