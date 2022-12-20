import csv

with open("st.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["один",
                "два",
                "три"])
    w.writerow(["четыре",
                "пять",
                "шесть"])