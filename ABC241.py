N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
count = 0
ans = "No"
for i in B:
    if i in A:
        count += 1
        A.remove(i)
if count==M:
    ans = "Yes"
print(ans)