#A
# N = int(input())
# S = list(input())
# ans="Yes"
# for i in range(N-1):
#     if N==1:
#         ans="Yes"
#     elif S[i+1]==S[i]:
#         ans="No"
  
# print(ans)

#B
# 8x8のグリッドの状態を入力
S = [input() for _ in range(8)]
print(S)

# コマが置かれているマスを探索
for i in range(8):
    if "*" in S[i]:
        j = S[i].index("*")
        # 対応するマスの名前を出力
        print(chr(ord("a") + j) + str(9-(i+1)))
        break
