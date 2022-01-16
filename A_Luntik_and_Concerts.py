t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    if a%2 + b%2 + c%2 == 0:
        print(0)
    elif a%2 == 1 and b%2 + c%2 == 0:
        print(1)
    elif a%2 + c%2 == 0 and b%2 == 1:
        print(0)
    elif a%2 + b%2 == 0 and c%2 == 1:
        print(1)

    elif a%2 + b%2 + c%2 == 3:
        print(0)
    elif a%2 == 0 and b%2 + c%2 == 2:
        print(1)
    elif a%2 + c%2 == 2 and b%2 == 0:
        print(0)
    elif a%2 + b%2 == 2 and c%2 == 0:
        print(1)
