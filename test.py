# 式の左辺を計算する関数 f(x) を用意する
def f(N, x):
    print(N,x)
    ans = N + 1
    for i in range(5):
        ans = ans * x + 1
    return ans

N, M = map(float, input().split())

# 二分探索 (Xは 0 以上 100 以下であることがわかっている)
left = 0
right = 100
while (right-left>1e-4): # 精度が十分良くなるまで
    # left と right の 中点 mid をとる
    mid = (left+right)/2
    if (f(N, mid)<M): # もし f(mid) < N ならば答えは mid 以上 right 以下
        left = mid; # 範囲を狭める
    else: # そうでなければ答えは left 以上 mid 未満
      right = mid; # 範囲を狭める

# 答えは left 以上 right 以下であることがわかっている。
# 精度は十分なので、ここでは left の値を出力する。
ans = left
print(ans)