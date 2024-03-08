#B
N = int(input())
str_list = []

for i in range(N):
    a = int(input())
    str_list.append(a)

index = 0
count = 1
hoge = 0
while 2 != str_list[index]:
    if str_list[index] != 2:
        index = str_list[index] - 1
        count += 1
        hoge += 1
        if hoge >= N:
            count = -1
            break
print(count)

