import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

# primes including n
def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
 
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1


# prime factorization
n = ip()
ans = 0 

for i in range(2,n+1):
    cur = i

    d =  2 
    fac =set()
    while d*d <= cur:
        while cur % d == 0 :
            fac.add(d)
            cur //= d

        d += 1

    if cur > 1:
        fac.add(cur)



