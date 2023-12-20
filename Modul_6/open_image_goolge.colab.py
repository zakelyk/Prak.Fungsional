from google.colab import files
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
# Mengunggah gambar dari perangkat lokal ke Google Collab
uploaded = files.upload()
# Mendapatkan nama file gambar yang diunggah
uploaded_filename = next(iter(uploaded.keys()))
# Membaca gambar menggunakan Matplotlib Image
img = mpimg.imread(uploaded_filename)
# Menampilkan gambar
plt.imshow(img)
plt.axis('off') # Tidak menampilkan sumbu koordinat
plt.show()