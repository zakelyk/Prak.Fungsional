from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# Data tinggi badan individu dalam sentimeter
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10  # Misalnya interval ukuran per 10 sentimeter

# TODO 1: buat Fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def heightGrouping(tinggi_badan, interval_size):
    return [(tinggi // interval_size) * interval_size for tinggi in tinggi_badan]

interval_limit = np.arange(min(tinggi_badan), max(tinggi_badan) + interval_size, interval_size)
heightGroup = heightGrouping(tinggi_badan, interval_size)
# TODO 2: Menghitung frekuensi tinggi badan dalam interval
def freq(heightGroup):
    frekuensi = {}
    for tinggi in heightGroup:
        frekuensi[tinggi] = frekuensi.get(tinggi, 0) + 1
    return frekuensi

frequency = freq(tinggi_badan)
# TODO 3: Visualisasi data dalam bentuk histogram
def histogram(tinggi_badan, bins, interval_size):
    plt.hist(tinggi_badan, bins=bins, width=interval_size,density=True)
    plt.xlabel('Tinggi Badan (cm)')
    plt.ylabel('Frekuensi Normalisasi')
    plt.title('Histogram Tinggi Badan')

histogram(heightGroup, bins=interval_limit,interval_size=interval_size)
# TODO 4: Menambahkan kurva pdf pada hasil visualisasi data
def pdf_curve(tinggi_badan, interval_limit):
    mean, std = np.mean(tinggi_badan), np.std(tinggi_badan)
    x = np.linspace(min(interval_limit), max(interval_limit), 100)
    pdf = norm.pdf(x, mean, std)
    plt.plot(x, pdf, label='Kurva PDF', color='red')

pdf_curve(tinggi_badan, interval_limit)


plt.legend(loc='lower left')
plt.show()
