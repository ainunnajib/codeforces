n = int(input())
l = list(map(int, input().split()))
count = 0
for i in range(1, n-1):
    if l[i-1:i+2] == [1,0,1]:
        l[i+1] = 0
        count += 1
print(count)