def enough(n, m, k, v):
    x = n
    if k >= v:
        x += v*(v+1)//2
    else:
        x += k*(k+1)//2 + (v-k)*k
    if (n-k) >= v-1:
        x += (v-1)*v//2
    else:
        x += (n-k)*(n-k+1)//2 + (v-1-n+k)*(n-k)
    return m >= x

n, m, k = map(int, input().split())
a = 0
b = m
while a < b-1:
    v = (a+b)//2
    if enough(n, m, k, v):
        a = v
    else:
        b = v
print(a+1)