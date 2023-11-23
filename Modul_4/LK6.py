def point(x, y):
    return x, y

def line_equation_of(p1, M):
    # Inner function untuk menghitung nilai C
    def calculate_intercept():
        return p1[1] - M * p1[0]

    # Panggil fungsi inner untuk mendapatkan nilai C
    C = calculate_intercept()

    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik (6,-2) dan bergradien -2:")
print(line_equation_of(point(6, -2), 2))
# print(line_equation_of(point(2, 7), 8))
# ubah nilai input dengan 3 digit NIM akhir kalian
# dan lakukan perhitungan manual sesuai rumus yang kalian gunakan dalam fungsi
# untuk membuktikan bahwa output suda benar
