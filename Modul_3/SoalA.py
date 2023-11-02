from functools import reduce

transactions = [
    {"product": "Buku", "price": 10000, "quantity": 2},
    {"product": "Pensil", "price": 2000, "quantity": 5},
    {"product": "Pensil", "price": 2000, "quantity": 3},
    {"product": "Pulpen", "price": 5000, "quantity": 2},
    {"product": "Buku", "price": 12000, "quantity": 1},
    {"product": "Pulpen", "price": 6000, "quantity": 4}
]

# Fungsi untuk menghitung total harga transaksi menggunakan lambda
calculateTotal = lambda transaction: transaction["price"] * transaction["quantity"]

# Fungsi untuk menyaring transaksi hanya untuk produk tertentu dengan HoF
def filterTransactions(product, transactions):
    return list(filter(lambda transaction: transaction["product"] == product, transactions))

# Fungsi untuk menghitung jumlah item yang terjual
def countSold(product, transactions):
    return sum(map(lambda transaction: transaction["quantity"], filterTransactions(product, transactions)))

# Input nama produk yang ingin disaring
filterInput = input("Masukkan nama produk yang ingin disaring: ")

# Menggunakan filter() untuk menyaring transaksi sesuai input produk
filtered = filterTransactions(filterInput, transactions)

# Menampilkan transaksi produk tertentu
print(f"Transaksi Pembelian Produk {filterInput}:")
for transaction in filtered:
    print(transaction)

# Menggunakan map() untuk menghitung total harga untuk setiap transaksi yang tersaring
TCtotals = list(map(calculateTotal, filtered))

# Menampilkan total harga untuk setiap transaksi produk tertentu
print("\nTotal Harga untuk Setiap Transaksi Produk", filterInput + ":")
for total in TCtotals:
    print(total)

# Menggunakan reduce() untuk menghitung total Pendapatan dari semua transaksi yang tersaring
revenue = reduce(lambda acc, total: acc + total, TCtotals, 0)

# Menampilkan Total Pendapatan dan Total Jumlah Item Terjual
print("\nTotal Pendapatan dari Transaksi Produk", filterInput + ":", revenue)
totalSold = countSold(filterInput, transactions)
print("Total Jumlah Item Terjual dari Produk", filterInput + ":", totalSold)
