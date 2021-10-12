n = int(input())
ok = False
for i in range(1, 1001):
    s = str(i)
    if sum([c in ['4', '7'] for c in s]) == len(s) and n%i == 0:
        ok = True
        break
print('YES' if ok else 'NO')
