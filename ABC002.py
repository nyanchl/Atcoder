#B
W = input()

res = ""
for i in range(len(W)):
  if W[i] not in set(["a","e","i","o","u"]):
    res += W[i]
    
print(res)