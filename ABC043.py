#B
s = input()
ans = []
for i,str in enumerate(s):
    if (len(ans)>0) and str=='B':
        del ans[i-1]
    elif str== 'B':
        continue
    else:
        ans.append(str)

print(*ans,sep='')