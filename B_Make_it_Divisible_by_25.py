t = int(input())
for _ in range(t):
    s = input()
    n = int(s)
    if n%25 == 0:
        print(0)
    else:
        ls = len(s)
        ans, i = ls+10, 0
        for p in ['00', '52', '05', '57']:
            i = 0
            for x in p:
                i += 1
                while i <= ls and s[-i] != x:
                    i += 1
            if i <= ls:
                ans = min(ans, i-2)
        print(ans)