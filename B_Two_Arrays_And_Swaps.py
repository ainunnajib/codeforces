t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort(reverse=True)
    i = 0
    while i < k and i < n and b[i] > a[i]:
        a[i] = b[i]
        i += 1
    print(sum(a))