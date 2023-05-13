#A
# N = int(input())
# W = list(input().split())
# eng = ["and","not","that","the","you"]
# ans = "No"
# for i in range(N):
#     if W[i] in eng:
#         ans = "Yes"
#         print(ans)
#         exit()
# print(ans)

#B
R,C = map(int,input().split())
masu = []
for i in range(R):
    gyou = list(input().split())
    masu.append(gyou)
print(masu)