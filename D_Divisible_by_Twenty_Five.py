s = input()
ways = 0
if len(s) == 1:
    if s in ['_', 'X', '0']:
        ways = 1
elif len(s) == 2:
    if s in ['25', '50', '75']:
        ways = 1
    elif s in ['__', '_X', 'X_']:
        ways = 3
    elif s == '_0':
        ways = 1
    elif s in ['_5', 'X5']:
        ways = 2
    elif s in ['2_', '5_', '7_', '2X', '5X', '7X', 'X0']:
        ways = 1
else:
    d = s[-2:]
    s = s[:-2]
    if d in ['00', '25', '50', '75', '__', '_X', 'X_', 'XX', '_0', '_5', '0_', '2_', '5_', '7_', 'X0', 'X5', '0X', '2X', '5X', '7X']:
        ways = 1
        xfound = False

        if d in ['__', '_X', 'X_']:
            ways *= 4
        elif d in ['_0', '_5', 'X0', 'X5']:
            ways *= 2
        
        if 'X' in d:
            xfound = True
        
        if s[0] == '_' or (s[0] == 'X' and not xfound):
            ways *= 9
        if s[0] == 'X':
            xfound = True

        if s[0] == 'X' and d in ['_X', 'X_', 'XX', '0X', 'X0', '5X']:
            if d == 'X0':
                ways //= 2
            elif d in ['_X', 'X_']:
                ways //= 4
                if d == 'X_':
                    ways *= 3
                else:
                    ways *= 2
            else:
                ways = 0

        if s[0] == '0':
            ways = 0

        for c in s[1:]:
            if c == '_':
                ways *= 10
            elif c == 'X' and not xfound:
                ways *= 10
                xfound = True

print(ways)