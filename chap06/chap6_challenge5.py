fox = ["Рыжая",
         "лиса",
         "перерпрыгнула",
         "через",
         "низкий",
         "забор",
         "."]

fox = " ".join(fox)

print(fox.replace(" .", "."))
print(fox[:-2] + ".")