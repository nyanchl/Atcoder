# N,D = map(int,input().split())
# T = list(map(int,input().split()))
# for i in range(N-1):
#     if T[i+1] - T[i] <= D:
#         print(T[i+1])
#         exit()
 
# print("-1")

S = input()
nya = []
nyon = []
for i,str in enumerate(S):
    if "B" in str:
        nya.append(i+1)
    elif "R" in str:
        nyon.append(str)
    elif "K" in str:
        nyon.append(str)

if nya[0] == 1 or nya[1] == 1:
    print("No")
    exit()
elif nya[1]%nya[0]==0 and nyon.index("K") == 1:
    print("Yes")
    exit()
else:
    print("No")
    