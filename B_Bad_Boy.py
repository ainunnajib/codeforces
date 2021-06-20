global maxdist, o, ans1, ans2

def dist(p, q):
    return abs(p[0]-q[0]) + abs(p[1]-q[1])

def checkpair(p, q):
    global maxdist, o, ans1, ans2
    newdist = dist(p, o) + dist(q, o) + dist(p, q)
    if newdist > maxdist:
        maxdist = newdist
        ans1, ans2 = p, q

t = int(input())
for _ in range(t):
    n, m, i, j = map(int, input().split())
    o = (i, j)
    a = (1, 1)
    b = (1, m)
    c = (n, 1)
    d = (n, m)

    maxdist = -1
    checkpair(a, b)
    checkpair(a, c)
    checkpair(a, d)
    checkpair(b, c)
    checkpair(b, d)
    checkpair(c, d)

    print(ans1[0], ans1[1], ans2[0], ans2[1])