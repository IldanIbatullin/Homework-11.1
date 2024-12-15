def filter_by_currency(transactions, currency):
    """
    Генератор, который фильтрует транзакции по заданной валюте.

    :param transactions: Список транзакций, каждая из которых представлена словарем.
    :param currency: Код валюты для фильтрации (например, 'USD', 'RUB').
    :yield: Транзакции, соответствующие указанной валюте.
    """
    for transaction in transactions:
        if transaction["operationAmount"]['currency']['code'] == currency:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генератор, который возвращает описания транзакций.

    :param transactions: Список транзакций, каждая из которых представлена словарем.
    :yield: Описание каждой транзакции.
    """
    for transaction in transactions:
         description = transaction["description"]
         yield description


def card_number_generator(start, stop):
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: Начальное значение (от 1 до 9999999999999999).
    :param stop: Конечное значение (от 1 до 9999999999999999).
    :yield: Номера банковских карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, stop + 1):
        # Используем zfill для добавления ведущих нулей
        card_number = str(number).zfill(16)
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number