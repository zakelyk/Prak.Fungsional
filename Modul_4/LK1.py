def perkalian(a):
    def dengan(b):
        nonlocal a
        return a * b
    return dengan

kali = perkalian(4)
hasil = kali(3)

print(hasil)