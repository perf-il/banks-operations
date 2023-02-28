import utils as ut


for operation in ut.get_n_operation():
    date_operation = ut.get_date(operation['date'])
    descr_operation = operation.get('description')
    from_operation = operation.get('from')
    to_operation = operation.get('to')
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    print(date_operation, descr_operation)
    if from_operation is not None:
        if ut.is_bill(from_operation):
            print(f'{ut.get_secret_bill(from_operation)} -> {ut.get_secret_bill(to_operation)}')
        else:
            print(f'{ut.get_secret_card(from_operation)} -> {ut.get_secret_bill(to_operation)}')
    else:
        print(f'{ut.get_secret_bill(to_operation)}')
    print(amount, currency, '\n')

