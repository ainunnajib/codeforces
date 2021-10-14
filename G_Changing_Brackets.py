t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    b = [-1 for i in range(n)]
    for i in range(n):
        if s[i] in '[]':
            b[i] = i%2
    l0 = [0 for i in range(n)]
    l1 = [0 for i in range(n)]
    c0, c1 = 0, 0
    for i in range(n):
        if b[i] == 0:
            c0 += 1
        elif b[i] == 1:
            c1 += 1
        l0[i] = c0 
        l1[i] = c1 

    q = int(input())
    for __ in range(q):
        a, b = map(int, input().split())
        if a > 1:
            print(abs((l0[b-1]-l0[a-2]) - (l1[b-1]-l1[a-2])))
        else:
            print(abs(l0[b-1] - l1[b-1]))