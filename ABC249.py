A,B,C,D,E,F,X = map(int,input().split())
takahasi= 0
aoki = 0
for i in range(X):
    if  0 <=i % (A+C) < A:
        takahasi +=B
    if  0 <=i % (D+F) < D:
        aoki +=E
if takahasi > aoki:
    print ("Takahashi")
elif takahasi < aoki:
    print ("Aoki")
else:
    print ("Draw")