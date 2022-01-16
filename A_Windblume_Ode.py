from itertools import combinations

isprime = [True for i in range(20000)]
for i in range(2, 20000):
    for x in range(i*i, 20000, i):
        isprime[x] = False
allprimes = set()
for i in range(2, 20000):
    if isprime[i]:
        allprimes.add(i)

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    s = sum(l)
    ex = set()
    ans = list(range(1, n+1))
    done = False
    if s in allprimes:
        for i in range(1, n+1):
            for x in combinations(ans, i):
                ss = s - sum([l[j-1] for j in x])
                if ss not in allprimes:
                    ex = set(x)
                    done = True
                    break
            if done:
                break
    p = []
    for x in ans:
        if x not in ex:
            p.append(str(x))
    print(len(p))
    print(' '.join(p))