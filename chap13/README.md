# Глава 13. Четыре столпа ООП

> Хороший дизайн приносит пользу быстрее, чем увеличивает расходы.

<p style="text-align: right;"><i>Томас Гейл</i></p>

- инкапсуляция
- абстракция
- полиморфизм
- наследование

### Инкапсуляция
1. Переменные (хранят состояние) и методы (для изменения состояния или выполнения вычислений)
группируются в одно целое - объект.  [Пример](../chap12/ex244.py)
2. Сокрытие внутренних данных класса для предотвращения прямого доступа из вне (кодом вне класса) [Пример](ex247.py)

**Закрытые переменные** и **закрытые методы** - переменные и методы, к которым могут обращаться объекты
в коде, реализующие различные методы, но клиент не может. В Python нет закрытых переменных, 
вместо этого используется конвенции (соглашения) имен. К именам тех переменных, 
к которым вызывающий не должен получить доступ, необходимо добавить нижнее подчеркивание.
[Пример](ex248.py)

### Абстракция
В ООП абстракция используется, когда объекты модедлируются с использованием классов, 
а ненужные подробности опускаются, используются только существенные параметры.

### Полиморфизм

Способность представить один и тот же интерфейс (функции или методы) для разных базовых форм (типов данных).
```python
print("Привет, мир!")
print(200)
print(200.1)
```
### Наследование
Класс (дочерний) наследует свойства и методы от другого класса (родителя). 
[Пример](ex253.py). 

Переопределение метода - способность дочернего класса изменять метод родителя. 
[Пример](ex253.py). 

### Композиция
Композиция создает отношение "имеет", сохраняя объект в другом объекте как переменную.
[Пример](ex257.py). 