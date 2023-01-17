#A
A,B = map(int,input().split())
ans = A
for i in range(1,B):
  ans *= A
print(ans)