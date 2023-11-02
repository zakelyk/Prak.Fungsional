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
def totalPrice(transactions):
    return lambda trans: transactions['price'] * transactions['quantity']

# Fungsi untuk menyaring transaksi hanya untuk produk tertentu dengan HoF
def filterTCProduct(transactions, product):
    return list(filter(lambda transactions: transactions['product'] == product, transactions))

# Fungsi untuk menghitung jumlah item yang terjual
def soldItem(transactions, product):
    return sum(map(lambda item: item['quantity'], filterTCProduct(transactions, product)))

# Input nama produk yang ingin disaring
product_filter_input = input("Masukkan nama produk yang ingin disaring: ")
product = product_filter_input

print("totalPrice")
print(totalPrice(transactions))
print("filterTCProduct")
print(filterTCProduct(transactions, product))
print("soldItem")
print(soldItem(transactions, product))

# Menggunakan filter() untuk menyaring transaksi sesuai input produk
filtered = filterTCProduct(transactions, product_filter_input)
print(filtered)

# Menggunakan map() untuk menghitung total harga untuk setiap transaksi yang tersaring
TCTotal = list(map(totalPrice, filtered))
print(TCTotal)

# Menggunakan reduce() untuk menghitung total Pendapatan dari semua transaksi yang tersaring
totalFiltered = reduce(lambda x, y: x + y, TCTotal)

# Menampilkan Output
print(f"Transaksi Pembelian Produk {product_filter_input} :")
print(filtered)
