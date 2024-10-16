n = int(input("Masukkan nilai n: "))
# Membuat input untuk pengguna memasukkan nilai n sebagai batas akhir angka yang akan dicek

print("Angka ganjil hingga", n, ":")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)