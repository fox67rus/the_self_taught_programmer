import csv

cinema = [["Звездные войны", "Терминатор", "Искуственный интеллект"],
          ["Дурак", "Матильда", "Левиафан"],
          ["Люди в черном", "Я - робот", "Эволюция"]]

with open("cinema.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    for movie in cinema:
        w.writerow(movie)
