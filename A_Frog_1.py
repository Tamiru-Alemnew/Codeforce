import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;
n = ip()

cost = tip()

dp = [0]*n
dp[0] = 0
for i in range(1 , n ):
    if i >= 2:
        dp[i] = min(abs(cost[i] - cost[i-1] ) + dp[i-1], dp[i-2] +  abs(cost[i] -cost[i-2]))
    else:
        dp[i] = abs(cost[i] - cost[i-1] ) + dp[i-1]

print(dp[-1])