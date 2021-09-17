s = input()
u = sum([c.isupper() for c in s])
print(s.upper() if u > len(s)//2 else s.lower())