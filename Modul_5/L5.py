from matplotlib import pyplot as plt

# Mengimpor fungsi normal dari pustaka numpy.random
# Digunakan untuk menghasilkan sampel data dari distribusi normal
from numpy.random import normal

# Mengimpor fungsi mean dan std dari pustaka numpy
# Digunakan untuk menghitung rata-rata dan standar deviasi data
from numpy import mean, std

# Mengimpor distribusi normal dari pustaka scipy.stats
# Digunakan untuk analisis statistik terkait distribusi normal
from scipy.stats import norm


#cara membuat sample data
sample = normal(loc=50, scale=5, size=1000)
#panggil variabel sample untuk mengetahui hasilnya:
#sample
#atau tampilkan dalam bentuk histogram:
plt.figure(figsize=(5,4)) #perkecil media gambar
plt.hist(sample, bins=10, density=True)

plt.show()