t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = -1
    l = list(s)
    ch = set(l)
    for c in ch:
        i = 0
        j = n-1
        left = 0
        right = 0
        palindrome = True
        musterase = 0
        while i <= j:
            if s[i] == c:
                i += 1
                left += 1
                continue
            if s[j] == c:
                j -= 1
                right += 1
                continue
            if s[i] != s[j]:
                palindrome = False
                break
            musterase += abs(left-right)
            left = 0
            right = 0
            i += 1
            j -= 1

        if not palindrome:
            continue
        if ans < 0:
            ans = musterase
        else:
            ans = min(ans, musterase)
    print(ans)