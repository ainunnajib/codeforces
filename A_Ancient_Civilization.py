t = int(input())
for _ in range(t):
    n, l = map(int, input().split())
    x = list(map(int, input().split()))
    b = [bin(i)[2:].zfill(l)[::-1] for i in x]
    ans = 0
    m = 1
    for i in range(l):
        c = 0
        for j in range(n):
            if b[j][i] == '1':
                c += 1
        if c * 2 > n:
            ans += m
        m *= 2
    print(ans)