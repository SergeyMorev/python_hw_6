import os
import pickle
import json
import yaml

"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""

MONEY = {'RUR': 10.0}   # Можно расширить на другие валюты.
HISTORY = {}

file_formats = ['bin', 'json', 'yaml']
STORAGE_DIR = '.'
# STORAGE_DIR = os.path.join('.', 'storage')
balance_file = {ff: os.path.join(STORAGE_DIR, f'balance.{ff}') for ff in file_formats}
shopping_file = {ff: os.path.join(STORAGE_DIR, f'shopping.{ff}') for ff in file_formats}


def input_float(message):
    while True:
        try:
            res = float(input(message))
            return res
        except ValueError:
            print('Это не число')


def save(file_name, data, file_format):
    """
    Сохраняет данные в один из трех возможных форматов: 'bin', 'json', 'yaml'.
    :param file_name: путь к файлу в относительном или абсолютном виде.
    :param data: любые данные для записи в файл.
    :param file_format: название формата из списка форматов file_formats
    :return: False если формат сохранения не поддерживатеся, True если известный формат
    """
    file_mode = "wb" if file_format == 'bin' else "wt"

    if file_format in file_formats:
        with open(file_name, file_mode) as f:
            if file_format == 'bin':
                pickle.dump(data, f)
            elif file_format == 'json':
                json.dump(data, f)
            elif file_format == 'yaml':
                yaml.dump(data, f)
        return True
    else:
        return False


def load(file_name, file_format):
    file_mode = "rb" if file_format == 'bin' else "rt"

    data = {}
    if os.path.exists(file_name):
        with open(file_name, file_mode) as f:
            if file_format == 'bin':
                data = pickle.load(f)
            elif file_format == 'json':
                data = json.load(f)
            elif file_format == 'yaml':
                data = yaml.load(f)
            return data
    else:
        return data


# -----------------------------------------------
def save_balance(balance, file_format='json'):
    save(balance_file[file_format], balance, file_format)


def load_balance(file_format='json'):
    return load(balance_file[file_format], file_format)


def save_shopping(shopping_list, file_format='json'):
    save(shopping_file[file_format], shopping_list, file_format)


def load_shopping(file_format='json'):
    return load(shopping_file[file_format], file_format)


def store_balance():
    # Сохраняем balance во всех форматах
    for ff in file_formats:
        save_balance(MONEY, ff)


def store_shopping():
    # Сохраняем shopping_list во всех форматах
    for ff in file_formats:
        save_shopping(HISTORY, ff)
# -----------------------------------------------


def get_curr_balance(currency='RUR'):
    global MONEY
    return MONEY[currency]


def change_curr_balance(delta, currency='RUR'):
    global MONEY
    err_msg = None
    if currency in MONEY:
        MONEY[currency] += delta
    else:
        err_msg = 'Нет такой валюты'


def add_money(money, currency='RUR'):
    """
    :param money: сумма, которая будет добавлена к текущему счету
    :param currency: в какой валюте
    :return: сообщение об ошибке
    """
    err_msg = None
    if money < 0:
        err_msg = 'Счет можно только пополнить, снять деньги нельзя.'
    else:
        change_curr_balance(money, currency)
        store_balance()

    return err_msg


def spend_money(amount, currency='RUR'):
    """
    :param amount: количество денег, которое хотим потратить
    :param currency: в какой валюте
    :return: сообщение об ошибке (пустая строка если все ок).
    """
    if amount <= get_curr_balance(currency):
        return change_curr_balance(-amount, currency)
    else:
        return 'На счете не достаточно денег.'


def menu_add_money():
    print('\t', '-' * 20)
    print('\tПополнение счета')
    print(f"\tНа вашем счете {get_curr_balance()} руб")
    delta = input_float('\tВведите сумму, на которую вы хотите пополнить счет: ')
    err_msg = add_money(delta)
    if err_msg is None:
        print(f'Текущий баланс {get_curr_balance()} руб')
    else:
        print(err_msg)


def add_shopping(name, cost):
    global HISTORY

    err_msg = spend_money(cost)
    if err_msg is None:
        HISTORY[name] = cost
        # Сохраняем во всех форматах
        store_shopping()
        store_balance()

    return err_msg


def menu_add_shopping():
    print('\t', '-' * 20)
    print('\tНовая покупка')
    name = input('\tВведите название покупки: ')
    cost = input_float('\tВведите стоимость покупки: ')
    err_msg = add_shopping(name=name, cost=cost)
    if err_msg:
        print(err_msg)


def print_shopping_list():
    global HISTORY
    print('\tИстория покупок')
    if HISTORY:
        for k in HISTORY:
            print(f'\t{k} \t: {HISTORY[k]:.2f}')
    else:
        print('\tНет покупок')


def show_menu():
    print(f'\n{"=" * 20} Текущий счет: {get_curr_balance():.2f}')
    print('1. Пополнение счета')
    print('2. Новая покупка')
    print('3. История покупок')
    print('4. Выход')
    item = input('Выберите пункт меню: ')
    return item


def start_account():
    global MONEY, HISTORY

    # Load from json files.
    new_balance = load_balance()
    new_shopping_list = load_shopping()

    if new_balance:
        MONEY = new_balance

    if new_shopping_list:
        HISTORY = new_shopping_list

    while True:
        choice = show_menu()
        if choice == '1':
            menu_add_money()
        elif choice == '2':
            menu_add_shopping()
        elif choice == '3':
            print_shopping_list()
        elif choice == '4':
            break   # exit
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    start_account()



