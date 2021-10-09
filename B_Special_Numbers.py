t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    b = bin(k)[2:]
    a = 0
    p = 0
    for c in b[::-1]:
        if c == '1':
            a += n**p
            a %= 1000000007
        p += 1
    print(a)