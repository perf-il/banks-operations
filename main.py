import utils as ut


# цикл вывода n последних операций (по-умолчанию 5)
def main():
    for operation in ut.get_n_operation():
        date_operation = ut.get_date(operation['date'])  # переменная с датой совершения операции
        descr_operation = operation.get('description')  # переменная с названием операции
        from_operation = operation.get('from')  # переменная с указанием откуда совершен перевод
        to_operation = operation.get('to')  # переменная с указанием куда совершен перевод
        amount = operation['operationAmount']['amount']  # переменная с суммой операции
        currency = operation['operationAmount']['currency']['name']  # переменная с названием валюты

        # блок вывода отформатированных значений по каждой операции
        print(date_operation, descr_operation)
        if from_operation is not None:
            if ut.is_bill(from_operation):
                print(f'{ut.get_secret_bill(from_operation)} -> {ut.get_secret_bill(to_operation)}')
            else:
                print(f'{ut.get_secret_card(from_operation)} -> {ut.get_secret_bill(to_operation)}')
        else:
            print(f'{ut.get_secret_bill(to_operation)}')
        print(amount, currency, '\n')
    return


if __name__ == '__main__':
    main()
