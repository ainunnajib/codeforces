x = 0
for _ in range(int(input())):
    if '+' in input():
        x += 1
    else:
        x -= 1
print(x)