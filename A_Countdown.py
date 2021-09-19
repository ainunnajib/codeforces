t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, list(input())))
    print(sum(l) + sum([x != 0 for x in l]) - int(l[-1]>0))