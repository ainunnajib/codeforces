t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(1, n):
        print('()'*(n-i) + '('*i + ')'*i)
    if n > 2:
        print('('*(n-1) + ')(' + ')'*(n-1))
    elif n == 2:
        print('(())')
    else:
        print('()')