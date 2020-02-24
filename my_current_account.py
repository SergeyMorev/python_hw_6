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

MONEY = {'RUR': 10.0}
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
    file_mode = "wb" if file_format == 'bin' else "wt"

    if file_format in file_formats:
        with open(file_name, file_mode) as f:
            if file_format == 'bin':
                pickle.dump(data, f)
            elif file_format == 'json':
                json.dump(data, f)
            elif file_format == 'yaml':
                yaml.dump(data, f)


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


# --- bin ---------------------------------------
def save_balance(balance, file_format='json'):
    save(balance_file[file_format], balance, file_format)


def load_balance(file_format='json'):
    return load(balance_file[file_format], file_format)


def save_shopping(shopping_list, file_format='json'):
    save(shopping_file[file_format], shopping_list, file_format)


def load_shopping(file_format='json'):
    return load(shopping_file[file_format], file_format)
# -----------------------------------------------


def get_curr_balance():
    return MONEY['RUR']


def add_money(money):
    """
    :param money: сумма, которая будет добавлена к текущему счету
    :return: сообщение об успешности выполнения операции
    """
    global MONEY
    result = ''
    if money < 0:
        result = 'Счет можно только пополнить, снять деньги нельзя.'
    else:
        MONEY['RUR'] += money

        # Сохраняем во всех форматах
        for ff in file_formats:
            save_balance(MONEY, ff)

        result = f'Текущий баланс {get_curr_balance()} руб'

    return result


def menu_add_money():
    print('\t', '-' * 20)
    print('\tПополнение счета')
    print(f"\tНа вашем счете {get_curr_balance()} руб")
    delta = input_float('\tВведите сумму, на которую вы хотите пополнить счет: ')
    print(add_money(delta))


def menu_add_shopping():
    global MONEY, HISTORY
    print('\t', '-' * 20)
    print('\tНовая покупка')
    k = input('\tВведите название покупки: ')
    v = input_float('\tВведите стоимость покупки: ')
    if v <= MONEY['RUR']:
        MONEY['RUR'] -= v
        HISTORY[k] = v
    else:
        print('На счете не достаточно денег.')


def print_shopping_list():
    global HISTORY
    print('\tИстория покупок')
    if HISTORY:
        for k in HISTORY:
            print(f'\t{k} \t: {HISTORY[k]:.2f}')
    else:
        print('\tНет покупок')


def show_menu():
    print(f'\n{"-" * 20} текущий счет: {get_curr_balance():.2f}')
    print('1. Пополнение счета')
    print('2. Новая покупка')
    print('3. История покупок')
    print('4. Выход')
    item = input('Выберите пункт меню: ')
    return item


def start_account():
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



