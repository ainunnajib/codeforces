t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    print('YES' if sum(l) == m else 'NO')
