import matplotlib.pyplot as plt
from functools import reduce

# Data nilai-nilai ujian mahasiswa
nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

# TODO 1: Menghitung rata-rata menggunakan fungsi reduce
mean = reduce(lambda x,y:x+y, nilai_mahasiswa) / len(nilai_mahasiswa)
# TODO 2: Membuat label mahasiswa (sumbu x) dalam bentuk fungsional dinamis (list-map-lamda)
label = list(map(lambda x:f'{x+1}', range(len(nilai_mahasiswa))))
# TODO 3: Visualisasi data dalam bentuk diagram batang
plt.bar(label,nilai_mahasiswa)
plt.axhline(y=mean, color='r', linestyle='--', label=f'Rata-Rata: {mean:.2f}')
plt.xlabel('Mahasiswa')
plt.ylabel("Nilai")
plt.title("Nilai Ujian")
plt.legend(loc='upper left')
plt.show()