import random

word_list = ["фольга",
             "дым",
             "шутка",
             "черта",
             "толпа",
             "дядя",
             "тетя",
             "кофе",
             "куст",
             "друг"]


def hangman(word: str):
    """

    :param word: слово, которое должен отгадать игрок
    :return:
    """
    wrong = 0  # количество неправильных предложений игрока
    stages = ["",
              "________     ",
              "|      |     ",
              "|      |     ",
              "|      0     ",
              "|     /|\    ",
              "|     / \    ",
              "|            "
              ]
    rletters = list(word)  # содержит все символы слова и отслеживает, какие символы осталось отгадать
    board = ["_"] * len(word)  # список строк для отслеживания отгаданных слов
    win = False
    print("Добро пожаловать на казнь!")

    while wrong < len(stages) - 1:  # пока количество попыток меньше, чем строк в рисунке висельника
        print("\n")  # декоративный отступ
        msg = "Введите букву: "
        guess = input(msg)
        if guess in rletters:
            cind = rletters.index(guess)  # сохраняем индекс отгаданной буквы
            board[cind] = guess  # отображение отгаданного символа на табло
            rletters[cind] = '$'  # замена для корректного поиска повторяющихся букв в слове
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1  # +1 чтобы верно отобразить количество строк в текущей версии рисунка висельника
        print("\n".join(stages[:e]))

        if "_" not in board:  # отгаданы ли все буквы
            print("Вы выиграли! Было загадано слово: ")
            print(" ".join((board)))
            win = True
            break

    if not win:
        print("\n".join((stages[0:wrong])))
        print("Вы проиграли! Было загадано слово: {}.".format(word))


if __name__ == '__main__':
    rnd = random.randint(0, (len(word_list) - 1))
    hangman(word_list[rnd])
