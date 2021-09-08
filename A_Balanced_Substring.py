t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    a = [1 if c == 'a' else -1 for c in s]
    
    ca = [0 for _ in range(n+1)]
    ca[0] = 0
    for i in range(1, n+1):
        ca[i] = ca[i-1] + a[i-1]
    
    seta = {}
    done = False
    for x in range(1, n+1):
        if ca[x] == 0:
            print(1, x)
            done = True
            break
        if ca[x] in seta:
            print(seta[ca[x]]+1, x)
            done = True
            break
        seta[ca[x]] = x
    if not done:
        print(-1, -1)