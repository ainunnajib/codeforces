s = ''
for c in input():
    if c not in ['a', 'i', 'u', 'e', 'o', 'y' , 'A', 'I', 'U', 'E', 'O', 'Y']:
        s += '.' + c.lower()
print(s)