import random

# 1. Membuat board dengan list comprehension
def buat_board(lebar, tinggi):
    return [['-' for _ in range(lebar)] for _ in range(tinggi)]

# 2. Buat generator posisi acak (kali ini kita maksimalkan 3x)
def random_posisi(lebar, tinggi):
    attempts = 0
    while attempts < 3:
        yield (random.randint(0, lebar - 1), random.randint(0, tinggi - 1))
        attempts += 1

# Mengatur gerakan bidak
def gerakkan_bidak(pos, langkah, lebar, tinggi):
    x, y = pos
    if langkah == "a" and x > 0: x -= 1
    if langkah == "d" and x < lebar-1: x += 1
    if langkah == "w" and y > 0: y -= 1
    if langkah == "s" and y < tinggi-1: y += 1
    return (x,y)

# Main game
def main():
    print("Selamat datang di permainan board game pemrograman fungsional")
    lebar = int(input("Masukkan lebar papan: "))
    tinggi = int(input("Masukkan tinggi papan: "))

    while True:
        board = buat_board(lebar, tinggi)
        pos_gen = random_posisi(lebar, tinggi)
        bidak = next(pos_gen)
        target = next(pos_gen)
        while bidak == target:  # Pastikan bidak dan target tidak di posisi yang sama
            target = next(pos_gen)

        # Menempatkan bidak dan target ke papan
        board[bidak[1]][bidak[0]] = 'A'
        board[target[1]][target[0]] = 'O'

        for row in board:
            print(' '.join(row))
        
        langkah = input("Apa langkahmu? (gunakan w, a, s, d): ")
        for l in langkah:
            board[bidak[1]][bidak[0]] = '-'
            bidak = gerakkan_bidak(bidak, l, lebar, tinggi)
            board[bidak[1]][bidak[0]] = 'A'

            # Cek menang atau kalah
            if bidak == target:
                print("Selamat! Kamu menang!")
                break
        else:
            print("Ups, kamu kalah! Coba lagi yuk!")

        lagi = input("Ingin coba lagi? (y/n): ").lower()
        if lagi != 'y':
            print("Sampai jumpa lagi, semoga beruntung di kesempatan berikutnya!")
            break

if __name__ == "__main__":
    main()
