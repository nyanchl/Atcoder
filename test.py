N = int(input())
S = input()
S_dict = {i:'' for i in S}
query = {}
late_query = {}
Q = int(input())
ans = []
for i in range(Q):
    c,d = map(str,input().split())
    S_dict[c] = d
    query[c] = d
    if d in query:
        late_query[c] = d
print(late_query)
for str in S:
    if S_dict[str]:
        ans.append(S_dict[str])
    else:
        ans.append(str)
for i,moji in enumerate(ans):
    if moji in late_query:
        ans[i] = late_query[moji]
print(*ans)
