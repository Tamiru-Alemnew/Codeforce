def find():
    n = int(input())
    if n % 2 == 0:
        ans = "1" * (n // 2)
    else:
        ans = "7" + "1" * ((n - 3) // 2)
    return ans

t = int(input())
for _ in range(t):
    print(find())