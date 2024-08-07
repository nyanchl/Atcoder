A,B,C = map(int, input().split())
def main(A,B,C,count=0):
    if A == B == C:
        print(-1)
        exit()
    if A%2 == 1 or B%2 == 1 or C%2 == 1:
        print(count)
        exit()
    else:
        A_dash = (B + C) // 2
        B_dash = (C + A) // 2
        C_dash = (A + B) // 2
        A,B,C = A_dash,B_dash,C_dash
        count += 1
        return main(A,B,C,count)

main(A,B,C)

A, B, C = map(int,input().split())

ans = 0
while True:
    if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
        print(ans)
        exit()
    ans += 1
    A, B, C = (B+C)//2, (C+A)//2, (A+B)//2
    if A ==  B == C:
        print(-1)
        exit()