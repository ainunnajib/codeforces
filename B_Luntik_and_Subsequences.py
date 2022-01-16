t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    ones = l.count(1)
    zeros = l.count(0)
    print(ones * 2**zeros)