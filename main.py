import utils as ut


operations = ut.get_n_operation()

for operation in operations:
    date_operation = ut.get_date(operation['date'])
    descr_operation = operation.get('description')
    from_operation = operation.get('from')
    to_operation = operation.get('to')
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    print(date_operation, descr_operation)
