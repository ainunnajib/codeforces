MAX = 100
p = [True for i in range(MAX)]
p[0], p[1] = False, False
for i in range(2, MAX):
    if p[i]:
        for x in range(i*i, MAX, i):
            p[x] = False
primes = set()
listprimes = []
for i in range(2, MAX):
    if p[i]:
        primes.add(i)
        listprimes.append(i)

t = int(input())
for _ in range(t):
    n = int(input())
    r = ['1', '1']
    r += ['0' for __ in range(n-2)]

    for i in range(n):
        s = r[i:] + r[:i]
        print(' '.join(s))
