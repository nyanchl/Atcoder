A,B,C = map(int,input().split())
d = C//A
s = C//B
if d>s:
    print(d)
else:
    print(s)