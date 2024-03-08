H,W = map(int,input().split())
map = [[] for i in range(H)]
count = 0
#横排除
for i in range(H):
    a = list(input())
    if '#' in a:
        for s in a:
            map[i-count].append(s)
    else:
        map.pop(i-count)
        count += 1
#縦排除
if len(map) == 1:
    ans = []
    for i in map[0]:
        if i != '.':
            ans.append(i)
    print(*ans,sep='')
else:
    for i,moji in enumerate(map[0]):
        if moji == '.':
            how = []
            for s in map:
                how.append(s[i])
            if '#' not in how:
                for n in map:
                    n.pop(i)
                
    for i in map:
        print(*i,sep='')
