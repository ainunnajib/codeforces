t = int(input())
for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input()
    if s == c*n:
        print(0)
    else:
        if s[-1] == c:
            print(1)
            print(n)
        else:
            x = n-1
            u = set()
            while x > 0:
                if not (s[x-1] == c and n%x != 0):
                    if s[x-1] != c:
                        u.add(x)
                else:
                    nonedivisible = True
                    for i in range(2, n//x+1):
                        if i*x in u:
                            nonedivisible = False
                            break
                    if nonedivisible:
                        break
                x -= 1
            if x == 0:
                print(2)
                print(n-1, n)
            elif nonedivisible:
                print(1)
                print(x)
            else:
                print(2)
                print(n-1, n)