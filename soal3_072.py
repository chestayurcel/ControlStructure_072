n = int(input("Masukkan nilai n : "))
# Membuat input untuk memasukkan nilai n yang merupakan jumlah elemen deret Fibonacci yang akan dihitung

a, b = 0, 1 # Inisialisasi dua angka pertama pada deret Fibonacci, yaitu 0 dan 1
hasil = [] # Membuat list kosong untuk menyimpan deret Fibonacci
for i in range(n):  # Mengulangi proses sebanyak n kali untuk menghasilkan deret Fibonacci
    hasil.append(a) # Menambahkan nilai a (angka pertama dari pasangan Fibonacci) ke dalam list hasil
    a, b = b, a + b # Memperbarui nilai a menjadi b dan nilai b menjadi hasil penjumlahan a + b

print("Deret Fibonacci hingga", n, ":", hasil)
# Mencetak deret Fibonacci yang telah disimpan dalam list hasil hingga elemen ke-n