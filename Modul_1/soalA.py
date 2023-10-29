import csv


def loadData():
    with open("account.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        lines = list(reader)
    return header, lines


def saveData(header, lines):
    with open("account.csv", "w", newline="") as file:
        write = csv.writer(file)
        write.writerow(header)
        write.writerows(lines)


header, lines = loadData()
# print(header)
# print(lines)


def login():
    user = input("Masukan user\t: ")
    password = input("Masukan Pass\t: ")
    for row in lines:
        # print("ID : "+ row[0]+ ", Name : "+ row[1]+ ", Role : "+ row[2]+ ", Nilai : "+ row[4])
        if user == row[1] and password == row[3]:
            return {"name": row[1], "id": row[0], "role": row[2]}
    return {"name": "None", "id": "None", "role": "none"}


def listPeserta():
    print("ID\t| Name\t| Role   \t| Nilai")
    for row in lines:
        if row[2] == "peserta":
            print(row[0] + "\t|" + row[1] + "\t|" + row[2] + "\t|" + row[4])


def inputDat(menu):
    listPeserta()
    pesertaID = str(input("Masukan Id dari peserta : "))
    for row in lines:
        if pesertaID == row[0]:
            loop = False
            while not loop:
                if menu == 1:
                    result = int(input("Masukan Nilai untuk peserta : "))
                    row[4] = str(result)
                    saveData(header, lines)
                    #
                    print(
                        "ID : "
                        + row[0]
                        + "| Name : "
                        + row[1]
                        + "| Role : "
                        + row[2]
                        + "| Nilai : "
                        + row[4]
                    )
                    return
                elif menu == 2:
                    result = int(input("Masukan Nilai Terbaru : "))
                    row[4] = str(result)
                    saveData(header, lines)
                    #
                    print(
                        "ID : "
                        + row[0]
                        + "| Name : "
                        + row[1]
                        + "| Role : "
                        + row[2]
                        + "| Nilai : "
                        + row[4]
                    )
                    return
    print("Peserta tidak ditemukan")


def showResult(userInfo):
    print("Data anda : ")
    print("ID : " + userInfo["id"] + "| Name : " + userInfo["name"])
    for row in lines:
        if row[0] == userInfo["id"]:
            print("Nilaimu : " + row[4])
            if int(row[4]) >= 75:
                print("Anda Lolos!!")
            else:
                print("Anda tidak Lolos")
    print("-----------------")


def admin():
    print("admin Menu")
    print("1. Input data")
    print("2. Rubah data")
    # print("3. Tambah peserta")
    # print("4. Hapus peserta")
    menu = int(input("Masukan Nomer Menu : "))
    if menu == 1:
        inputDat(menu)
    elif menu == 2:
        inputDat(menu)

    admin()


def peserta(userInfo):
    print("Menu Peserta")
    print("1. Menampilkan nilai & hasil akhir")
    # print(userInfo)
    menu = int(input("Pilih nomer menu : "))
    if menu == 1:
        showResult(userInfo)

    peserta(userInfo)


def main():
    userInfo = login()
    # print(userInfo)
    # print(userInfo["name"])
    if userInfo["role"] == "admin":
        admin()
    elif userInfo["role"] == "peserta":
        peserta(userInfo)
    elif userInfo["role"] == "none":
        print("User tidak ditemukan atau password salah.")
    else:
        print("Login Verify Error")
    main()


main()
