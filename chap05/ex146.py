rhymes = {"1": "смех",
          "2": "синий",
          "3": "я",
          "4": "этаж",
          "5": "этаж"
}

n = input("Введите число: ")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Не найдено.")