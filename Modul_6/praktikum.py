# TODO 0: Import library yang dibutuhkan
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# TODO 1: Buka kedua gambar menggunakan Pillow
gambar_background = Image.open("path/to/background_image.jpg")
gambar_overlay = Image.open("path/to/overlay_image.jpg")

# TODO 2: Ubah gambar background menjadi hitam-putih (grayscale),
#         berotasi sebesar 30 derajat, dan blur
gambar_background = gambar_background.convert("L")  # Grayscale
gambar_background = gambar_background.rotate(30)  # Rotasi 30 derajat
gambar_background = gambar_background.filter(ImageFilter.BLUR)  # Blur

# TODO 3: Ubah tingkat kecerahan dan kontras gambar overlay
x = 12  # Ganti dengan 2 digit NIM akhir (contoh: 12)
y = 34  # Ganti dengan 2 digit NIM akhir (contoh: 34)

brightness_factor = 1.2  # Kecerahan 1.x kali lipat
contrast_factor = 1.3  # Kontras 1.y kali lipat

gambar_overlay = gambar_overlay.point(lambda i: i * brightness_factor)
gambar_overlay = gambar_overlay.point(lambda i: i * contrast_factor)

# Resize gambar overlay sesuai kebutuhan
width, height = gambar_background.size
gambar_overlay = gambar_overlay.resize((width, height))

# TODO 4: Sisipkan gambar overlay ke dalam gambar background
gambar_background.paste(gambar_overlay, (0, 0), gambar_overlay)

# TODO 5: Tambahkan teks "Informatika JOSSS!" pada gambar overlay
draw = ImageDraw.Draw(gambar_background)
font = ImageFont.load_default()  # Gunakan font default atau sesuaikan dengan path font Arial
text = "Informatika JOSSS!"
text_width, text_height = draw.textsize(text, font)
text_x = (gambar_background.width - text_width) // 2
text_y = (gambar_background.height - text_height) // 2
draw.text((text_x, text_y), text, font=font, fill=255)

# TODO 6: Simpan gambar hasil edit
gambar_background.save("tugas_praktikum_enam.jpg")

# Tampilkan hasil akhir gambar
gambar_background.show()
