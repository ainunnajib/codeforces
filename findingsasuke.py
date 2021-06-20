t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    for i in range(n//2):
        l[i] *= -1
    
    s = [str(x) for x in l[::-1]]
    print(' '.join(s))
