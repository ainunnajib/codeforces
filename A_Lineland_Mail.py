n = int(input())
x = list(map(int, input().split()))
mind = [x[1]-x[0]]
maxd = [x[n-1]-x[0]]
for i in range(1, n-1):
    mind.append(min(x[i]-x[i-1], x[i+1]-x[i]))
    maxd.append(max(x[i]-x[0], x[n-1]-x[i]))
mind.append(x[n-1]-x[n-2])
maxd.append(x[n-1]-x[0])
for i in range(n):
    print(mind[i], maxd[i])