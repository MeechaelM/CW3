def sorted_operations_status(data):
    """Сортировка операций по статусу EXECUTED"""
    list_data = []
    for transaction in data:
        if transaction and transaction.get('state') == "EXECUTED":
            list_data.append(transaction)
    return list_data

def sorted_operations_date(data):
    """Сортировка последних 5 операций по дате"""
    return sorted(data, key= lambda x: x['date'], reverse=True)[:5]

def format_date(date):
    """форматирование даты"""
    format_date = date[0:10].split(sep='-')
    return f'{format_date[2]}.{format_date[1]}.{format_date[0]}'

def mask_card_number(card_number: str):
    """маскировка номера карты в формате XXXX XX** **** XXXX"""
    if card_number.isdigit() and len(card_number) == 16:
        return f'{card_number[:4]} {card_number[4: 6]}** **** {card_number[-4:]}'
    else:
        raise ValueError('Номер карты неверный')

def mask_account_number(account_number: str):
    """маскировка номера счета в формате **XXXX"""
    if account_number.isdigit() and len(account_number) == 20:
        return f'**{account_number[-4:]}'
    else:
        raise ValueError('номер неверный')

def mask_in_message(num):
    """Скрывает номера в сообщении"""
    if num is None:
        return ""
    num = num.split()
    if num[0] == "Счет":
        num_mask = mask_account_number(num[-1])
    else:
        num_mask = mask_card_number(num[-1])
    return ' '.join(num[:-1]) + ' ' + num_mask

def message(meaning):
    """Формат сообщения на вывод"""
    date = format_date(meaning.get('date'))
    description = meaning.get('description')
    from_ = mask_in_message(meaning.get('from_'))
    from_ = f'{from_} -> ' if from_ else ''
    to = mask_in_message(meaning.get('to'))
    amount = meaning.get('operationAmount').get('amount')
    currency = meaning.get('operationAmount').get('currency').get('name')
    return f'{date} {description}\n{from_}{to}\n{amount}{currency}'