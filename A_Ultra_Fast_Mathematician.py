a = list(map(int, list(input())))
b = list(map(int, list(input())))
c = [str((a[i]+b[i])%2) for i in range(len(a))]
print(''.join(c))