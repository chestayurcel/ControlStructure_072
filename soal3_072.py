a, b = 0, 1
hasil = []
9
for i in range(n):
    hasil.append(a)
    a, b = b, a + b

print("Deret Fibonacci hingga", n, ":", hasil)

n = int(input("Masukkan nilai n: "))