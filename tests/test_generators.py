import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Пример транзакций для тестов
@pytest.fixture
def sample_transactions():
    """Фикстура для предоставления тестовых данных о транзакциях."""
    return [
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

@pytest.fixture
def empty_transactions():
    """Фикстура для предоставления пустого списка транзакций."""
    return []

# Тестирование функции filter_by_currency
def test_filter_by_currency(sample_transactions, empty_transactions):
    # Проверка фильтрации по валюте USD
    usd_transactions = list(filter_by_currency(sample_transactions, 'USD'))
    assert len(usd_transactions) == 2
    assert usd_transactions[0]["id"] == 1
    assert usd_transactions[1]["id"] == 2

    # Проверка фильтрации по валюте RUB
    rub_transactions = list(filter_by_currency(sample_transactions, 'RUB'))
    assert len(rub_transactions) == 1
    assert rub_transactions[0]["id"] == 3

    # Проверка фильтрации по валюте, которой нет в списке
    empty_transactions_result = list(filter_by_currency(sample_transactions, 'EUR'))
    assert len(empty_transactions_result) == 0

    # Проверка на пустом списке транзакций с использованием фикстуры
    filtered_empty = list(filter_by_currency(empty_transactions, 'USD'))
    assert len(filtered_empty) == 0


# Тестирование функции transaction_descriptions
def test_transaction_descriptions(sample_transactions, empty_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))

    # Проверяем количество описаний
    assert len(descriptions) == len(sample_transactions)

    # Проверяем корректность описаний
    assert descriptions[0] == sample_transactions[0]["description"]
    assert descriptions[1] == sample_transactions[1]["description"]

    # Проверка на пустом списке транзакций с использованием фикстуры
    descriptions_empty = list(transaction_descriptions(empty_transactions))
    assert len(descriptions_empty) == 0


# Тестирование генератора card_number_generator
def test_card_number_generator():
    # Генерация номеров карт от 1 до 5
    generated_cards = list(card_number_generator(1, 5))

    # Проверяем количество сгенерированных номеров карт
    assert len(generated_cards) == 5

    # Проверяем форматирование номеров карт
    expected_format = [
        '0000 0000 0000 0001',
        '0000 0000 0000 0002',
        '0000 0000 0000 0003',
        '0000 0000 0000 0004',
        '0000 0000 0000 0005'
    ]

    assert generated_cards == expected_format

    # Проверка крайних значений диапазона (например, от 9999999999999998 до 9999999999999999)
    edge_cases = list(card_number_generator(9999999999999998, 9999999999999999))

    assert len(edge_cases) == 2
    assert edge_cases[0] == '9999 9999 9999 9998'
    assert edge_cases[1] == '9999 9999 9999 9999'
