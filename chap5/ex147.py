lists = []
rap = ["Баста",
       "Кравц",
       "Злой дух",
       "25-17"]
rock = ["Наутилус Помпилиус",
        "Кино",
        "Ария"]
djs = ["Paul Oakenfold",
       "Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)
print(lists[1])

# добавляем элемент в список
rap = lists[0]
rap.append("Наше дело")
print(rap)
print(lists)


