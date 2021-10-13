t = int(input())
for _ in range(t):
    n = int(input())
    print('YES' if n//2020 >= n%2020 else 'NO')