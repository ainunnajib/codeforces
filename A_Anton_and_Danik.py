n = int(input())
s = input()
a = s.count('A')
d = s.count('D')
if a == d: print('Friendship')
else: print('Anton' if a > d else 'Danik')