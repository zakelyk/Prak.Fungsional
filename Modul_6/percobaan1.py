# TODO 0: Import library lain yang dibutuhkan
from PIL import Image, ImageDraw, ImageFont

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open("sample.jpg")

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
# draw = ImageDraw.Draw(gambarBW)
# direktoriFont = "BODONI BK BT BOOK.TTF"  # Ganti dengan direktori font yang kamu gunakan
# size = 24
# font = ImageFont.truetype(direktoriFont, size)
# text = "Nama: [Nama Anda]\nNIM: [NIM Anda]"
# # text_width, text_height = draw.textsize(text, font)
# text_width, text_height = draw.textbbox(text, font)
# text_x = (gambarku.width - text_width) // 2
# text_y = (gambarku.height - text_height) // 2
# draw.text((text_x, text_y), text, font=font, fill=255)

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarku.save("percobaan_satu.jpg")

# TODO 5: Tampilkan hasil akhir gambar
gambarku.show()
