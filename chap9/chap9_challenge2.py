answer = input("Как вас зовут?")

with open("answer.txt", "w") as f:
    f.write(answer)
print(f)
