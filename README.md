# Homework-11.1

Модуль для работы с транзакциями и генерацией номеров карт.

## Описание

Этот проект включает в себя модуль `generators`, который предоставляет функции для фильтрации транзакций по валюте, извлечения описаний транзакций и генерации номеров банковских карт. Модуль написан с использованием Python и включает тесты для проверки функциональности.

## Установка

Для установки необходимых зависимостей выполните следующие шаги:

1. Клонируйте репозиторий:

git clone https://github.com/IldanIbatullin/Homework-11.1.git


## Использование

### Импортирование модуля

Импортируйте функции из модуля `generators`:

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
text

### Примеры использования функций

#### 1. Функция `filter_by_currency`

Эта функция фильтрует транзакции по заданной валюте.

**Пример:**

transactions = [
{
"id": 1,
"operationAmount": {
"amount": "1000.00",
"currency": {"code": "USD"}
},
"description": "Перевод"
},
{
"id": 2,
"operationAmount": {
"amount": "2000.00",
"currency": {"code": "EUR"}
},
"description": "Перевод в евро"
}
]
usd_transactions = list(filter_by_currency(transactions, 'USD'))
print(usd_transactions) # Выводит транзакции в USD
text

#### 2. Функция `transaction_descriptions`

Эта функция возвращает описания всех транзакций.

**Пример:**

descriptions = list(transaction_descriptions(transactions))
print(descriptions) # Выводит список описаний транзакций
text

#### 3. Генератор `card_number_generator`

Этот генератор создает номера банковских карт в формате `XXXX XXXX XXXX XXXX`.

**Пример:**

for card_number in card_number_generator(1, 5):
print(card_number)
Выводит:
0000 0000 0000 0001
0000 0000 0000 0002
...
text

## Тестирование

Для запуска тестов используйте следующую команду:

pytest tests/