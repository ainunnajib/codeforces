t = int(input())
for _ in range(t):
    n = int(input())
    a = [0 if c == '1' else 1 for c in input()]
    sa = sum(a)
    if sa > 2 or sa == 0:
        print('YES')
        wins = []
        for i in range(n):
            if a[i] == 1:
                wins.append(i)
        against = {}
        for i in range(sa):
            against[wins[i]] = wins[(i+1)%sa]
        for i in range(n):
            line = ""
            for j in range(n):
                if i == j:
                    line += 'X'
                elif i in against and j == against[i]:
                    line += '+'
                elif j in against and i == against[j]:
                    line += '-'
                else: line += '='
            print(line)
    else:
        print('NO')