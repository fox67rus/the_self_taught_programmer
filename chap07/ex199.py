tv = ["Во все тяжкие",
      "Секретные материалы",
      "Фарго"]
coms = ["Теория большого взрыва",
        "Друзья",
        "Это - мы"]
all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)
