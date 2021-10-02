t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    k -= 2
    if 2*m > n*(n-1) or m < n-1:
        print('NO')
    else:
        if k > 1:
            print('YES')
        else:
            if k == 1:
                if 2*m == n*(n-1):
                    print('YES')
                else:
                    print('NO')
            else:
                if n == 1:
                    if k >= 0:
                        print('YES')
                    else:
                        print('NO')
                else:
                    print('NO')