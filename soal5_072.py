n = int(input("Masukkan nilai n : "))
# Membuat input untuk pengguna memasukkan nilai n

for i in range(1, n + 1): # Loop luar untuk mengontrol jumlah baris
    for j in range(i): # Mencetak nilai i (nomor baris saat ini) diikuti dengan spasi
        print(i, end=" ") # end=" " digunakan agar angka dicetak pada baris yang sama
    print()
    # Pindah ke baris baru setelah selesai mencetak satu baris