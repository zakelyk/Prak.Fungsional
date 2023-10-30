import random

def genRand():
    x = random.randint(1, 3)
    if x == 1:
        return random.randint(1, 1000)
    elif x == 2:
        return random.uniform(0.1, 1000.0)
    else :
        return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

random_list = [genRand() for x in range(10)] #seperti pada kegiatan 1 modul 1
print(random_list)
# Filter untuk memisahkan nilai float, int, dan string
float_data = list(filter(lambda x: isinstance(x, float), random_list))
int_data = list(filter(lambda x: isinstance(x, int), random_list))
string_data = list(filter(lambda x: isinstance(x, str), random_list))

print(type(float_data))
print(type(int_data))
print(type(string_data))
# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def numberGroup(value):
    if value < 10:
        return {"satuan": value, "puluhan": 0, "ratusan": 0}
    elif value < 100:
        return {"satuan": 0, "puluhan": value, "ratusan": 0}
    else:
        return {"satuan": 0, "puluhan": 0, "ratusan": value}
    
mapInt = list(map(numberGroup, int_data))

# Output

print("Data Float :"+str(float_data))
# print("Data Int :"+str(int_data))
print("Data Int :")
print(mapInt)
print("Data String :"+str(string_data))


# Data Float : (3.1, 2.7, 5.5)
# Data Int :
# {'ratusan': 1, 'puluhan': 0, 'satuan': 5}
# {'ratusan': 7, 'puluhan': 3, 'satuan': 7}
# {'ratusan': 4, 'puluhan': 1, 'satuan': 2}
# Data String : ['Hello', 'Python', 'world', 'AI']