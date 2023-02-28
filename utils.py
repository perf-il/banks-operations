import json
from _datetime import datetime


def load_all_operation():
    with open('operation.json', encoding='utf-8') as f:
        all_operation = json.loads(f.read())
    return all_operation


def load_id_operation(idn):
    all_operation = load_all_operation()
    for operate in all_operation:
        if operate['id'] == idn:
            return operate
    return f'Операция с номером {idn} не найдена'


def get_n_operation(n=5):
    all_operation = load_all_operation()
    n_operation = [operate for operate in all_operation if operate['state'] == 'EXECUTED']
    n_operation.sort(key=lambda dictionary: dictionary['date'], reverse=True)
    return n_operation[:n]


def get_date(date):
    new_date = datetime.strptime(date[:10], '%Y-%m-%d')
    return new_date.strftime('%d.%m.%Y')


def get_secret_card(name_card: object) -> object:
    name = name_card[:-16]
    number = name_card[-16:]
    return f'{name}{number[:6]}******{number[-4:]}'


def get_secret_bill(name_bill):
    return f'{name_bill[:4]} **{name_bill[-4:]}'


def is_bill(name_bill: object) -> object:
    return name_bill[:4] == 'Счет'


