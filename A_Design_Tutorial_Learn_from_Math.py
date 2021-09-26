def isprime(x):
    if x%2 == 0:
        return False
    for i in range(3, x, 2):
        if x%i == 0:
            return False
    return True

n = int(input())
a = 4
b = n-a
while isprime(a) or isprime(b):
    a += 1
    b = n-a
print(a, b)