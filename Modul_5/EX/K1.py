import matplotlib.pyplot as plt
from functools import reduce

# Data nilai-nilai ujian mahasiswa
nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

# Menghitung rata-rata menggunakan fungsi reduce
rata_rata = reduce(lambda x, y: x + y, nilai_mahasiswa) / len(nilai_mahasiswa)

# Membuat label mahasiswa (sumbu x) dalam bentuk fungsional dinamis (list-map-lambda)
label_mahasiswa = list(map(lambda x: f' {x+1}', range(len(nilai_mahasiswa))))

# Visualisasi data dalam bentuk diagram batang
plt.bar(label_mahasiswa, nilai_mahasiswa)

# Menambahkan garis putus-putus untuk rata-rata
plt.axhline(y=rata_rata, color='r', linestyle='--', label=f'Rata-rata: {rata_rata:.2f}')

plt.xlabel('Mahasiswa')
plt.ylabel('Nilai Ujian')
plt.title('Diagram Batang Nilai Ujian Mahasiswa')
plt.legend()
plt.show()
