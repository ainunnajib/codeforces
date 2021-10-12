n = int(input())
l = list(map(int, input().split()))
s = sum(l)
l.sort(reverse=True)
x = 0
while sum(l[:x+1])*2 <= s:
    x += 1
print(x+1)