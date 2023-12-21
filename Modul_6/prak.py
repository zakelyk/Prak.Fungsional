import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance

background = Image.open("campus.jpg")
logo = Image.open("umm.png")

background = background.convert("L")
background =  background.rotate(30)
background = background.filter(ImageFilter.BLUR)

brightness = ImageEnhance.Brightness(logo)
contrast = ImageEnhance.Contrast(logo)
logo = brightness.enhance(1.7)
logo = contrast.enhance(1.8)
logo_size = (500,500)
logo = logo.resize(logo_size)

background.paste(logo, (150,0), logo)

text = "Informatika JOSSS!"
font = ImageFont.truetype("arial.ttf", 24)
draw = ImageDraw.Draw(background)

draw.text((300, 450), text, font=font)

background.save("tugas_praktikum_enam.jpg")

plt.imshow(mpimg.imread("tugas_praktikum_enam.jpg"), cmap='gray')
# plt.imshow(mpimg.imread("tugas_praktikum_enam.jpg"))
plt.axis('off') # Tidak menampilkan sumbu koordinat
plt.show()

# background.show()