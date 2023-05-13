#A
# N = int(input())
# S = list(input())
# ans="Yes"
# for i in range(N-1):
#     if N==1:
#         ans="Yes"
#     elif S[i+1]==S[i]:
#         ans="No"
  
# print(ans)

#B
v = list("abcdefgh")

for i in range(8):
    s=input()
    if "*" in s:
        print(v[s.index("*")],end="")
        print(8-i)
        print(s.index("*"))