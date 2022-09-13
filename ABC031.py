#A
A,D = map(int,input().split())
if (A+1)*D>(D+1)*A:
    print((A+1)*D)
else:
    print((D+1)*A)