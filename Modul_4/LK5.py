def point(x, y):
    return x, y

def line_equation_of(p1, p2):

    def calculate_M():
        return (p2[1] - p1[1]) / (p2[0] - p1[0])
    # pangggil fungsi inner untuk mendapatkan nilai M
    M = calculate_M()
    
    # tulis rumus untuk mendapatkan nilai C disini
    C = p1[1] - M * p1[0]
    
    return f"y = {M:.2f}x + {C:.2f}"

# ubah nilai input dengan 4 digit NIM terakhir Anda (1278)
# Lakukan perhitungan manual sesuai rumus yang digunakan dalam fungsi untuk membuktikan bahwa output sudah benar
print("Persamaan garis yang melalui titik A dan B:")
# print(line_equation_of(point(4, -2), point(-1, 3)))
print(line_equation_of(point(1, 2), point(7, 8)))