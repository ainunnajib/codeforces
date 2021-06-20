n = int(input())
jumlahsampaikotak = [0 for i in range(n+1)]
for i in range(n, 1, -1): # n, n-1, n-2, ..., 2
    print('?', 1, i)
    jumlahsampaikotak[i] = int(input())
print('?', 2, n)
keduasampaiakhir = int(input())

kotak = [0 for i in range(n+1)]
for i in range(n, 2, -1):
    kotak[i] = jumlahsampaikotak[i] - jumlahsampaikotak[i-1]

kotak[1] = jumlahsampaikotak[n] - keduasampaiakhir
kotak[2] = jumlahsampaikotak[2] - kotak[1]

jumlah = [str(kotak[i]) for i in range(1, n+1)]
print('!', ' '.join(jumlah))
