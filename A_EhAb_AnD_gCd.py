t = int(input())
for _ in range(t):
    x = int(input())
    if x%2 == 0:
        print(x//2, x//2)
    else:
        print(1, x-1)