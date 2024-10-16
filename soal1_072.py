def evaluasi_kinerja(persentase):
    # Fungsi 'evaluasi_kinerja' menerima satu parameter yaitu 'persentase'

    if persentase >= 90:
        # Jika persentase kinerja lebih besar atau sama dengan 90, maka tampilkan "Excellent performance"
        print("Excellent performance")
        
    elif persentase >= 80:
        # Jika persentase kinerja lebih besar atau sama dengan 80 tetapi kurang dari 90, maka tampilkan "Very Good performance"
        print("Very Good performance")
        
    elif persentase >= 70:
        # Jika persentase kinerja lebih besar atau sama dengan 70 tetapi kurang dari 80, maka tampilkan "Good performance"
        print("Good performance")
        
    elif persentase >= 60:
        # Jika persentase kinerja lebih besar atau sama dengan 60 tetapi kurang dari 70, maka tampilkan "Average"
        print("Average")
        
    else:
        # Jika persentase kinerja kurang dari 60, maka tampilkan "Below Average"
        print("Below Average")

# Menggunakan persentase siswa sebagai input (input)
persentase = float(input("Masukkan persentase siswa : "))

# Mencetak kinerja nya (output)
evaluasi_kinerja(persentase)