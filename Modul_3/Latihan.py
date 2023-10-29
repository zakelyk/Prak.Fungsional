# def konversi(j=0):
#     def menit(m=0):
#       def detik(d=0):
#         return ((j*60)+m)*60+d
#       return detik
#     return menit

def konversi(minggu=0):
    def hari(h=0):
        def jam(j=0):
            def menit(m=0):
                return ((minggu*7+h)*24+j)*60+m
            return menit
        return jam
    return hari

# data = "05:33:05"

data = ["3 minggu 3 hari 7 jam 21 menit",
         "5 minggu 5 hari 8 jam 11 menit",
         "7 minggu 1 hari 5 jam 33 menit"]

# kita split data untuk mendapatkan nilai jam, menit, dan detik
# data_split = data.split(':')
# print("data = ",data)
# print("data split = ",data_split)

# kita simpan masing-masing valuenya dalam variabel terpisah
# jam = int(data_split[0])
# menit = int(data_split[1])
# detik = int(data_split[2])
for entry in data:
    data_split = entry.split(' ')
    minggu = int(data_split[0])
    hari = int(data_split[2])
    jam = int(data_split[4])
    menit = int(data_split[6])
# print("jam = ", jam)
# print("menit = ", menit)
# print("detik = ", detik)
    print("data = ",data)
    print("data split = ",data_split)
    print(entry)

    konvert = konversi(minggu)(hari)(jam)(menit)
    print("hasil konversi = ", konvert) #19985