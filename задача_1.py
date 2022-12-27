## Задание 1
import re
## - не знаю в чем ошибка в первом задании - абсолютно ничего не знаю про регулярыне выражения ((( но это пока что
def to_camel_case(text):
    return re.split('_|-', text)[1] + ''.join(word.title() for word in re.split('_|-', text)[1::])


## Задание 2
class SingletonMeta(type):
    _instances = {}

    def __str__(cls, *args, **kwargs):
        if cls in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]



## Задание 3
count_bits = lambda n: bin(n).count('1')

## задание 4
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))

## задание 5
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"
