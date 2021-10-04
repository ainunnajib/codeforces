t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    s = sorted(a)
    if a == s:
        print('YES')
    else:
        if 2*x > n-1:
            if s[n-x:x] == a[n-x:x]:
                print('YES')
            else:
                print('NO')
        else:
            print('YES')