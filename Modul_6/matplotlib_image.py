import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# Membaca dan menampilkan gambar
img = mpimg.imread('sample.jpg') #Sesuaikan dengan direktori letak gambar tersimpan
plt.imshow(img)
plt.axis('off') # Tidak menampilkan sumbu koordinat
plt.show()