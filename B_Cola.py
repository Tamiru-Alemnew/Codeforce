import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()


n , a , b , c = tip()
ans = 0 
mxa = a // 2
mic = max(0, (n - a // 2 - b) // 2)
for i in range(mic, min(n // 2, c) + 1):
    nab = n - i * 2
    ans += max(0, min(nab, b) - max(0, nab - mxa) + 1)
print(ans)
                    

