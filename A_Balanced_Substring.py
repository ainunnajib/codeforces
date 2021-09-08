t = int(input())
for _ in range(t):
    n = int(input())
    a = [1 if c == 'a' else -1 for c in input()]
    
    done = False
    for i in range(n-1):
        if a[i] + a[i+1] == 0:
            print(i+1, i+2)
            done = True
            break
    if not done:
        print(-1, -1)