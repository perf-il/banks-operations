import json
from _datetime import datetime


def load_all_operation():
    """
    функция загрузки всех операций из файла 'operation.json'.
    :return: список словарей из файла
    """
    with open('operation.json', encoding='utf-8') as f:
        all_operation = json.loads(f.read())
    return all_operation


def get_n_operation(n=5):
    """
    функция вывода последних операций, осуществлет сортировку по дате выполнения (от последней к первой)
    :param n: кол-во операций, которое необходимо вывести, по умолчанию равняется 5
    :return: список отсортированных операций от 0 до n
    """
    all_operation = load_all_operation()
    n_operation = [operate for operate in all_operation if operate['state'] == 'EXECUTED']
    n_operation.sort(key=lambda dictionary: dictionary['date'], reverse=True)
    return n_operation[:n]


def get_date(date: str):
    """
    функция для преобразования даты выполнения операуии
    :param date: дата из словаря с операциями
    :return: дата в формате ДД.ММ.ГГГГ
    """
    new_date = datetime.strptime(date[:10], '%Y-%m-%d')
    return new_date.strftime('%d.%m.%Y')


def get_secret_card(name_card: str):
    """
    функция для форматирования отображения номера карты
    :param name_card: строку с названием карты и 16-ти значным номером
    :return: f-строку  в формате 'Имя карты XXXX XX** **** XXXX'
    """
    name = name_card[:-15]
    number = name_card[-16:]
    return f'{name}{number[:3]} {number[4:6]}** **** {number[-4:]}'


def get_secret_bill(name_bill):
    """
    функция для форматирования отображения номера счета
    :param name_bill: строку с номером счета из файла
    :return: f-строку в формате 'Счет **ХХХХ'
    """
    return f'{name_bill[:4]} **{name_bill[-4:]}'


def is_bill(name_bill):
    """
    функция для проверки является ли переданная строка счетом
    :param name_bill: строка с названием счета или карты
    :return: bool
    """
    return name_bill[:4] == 'Счет'


