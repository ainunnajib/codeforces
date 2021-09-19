n = int(input())
d = {1:0, 2:0, 3:0, 4:0}
l = list(map(int, input().split()))
for x in l:
    d[x] += 1

count = d[4]
x = min(d[3], d[1])
count += x
d[1] -= x
d[3] -= x
count += d[2]//2
d[2] %= 2
count += d[2]
d[1] -= 2*d[2]
if d[1] > 0:
    count += d[1]//4
    d[1] %= 4
    if d[1] > 0:
        count += 1
if d[3] > 0:
    count += d[3]
print(count)