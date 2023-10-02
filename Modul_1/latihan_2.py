random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

floats = []
strings = []
ints = {"satuan": [], "puluhan": [], "ratusan": []}

for item in random_list:
    if type(item) == float:
        floats.append(item)
    elif type(item) == str:
        strings.append(item)
    elif type(item) == int:
        if item < 10:
            ints["satuan"].append(item)
        elif item < 100:
            ints["puluhan"].append(item)
        elif item < 1000:
            ints["ratusan"].append(item)

floats = tuple(floats)

print("Floats:", floats)
print("Strings:", strings)
print("Ints:", ints)
