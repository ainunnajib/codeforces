t = int(input())
for _ in range(t):
    n = int(input())
    if n%4 == 0:
        print('YES')
        evens = [str(i) for i in range(2, n+1, 2)]
        odds = [str(i) for i in range(1, n, 2)]
        k = n//2
        odds[-1] = str(k*(k+1) - (k-1)**2)

        print(' '.join(evens), ' '.join(odds))
    else:
        print('NO')