#A
# N = int(input())
# A = list(map(int,input().split()))
# guu = []
# for i in A:
#     if i%2==0:
#         guu.append(i)
# print(*guu)

#B
H,W = map(int,input().split())
eng = [chr(ord("A")+i) for i in range(26)]
for i in range(H):
    A = map(int,input().split())
    ans = []
    for i,num in enumerate(A):
        if num == 0:
            ans.append(".")
        else:
            ans.append(eng[num-1])
    print(*ans,sep="")
