k, n, w = map(int, input().split())
print(max(k*w*(w+1)//2 - n, 0))