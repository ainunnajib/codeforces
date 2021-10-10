t = int(input())
for _ in range(t):
    n = int(input())
    a = list(input())
    b = list(input())
    x = sum([a[i] == '1' and b[i] == '1' for i in range(n)])
    print('NO' if x > 0 else 'YES')