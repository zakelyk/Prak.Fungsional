data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

def filter_numbers(entry):
    return list(filter(lambda x: x.isdigit(), entry.split()))

for entry in data:
    print(filter_numbers(entry))
