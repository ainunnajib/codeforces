t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(0 if a%b == 0 else b-a%b)