n = int(input("Masukkan nilai n : "))
# Membuat input untuk pengguna memasukkan nilai n sebagai batas akhir angka yang akan dicek

print("Angka ganjil hingga", n, ":") # Menampilkan teks untuk memberitahu bahwa program akan mencetak angka ganjil hingga nilai n
for i in range(1, n + 1): # Melakukan perulangan dari 1 hingga n dengan nilai i sebagai indeks
    if i % 2 != 0:
        # Mengecek apakah i adalah angka ganjil, yaitu jika i dibagi 2 tidak memiliki sisa
        print(i)
        # Jika i adalah ganjil, maka angka tersebut akan dicetak