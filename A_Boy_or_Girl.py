s = set()
for c in input():
    s.add(c)
print('CHAT WITH HER!' if len(s)%2 == 0 else 'IGNORE HIM!')