from bisect import *
n = int(input())
l = list(map(int, input().split()))
l.sort()
q = int(input())
for _ in range(q):
    print(bisect(l, int(input())))