n = int(input()) + 1
while(len(str(n)) > len(set(str(n)))): n+= 1
print(n)