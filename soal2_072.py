num1 = float(input("Masukkan angka pertama : "))
num2 = float(input("Masukkan angka kedua : "))
num3 = float(input("Masukkan angka ketiga : "))
# Membuat input untuk memasukkan tiga angka

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("Angka terbesar adalah : ", largest)