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

sample = normal(loc=50, scale=5, size=1000)
sample_mean = mean(sample) 
sample_std = std(sample)
dist = norm(sample_mean, sample_std)
dist

# pertama, buat list nilai yang akan digunakan dalam perhitungan
values = [value for value in range(30, 70)] #menggunakan list comprehension
# manfaatkan list comprehension untuk menerapkan method pdf
# berdasarkan value (yang telah disiapkan sebelumnya) pada data dist 
probabilitas = [dist.pdf(value) for value in values]
probabilitas # panggil variabel probabilitas untuk mengetahui hasilnya

print('Mean=%.3f \nStandard Deviation=%.3f' % (sample_mean, sample_std))

plt.hist(sample, bins=10, density=True) 
plt.plot(values, probabilitas)
plt.show()