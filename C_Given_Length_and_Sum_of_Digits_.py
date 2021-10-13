m, s = map(int, input().split())
dpmax = [[-1 for j in range(901)] for i in range(101)]
for i in range(10):
    dpmax[1][i] = i
for i in range(m+1):
    for j in range(s+1):
        for k in range(9, -1, -1):
            if dpmax[i-1][j-k] >= 0:
                dpmax[i][j] = k*(10**(i-1)) + dpmax[i-1][j-k]
                break

dpmin = [[-1 for j in range(901)] for i in range(101)]
for i in range(10):
    dpmin[1][i] = i
for i in range(m+1):
    for j in range(s+1):
        for k in range(10):
            if dpmin[i-1][j-k] >= 0:
                dpmin[i][j] = k*(10**(i-1)) + dpmin[i-1][j-k]
                break

a, b = dpmin[m][s], dpmax[m][s]
if s == 0 and m > 1:
    a, b = -1, -1
elif len(str(a)) < m:
    if dpmin[m-1][s-1] >= 0:
        a = 10**(m-1) + dpmin[m-1][s-1]
    else:
        a = -1
print(a, b)