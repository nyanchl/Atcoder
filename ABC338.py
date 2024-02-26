#A
S = [input()]
print(S)
count = 0
for num,str in enumerate(S):
    if num == 0 and str.islower() == False:
        count += 1
    elif num != 0 and str.islower() == False:
        count = 0
    else:
        print(str)
        count += 0
if count == 1:
    print("Yes")
else:
    print("No")