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