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

sample = normal (size=1000)
plt.hist(sample, bins=10)
plt.show()