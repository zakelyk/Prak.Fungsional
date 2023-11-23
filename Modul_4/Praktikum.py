import math

def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    def calculate_M():
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    M = calculate_M()
    C = p1[1] - M * p1[0]

    return f"y = {M:.2f}x + {C:.2f}"

def translasi(p):
    x, y = p
    def transform(trans):
        tx, ty = trans
        return x + tx, y + ty
    return transform

def rotation(p):
    x, y = p
    def transform(rotate):
        radian = math.radians(rotate)
        return x * math.cos(radian) - y * math.sin(radian), y * math.sin(radian) + x * math.cos(radian)
    return transform

def scaling(scale_factors):
    sx, sy = scale_factors

    def transform(p):
        return p[0] * sx, p[1] * sy

    return transform


def combined_transform(p, transforms):
    for transform in transforms:
        p = transform(p)
    return p

# Input data berdasarkan NIM dan perhitungan
nim = input("Masukkan 3 digit terakhir NIM Anda: ")
x = int(nim[0])
y = int(nim[1])
z = int(nim[2])

# Tentukan titik A, B, dan gradien berdasarkan ketentuan
A = point(x, y)
B = point(y, z)
gradien = x
tx = y
ty = z
sx = z
sy = x

# Hitung persamaan garis yang melalui titik A dan B
original_equation = line_equation_of(A, B)
print(f"Persamaan garis yang melalui titik A dan B:\n{original_equation}")

# Lakukan transformasi beruntun sesuai ketentuan
transforms = [translasi((2, -3)), rotation(60), scaling((1.5, 2))]

# Lakukan transformasi terhadap titik A
transformed_A = combined_transform(A, transforms)

# Hitung persamaan garis setelah transformasi
transformed_equation = line_equation_of(transformed_A, B)
print(f"Persamaan garis baru setelah transformasi :\n{transformed_equation}")
