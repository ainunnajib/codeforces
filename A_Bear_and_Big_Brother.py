a, b = map(int, input().split())
i = 0
while(a <= b):
    i += 1
    a *= 3
    b *= 2
print(i)