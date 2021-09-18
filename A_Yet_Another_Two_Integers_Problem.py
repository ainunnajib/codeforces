t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    x = abs(b-a)
    if x%10 == 0: print(x//10)
    else: print(x//10+1)