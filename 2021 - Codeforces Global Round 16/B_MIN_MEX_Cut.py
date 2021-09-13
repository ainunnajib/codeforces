t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    if ('1' * n) == s:
        print(0)
    else:
        i = 0
        while i < n and s[i] == '1':
            i += 1
        while i < n and s[i] == '0':
            i += 1
        while i < n and s[i] == '1':
            i += 1
        if i == n:
            print(1)
        else:        
            print(2)
