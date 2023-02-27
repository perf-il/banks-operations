import json


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


#for i in get_n_operation():
#    print(i['date'], i['description'])
#    print(i.get('from'), i.get('to'))
#   print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'], '\n')
