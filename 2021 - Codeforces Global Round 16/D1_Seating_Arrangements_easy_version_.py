t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    sortedl = sorted(l)
    ls = sorted(list(set(sortedl)))
    count = {}
    for x in ls:
        count[x] = 0
    ans = 0
    for x in l:
        for y in ls:
            if x <= y:
                break
            ans += count[y]
        count[x] += 1
    print(ans)