## Задача 2.1

list_ = [1, 0, 2, 5, 6, 0, 3, 9, 8, 0, 7, 4, 0]


def func(list_):
    """
    изменяет список перенося нули в конец списка
    :param list_: список содержащий  нули
    :return: список с перенесенными нулями в конец списка
    """
    for i in range(len(list_)):
        if list_[i] == 0:
            list_.append(list_[i])
            del (list_[i])
        else:
            continue
    return list_


## задача 2.2

stage = int(input('Введитеномер пирамиды для расчета сумы элементов этого ряда: '))


def get_coll_elements(stage):
    """
    Возвращает колличество элементов в
    пирамиде с заданным колличесвтом этажей
    :param stage: колличество этажей
    :return: колличество элементов пирамиды
    """
    coll_elements = 0
    for i in range(stage):
        coll_elements += i + 1
    return coll_elements


coll_elements = (get_coll_elements(
    stage) * 2)  # колличество элементво умножаем на 2 так как учитываются только нечетные элементы


def create_not_even_list(coll_elements):
    """
    Создает список нечетных элементов
    :param coll_elements: колличество элементов пирамиды умноженное на 2
    :return: список элементов пирамиды с нечетным значением
    """
    list_not_even = []
    for i in range(coll_elements):
        if i % 2 == 0:
            continue
        list_not_even.append(i)
    return list_not_even


list_not_even = create_not_even_list(coll_elements)


def create_pyramid_not_even(list_not_even):
    """
    Создает словарь на подобии пирамиды с нечетными
     значениями где ключ это номер этажа а значение
     это список элементво на этом этаже
    :param list_not_even: список элементов пирамиды с нечетным значением
    :return: словарь имитирующий поведение пирамиды нечетных значений
    """
    pyramid_not_even_number = {}
    list_not_even_ = list_not_even
    for i in range(len(list_not_even)):
        if list_not_even_ != []:
            pyramid_not_even_number[i + 1] = list_not_even_[:i + 1]
            list_not_even_ = list_not_even_[i + 1:]
    return pyramid_not_even_number


pyramid = create_pyramid_not_even(list_not_even)


def summ_elements_stage_pyramide_not_even_number(pyramid, stage):
    """
    суммирует элементы этажа пирамиды
    :param pyramid: словарь - пирамида
    :param stage: этаж пирамиды
    :return: сумма элементов этажа
    """
    list_elements = sum(pyramid[stage])
    return list_elements


if __name__ == "__main__":
    print(f"Задача №1. - {func(list_)}")
    print(f"Задача №2. - {summ_elements_stage_pyramide_not_even_number(pyramid, stage)}")
