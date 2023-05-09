#A
N,A,B = map(int,input().split())
count = 0
c = list(map(int,input().split()))
for i in c:
    if i == A+B:
        ddd = c.index(A+B)
        count = 1+ddd
print(count)