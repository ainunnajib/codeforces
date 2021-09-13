t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(c) for c in input()]
    b = [int(c) for c in input()]
    x = [a[i]+b[i] for i in range(n)]
    ans = 0
    i = 0
    start = True
    zerozero = False
    oneone = False
    while i < n:
        if start:
            if x[i] == 1:
                ans += 2
                zerozero = False
                oneone = False
                start = True
            elif x[i] == 0:
                zerozero = True
                oneone = False
                start = False
            else:
                zerozero = False
                oneone = True
                start = False
        else:
            if oneone:
                if x[i] < 2:
                    ans += 2
                    start = True
            elif zerozero:
                if x[i] == 0:
                    ans += 1
                    zerozero = True
                    oneone = False
                    start = False
                elif x[i] == 1:
                    ans += 3
                    zerozero = False
                    oneone = False
                    start = True
                else:
                    ans += 2
                    zerozero = False
                    oneone = False
                    start = True

        i += 1
    if not start:
        if zerozero:
            ans += 1
    print(ans)