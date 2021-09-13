t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    done = False
    for i in range(n-1):
        if s[i:i+2] in ['ab', 'ba']:
            print(i+1, i+2)
            done = True
            break
    if not done:
        print(-1, -1)