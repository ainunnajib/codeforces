s = input()
print(0 if s == '{}' else len(set(s[1:-1].split(', '))))