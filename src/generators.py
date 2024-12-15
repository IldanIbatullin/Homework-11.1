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
