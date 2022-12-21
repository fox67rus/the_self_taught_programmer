rock = []
country = []

def collect_song():
    song = "Укажите песню: "
    ask = "Введите [Р]ок или [К]антри. Введите Х для выхода: "

    while True:
        genre = input(ask)
        if genre.lower() == "х":
            break

        if genre.lower() == "р":
            rk = input(song)
            rock.append(rk)

        elif genre.lower() == "к":
            cy = input(song)
            country.append(cy)
        else:
            print("Нужно ввести р, к или Х")
    print(rock)
    print(country)

collect_song()
