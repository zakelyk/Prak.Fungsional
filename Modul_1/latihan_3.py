# Sistem penilaian mahasiswa

# Tambahkan fungsi untuk menghitung nilai akhir

# Tambahkan fungsi untuk menghitung semua nilai akhir


# Fungsi untuk menampilkan hasil nilai akhir
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))


# Program utama
def main():
    data_mahasiswa = {
        "Danu": {"UTS": 85, "UAS": 88},
        "Bahrul": {"UTS": 78, "UAS": 80},
        "fauzan": {"UTS": 90, "UAS": 92},
    }

    data_nilai_akhir = nilaiAkhir(
        data_mahasiswa
    )  # Menghitung nilai akhir semua mahasiswa

    tampilkan_nilai_akhir(data_nilai_akhir)


def nilaiAkhir(data_mahasiswa):
    nilaiAkhir = {}

    for nama, nilai in data_mahasiswa.items():
        rata_rata = (nilai["UAS"] + nilai["UTS"]) / 2
        nilaiAkhir[nama] = rata_rata

    return nilaiAkhir


if __name__ == "__main__":
    main()
