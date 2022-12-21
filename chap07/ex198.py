tv = ["Во все тяжкие",
      "Секретные материалы",
      "Фарго"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)

# специальный синтаксис
tv2 = ["Во все тяжкие",
      "Секретные материалы",
      "Фарго"]
for i, show in enumerate(tv2): # позволяет ввести переменную i и отслеживать текущий индекс
    new = tv2[i]
    new = new.upper()
    tv2[i] = new

print(tv2)
