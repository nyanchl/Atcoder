#B
N = int(input())
S = input()

x = 0
max_x = 0
for i in range(N):
  if S[i] == "I":
    x += 1
  elif S[i] == "D":
    x -= 1

  max_x = max(max_x, x)
  
print(max_x)
    