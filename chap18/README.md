# Глава 18. Системы управления пакетами

> Каждый программист - это автор.

<p style="text-align: right;"><i>Серкан Лейлек</i></p>


### Пакеты
Пакет включает файлы программы и метаданные (название ПО, номер версии, зависимости).
СУП управляет загрузкой всех зависимостей пакета.

### Pip
[Инструкция по установке pip](https://pythonworld.ru/osnovy/pip.html)

Команда для установки пакета: *pip install имя_пакета*. Пакет устанавливается в *site-packages* в каталоге Python.
[Список всех доступных пакетов](https://pypi.org/)

Для установки определенной версии необходимо указать номер версии с помощью двух знаков равенства (==)

```bash
$sudo pip install Flask==2.0.1

>> Пароль:
>> Successfully installed flask-2.0.1
```
В Windows запускать cmd от имени администратора.

После установки пакета, можно импортировать его в свою программу. [Пример](ex283.py)
[Подробное описание Flask](https://flask.palletsprojects.com/en/2.2.x/) 

*pip freeze* - посмотреть перечень установленных пакетов
*pip uninstall имя_пакета* - удалить пакет

### Виртуальные окружения
Позволяют устанавливать раздельно разные пакеты и их версии для разных проектов.

- **$PYTHONPATH** - Python ищет модули в списке папок, которые указаны в перенемой окружения
- **Apt-get** - менеджер пакетов Ubuntu
- **Pip** - менеджер пакетов для Python
- **PyPI** - веб сайт, который содержит пакеты Python
- **Site-packages** папка в $PYTHONPATH. Это папке, куда pip устанавливает пакеты, если не использовать виртуальные окружения


