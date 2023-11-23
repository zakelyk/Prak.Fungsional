import math

A = 3,4
B = 5,6

tx = 2
ty = -3
trans = tx, ty

rotasi = 60

sx = 1.5
sy = 2
dilat = sx, sy

def translasi(func):
    def transform(p):
        tx,ty=trans
        x,y = p
        return func((x+tx, y+ty))
    return transform

def rotation(func):
    def transform(p):
        x,y = p
        radian = math.radians(rotasi)
        return func((x*math.cos(radian) - y*math.sin(radian), y*math.sin(radian) + x*math.cos(radian)))
    return transform

def dilatasi(func):
    def transform(p):
        sx,sy=dilat
        x,y=p
        return func((x*sx,y*sy))
    return transform

def line_equation_of(p1, p2=None, M=None):
    if p2 is not None:
        M = (p2[1] - p1[1]) / (p2[0] - p1[0])

    C = p1[1] - M * p1[0]

    return f"y = {M:.2f}x + {C:.2f}"

@translasi
@rotation
@dilatasi
def multiTransform(p):
    return p

transformedA = multiTransform(A)
transformedB = multiTransform(B)
# print(f"A ({transformedA}) B ({transformedB})")

equation = line_equation_of(A, B)
transformedEquation = line_equation_of(transformedA, transformedB)
# print(equation)

print("Soal :")
print(f"hasil persamaan garis yang melalui titik {A} dan {B} :")
print(equation)
print(f"Persamaan garis baru setelah transformasi :")
print(transformedEquation)
#---------------------------------------------------------------------------------#
attempt = True
while attempt is True:
    try:
        nim_input = input("\nMasukkan NIM (3 digit terakhir): ")
        if len(nim_input) != 3 or not nim_input.isdigit():
            print("Input NIM harus berupa 3 digit angka.")
            input()

        x = int(nim_input[0])
        y = int(nim_input[1])
        z = int(nim_input[2])

        A = (x, y)
        B = (y, z)
        M = x
        tx = y
        ty = z
        sx = z
        sy = x
        trans = tx, ty
        dilat = sx, sy

        transformedA = multiTransform(A)
        transformedB = multiTransform(B)
        # print(f"A ({transformedA}) B ({transformedB})")

        equation = line_equation_of(A, None, M)
        transformedEquation = line_equation_of(transformedA, transformedB)
        # print(equation)

        print(f"\nNIM : {nim_input}")
        print(f"hasil persamaan garis yang melalui titik {A} dan gradien {M} :")
        print(equation)
        print(f"Persamaan garis baru setelah transformasi :")
        print(transformedEquation)

        transformedA = multiTransform(A)
        transformedB = multiTransform(B)
        # print(f"A ({transformedA}) B ({transformedB})")

        equation = line_equation_of(A, B)
        transformedEquation = line_equation_of(transformedA, transformedB)
        # print(equation)

        print(f"\nhasil persamaan garis yang melalui titik {A} dan {B} :")
        print(equation)
        print(f"Persamaan garis baru setelah transformasi :")
        print(transformedEquation)
        attempt = False
    except ValueError:
        print("Input harus berupa NIM 3 angka")
    except IndexError:
        print("Inout hanya boleh 3 angka")