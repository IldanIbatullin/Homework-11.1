import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Пример транзакций для тестов
transactions = [
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 2,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 3,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    }
]

# Тестирование функции filter_by_currency
def test_filter_by_currency():
    # Проверка фильтрации по валюте USD
    usd_transactions = list(filter_by_currency(transactions, 'USD'))
    assert len(usd_transactions) == 2
    assert usd_transactions[0]["id"] == 1
    assert usd_transactions[1]["id"] == 2

    # Проверка фильтрации по валюте RUB
    rub_transactions = list(filter_by_currency(transactions, 'RUB'))
    assert len(rub_transactions) == 1
    assert rub_transactions[0]["id"] == 3

    # Проверка фильтрации по валюте, которой нет в списке
    empty_transactions = list(filter_by_currency(transactions, 'EUR'))
    assert len(empty_transactions) == 0

    # Проверка на пустом списке транзакций
    empty_list = []
    filtered_empty = list(filter_by_currency(empty_list, 'USD'))
    assert len(filtered_empty) == 0
