import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

a = cip()
b = cip()

aa = len(a)
bb = len(b)

dp = [[0] * (aa + 1) for _ in range(bb + 1)]


for i in range(1, bb + 1):
    for j in range(1, aa + 1):
        if b[i - 1] == a[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


ans = []

l = bb
r = aa

while l > 0 and r  > 0 :

    if b[l-1] == a[r-1]:
        ans.append(b[l-1])
        l -= 1
        r -= 1

    elif dp[l-1][r] > dp[l][r-1]:
        l -= 1

    else:
        r -= 1


ans = "".join(ans[::-1])
print(ans)

