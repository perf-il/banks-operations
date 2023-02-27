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


def get_secret_card(name_card):
    name = name_card[:-16]
    number = name_card[-16:]
    return f'{name}{number[:6]}******{number[-4:]}'


def get_secret_bill(name_bill):
    return f'{name_bill[:4]} **{name_bill[-4:]}'


'''

for i in get_n_operation():
    print(get_date(i['date']), i['description'])
    print(get_secret_card(i.get('from')), get_secret_bill(i.get('to'))) if i.get('from') is not None else print(get_secret_bill(i.get('to')))
    print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'], '\n')

    
'''
