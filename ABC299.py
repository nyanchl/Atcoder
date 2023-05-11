#A
n=int(input())
S=list(input())
 
flag=0
for i in range(0,n):
  if(S[i]=='|'):
    flag+=1
  if(S[i]=='*' and flag==1):
    print("in")
    exit()
    
print("out")