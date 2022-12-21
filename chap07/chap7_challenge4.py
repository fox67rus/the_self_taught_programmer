num_list = [13, 70, 39, 69, 40, 96, 65, 59, 73, 88]

while True:
    answer = input("Угадайте число или введите Х для выхода: ")
    if answer.lower() == "х":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("Пожалуйста, введите число или Х")
    if answer in num_list:
        print(f"Ваше число {answer} есть в списке")
    else:
        print(f"Число {answer} отсутствует в списке")
