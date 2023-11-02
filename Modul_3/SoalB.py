from functools import reduce

movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

def countGenres(movies):
    genres = {}
    genre_list = list(map(lambda movie: movie['genre'], movies))
    for genre in set(genre_list):
        count = len(list(filter(lambda movie: movie['genre'] == genre, movies)))
        genres[genre] = count
        # print(f"movie : {movie}")
        # print(f"genre : {genre}")
        # print(f'genres[{genre}] : {genres[genre]}')
    return genres

# print(countGenres(movies))

def ratingByYear(movies):
    yearList = {}
    for movie in movies:
        year = movie['year']
        if year not in yearList:
            yearList[year] = {'total':0, 'count': 0}
        yearList[year]['total'] += movie['rating']
        yearList[year]['count'] += 1
    # rate = {year: data['total']/data['count'] for year, data in yearList.items()}
    rate = reduce(lambda acc, year_data: {**acc, year_data[0]: year_data[1]['total'] / year_data[1]['count']}, yearList.items())
    return rate


# print(ratingByYear(movies))

def highestRate(movies):
    return max(movies, key=lambda x: x['rating'])

# print(highestRate(movies))

def info(title, movies):
    movie = list(filter(lambda movie: movie['title'] == title, movies))
    if not movie:
        return None
    return movie

def menu():
    while True:
        print("\nPilih tugas yang ingin dilakukan:")
        print("1. Menghitung jumlah film berdasarkan genre")
        print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
        print("3. Menemukan film dengan rating tertinggi")
        print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
        print("5. Selesai")
        choice = input("Masukkan nomor tugas (1/2/3/4/5): ")

        if choice == '1':
            print("Jumlah Film Berdasarkan Genre:")
            print(countGenres(movies))
        elif choice == '2':
            print("Rata-rata Rating Film Berdasarkan Tahun Rilis:")
            print(ratingByYear(movies))
        elif choice == '3':
            highest = highestRate(movies)
            print("\nInformasi Film:", highest['title'])
            print("Rating:", highest['rating'])
            print("Tahun Rilis:", highest['year'])
            print("Genre:", highest['genre'])
        elif choice == '4':
            title = input("Masukkan judul film yang ingin dicari: ")
            info = info(title, movies)
            if info:
                print("\nInformasi Film:", info['title'])
                print("Rating:", info['rating'])
                print("Tahun Rilis:", info['year'])
                print("Genre:", info['genre'])
            else:
                print("Film dengan judul tersebut tidak ditemukan.")
        elif choice == '5':
            break

menu()