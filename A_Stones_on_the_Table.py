n = int(input())
count = 0
x = ''
for c in input():
    if c == x:
        count += 1
    x = c
print(count)