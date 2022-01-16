s = input()
if s == s.upper():
    print(s.lower())
elif s[1:] == s[1:].upper():
    print(s[0].upper() + s[1:].lower())
else:
    print(s)