d = {'Tetrahedron':4, 'Cube':6, 'Octahedron':8,
     'Dodecahedron':12, 'Icosahedron':20}
n = int(input())
ans = 0
for _ in range(n):
    ans += d[input()]
print(ans)