n, k, x = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
gaps = []
for i in range(1, n):
    if l[i]-l[i-1] > x:
        gaps.append((l[i]-l[i-1]-1)//x)
gaps.sort()
ans = len(gaps)+1
for g in gaps:
    if k >= g:
        k -= g
        ans -= 1
    else:
        break
print(ans)