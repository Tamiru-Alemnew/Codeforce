x = int(input())

for i in range(x):
    w = input()
    if len(w) > 10 :
        print(w[0]+str(len(w)-2)+w[len(w)-1])
    else:
        print(w)