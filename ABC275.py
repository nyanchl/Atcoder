#A
# N = int(input())
# H = list(map(int, input().split()))
# print(H.index(max(H))+1)

#B
A,B,C,D,E,F = map(int, input().split())
print(((A*B*C)-(D*E*F))%998244353)