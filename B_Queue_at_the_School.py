n, t = map(int, input().split())
s = input()
q = [c for c in s]
for _ in range(t):
    i = 0
    while(i<n-1):
        if q[i] == 'B' and q[i+1] == 'G':
            q[i] = 'G'
            q[i+1] = 'B'
            i += 2
        else:
            i += 1
print(''.join(q))