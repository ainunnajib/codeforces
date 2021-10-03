n = int(input())
l = list(map(int, input().split()))
print(n*max(l)-sum(l))