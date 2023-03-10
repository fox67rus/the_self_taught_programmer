# Глава 15. Практикум. Часть 2

> Пока код не запустился, это всего лишь разговоры.

<p style="text-align: right;"><i>Уорд Каннингем</i></p>

Цель практикума - создание карточной игры "Пьяница". В этой игре каждый игрок берет из колоды по карте -
побеждает тот, у которого карта старше.

Для создания игры понадобится определить классы, представляющие карту, колоду, игрока и саму игру.

#### Класс Card
содержит две переменные класса:
- suits - список строковых значений всех мастей 
- value - список строковых значений всех номиналов карт (в начале 2 элемента со значением None, чтобы индексы карт совпадали с их значением)

Объекты Card имеют две целочисленные переменные экземпляра - suit и value, определяющие вид карты.
Например, для создания двойки червей нужно присвоить им значение 1 и 2 соответственно.

Магические методы __lt__ и __gt__ позволяют сравнивать два объекта Card сначала по значению, а если они равно, то по масти.
Масти в списке располагаются в порядке возрастания.
```python
card1 = Card(10, 2)
card2 = Card(11, 3)
print(card1 < card2) # True
print(card1 > card2) # False
```
Магический метод __repr__ позволяет вывести карту, представляющую объект в удобном виде.
```python
card1 = Card(10, 2)
print(card1) # 10 бубей
```

#### Класс Deck (колода)
Используется для создания новой колоды и вывода каждой карты из нее.
Содержит два цикла for в __init__ для генерации колодцы из 52 карт. После создания колоды, карты случайным образом перемешиваются.

Метод rm_card - возвращает карту и изымает её из колоды или возвращает None, если колода пуста.

#### Класс Игрок
Содержит три переменных экземпляра:
- wins - отслеживание количества выигранных раундов
- card - карта, которую в данный момент держит игрок
- name - имя игрока

#### Класс Игра
При создании объекта игры принимаются имена игроков, создается колода
и два объекта игрока.

Метод *play_game* начинает игру и продолжает до тех пор пока в колоде 2 или больше карт или пока игрок принудительно не вышел, нажав Х.
При каждом прохождении цикла вынимаются по карте каждому игроку, карты сравниваются, результат текущего раунда записывается в переменную *wins* и выводится сообщение.
Когда карты в колоде заканчиваются, метод *winner* принимает два объекта игрока и сравнивает количество выигранных раундов и возвращает победившего.


[программа](chap15_challenge.py)

