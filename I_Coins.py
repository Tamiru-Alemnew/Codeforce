import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n = ip()
""""
dp = 
[
  [1.0, 0.0, 0.0, 0.0],  # i = 0 (0 coins)
  [0.0, 0.0, 0.0, 0.0],  # i = 1 (1 coin)
  [0.0, 0.0, 0.0, 0.0],  # i = 2 (2 coins)
  [0.0, 0.0, 0.0, 0.0]   # i = 3 (3 coins)
]

"""
arr = list(map(float , input().split()))

prev = [ 0 for i in range(n+1)]  

prev[0] = 1

for i in range(1 , n+1):
    current = [0]*(n+1)

    for j in range(i+1):
        if j >= 1:
            current[j] += prev[j-1] * arr[i-1]

        current[j] += prev[j] * (1-arr[i-1])

    prev = current[:]

print(sum(current[n//2+1:]))

