l = list(input())
l.extend(list(input()))
l.sort()
print('YES' if l == sorted(list(input())) else 'NO')