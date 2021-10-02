l = list(map(int, input().split()))
l.sort()
print(l[1]-l[0] + l[2]-l[1])