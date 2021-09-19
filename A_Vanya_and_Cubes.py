n = int(input())
h = 1
while n >= h*(h+1)//2:
    n -= h*(h+1)//2
    h += 1
print(h-1)