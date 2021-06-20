k = int(input())
for _ in range(k):
    n, x, t = map(int, input().split())
    if x > t:
        print(0)
    else:
        b = t//x
        if(n>=b):
            ans = (n-b)*b
            ans += (b-1)*b//2
        else:
            ans = (n-1)*n//2
        print(ans)