N = int(input())
call = list(map(int,input().split()))
list = [False for _ in range(N)]
no = []
count = 0
for i,num in enumerate(call):
    if list[i] == True:
        continue
    list[num-1] = True
for i,n in enumerate(list):
    if n==False:
        count += 1
        no.append(i+1)
print(count)
print(*no)