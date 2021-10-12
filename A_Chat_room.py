s = input()
hello = 'hello'
i = -1
for c in hello:
    i += 1
    while i < len(s) and s[i] != c:
        i += 1
    if i == len(s):
        break
print('YES' if i < len(s) else 'NO')