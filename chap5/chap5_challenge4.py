human_data = {"рост": 170,
              "вес": 80,
              "возраст": 30,
              "цвет глаз": "зеленый"
              }

input_data = input("Введите параметр (рост, вес, возраст, цвет глаз): ")
if input_data in human_data:
    data = human_data[input_data]
    print(data)
else:
    print("Не найдено.")

