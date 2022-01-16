t = int(input())
for _ in range(t):
    n = int(input())
    possible = True
    al = [[] for i in range(n)]
    edgenum = {}
    for i in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        al[a].append(b)
        al[b].append(a)
        edgenum[(a, b)] = i
        edgenum[(b, a)] = i
    for i in range(n):
        if len(al[i]) > 2:
            possible = False
            break
    if not possible:
        print(-1)
    else:
        startnode = 0
        for i in range(n-1):
            if len(al[i]) < 2:
                startnode = i
                break
        l = [0 for i in range(n-1)]
        done = set()
        for x in range(n-1):
            nextnode = al[startnode][0]
            if nextnode in done:
                nextnode = al[startnode][1]
            i = edgenum[(startnode, nextnode)]
            l[i] = 2 + x%2
            done.add(startnode)
            startnode = nextnode
        print(*l)
