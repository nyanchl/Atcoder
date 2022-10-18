A = list(map(int,input().split()))
S = sorted(A)
if S[2]-S[1]==S[1]-S[0]:
    print("Yes")
else:
    print("No")