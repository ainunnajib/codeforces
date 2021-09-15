l = list(map(int, input().split('+')))
l.sort()
print('+'.join([str(c) for c in l]))
