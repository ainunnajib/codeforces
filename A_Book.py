from heapq import *
t = int(input())
for _ in range(t):
    n = int(input())
    b = [[] for i in range(n+1)]
    d = [0 for i in range(n+1)]
    for i in range(1, n+1):
        l = list(map(int, input().split()))
        d[i] = l[0]
        for j in l[1:]:
            b[j].append(i)

    count = 0
    cursum = sum(d)
    if cursum == 0:
        print(1)
    else:
        possible = True
        canread = []
        for i in range(1, n+1):
            if d[i] == 0:
                heappush(canread, i)

        while True:
            if len(canread) == 0:
                break
            count += 1
            nextread = []
            while len(canread) > 0:
                x = heappop(canread)
                for c in b[x]:
                    d[c] -= 1
                    if d[c] == 0:
                        if c > x:
                            heappush(canread, c)
                        else:
                            heappush(nextread, c)
            canread = nextread

        print(count if sum(d) == 0 else -1)