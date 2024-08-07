N = int(input())
K = int(input())
x = list(map(int, input().split()))
x_dict = {i:0 for i in x}
for i in x:
    x_dict[i] += 1
ball_list = [False for _ in range(K)]
ans = 0
for i in x:
    ball_list[i] = True
for i, boolean in enumerate(ball_list):
    if boolean == True:
        kake = 1
        if x_dict[i] >= 1:
            kake = x_dict[i]
        before = i*kake
        behind = (K-i)*kake
        if before <= behind:
            ans += before*2
        else:
            ans += behind*2
print(ans)
