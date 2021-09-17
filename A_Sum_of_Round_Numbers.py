n = int(input())
for _ in range(n):
    s = input()
    i = len(s)-1
    l = []
    for c in s:
        if c != '0':
            l.append(c+'0'*i)
        i -= 1
    print(len(l))
    print(' '.join(l))