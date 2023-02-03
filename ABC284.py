#A
# N = int(input())
# list = []
# for i in range(N):
#     S = input()
#     list.append(S)
# newlist = reversed(list)
# for s in newlist:
#     print(s)

#B
T = int(input())
for i in range(T):
    ans = 0
    N = int(input())
    A = list(map(int,input().split()))
    for num in A:
        if num%2 == 1:
            ans += 1
    print(ans)
