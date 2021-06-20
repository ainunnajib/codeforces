MOD = 10**9 + 7
n, x, pos = map(int, input().split())

#fact = [1 for i in range(n+1)]
#for i in range(1, n+1):
#    fact[i] = fact[i-1] * i

lt = 0
gt = 0
left = 0
right = n
while left < right:
    middle = (left + right) // 2
    if pos >= middle:
        if pos > middle:
            lt += 1
        left = middle + 1
    else:
        gt += 1
        right = middle

# (x-1) C lt * (n-x) C gt * (n - lt - gt - 1)!
if x-1 >= lt and (n-x) >= gt:
    c = 1
#    d = 2
    for i in range(x-1, x-1-lt, -1):
        c *= i
#        while d <= lt and c % d == 0:
#            c //= d
#            d += 1
    c %= MOD
    ans = c

    c = 1
#    d = 2
    for i in range(n-x, n-x-gt, -1):
        c *= i
#        while d <= gt and c % d == 0:
#            c //= d
#            d += 1
    c %= MOD
    ans = (ans * c) % MOD

    c = 1
    for i in range(1, n - lt - gt):
        c = (c * i) % MOD
    ans = (ans * c) % MOD
else:
    ans = 0

print(ans)
