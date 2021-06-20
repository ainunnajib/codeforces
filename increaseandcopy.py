import math
t = int(input())
for _ in range(t):
    n = int(input())
    x = math.ceil(math.sqrt(n))
    steps = x - 1
    steps += math.ceil(n/x) - 1
    print(steps)
