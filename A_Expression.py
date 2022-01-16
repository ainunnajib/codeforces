# insert + and * operations between a, b and c so the result is maximum
a = int(input())
b = int(input())
c = int(input())
print(max(a + b + c, a * b * c, a + b * c, a * b + c, (a + b) * c, a * (b + c)))