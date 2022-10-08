n, k = map(int, input().split())
a = 'abcdefghijklmnopqrstuvwxyz'
x = a[:k]
print((x * (n//k)) + a[:n%k])