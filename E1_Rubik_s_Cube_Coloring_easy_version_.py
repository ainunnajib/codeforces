MODULO = 10**9+7

x = [4 for _ in range(62)]
for i in range(1, 62):
    x[i] = x[i-1]**2
    x[i] %= MODULO

k = int(input())
a = 6
for i in range(1, k):
    a *= x[i]
    a %= MODULO
print(a)