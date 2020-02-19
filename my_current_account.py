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

MONEY = 10.0
HISTORY = {}


def input_float(message):
    while True:
        try:
            res = float(input(message))
            return res
        except ValueError:
            print('Это не число')


def save_balance():
    pass


def load_balance():
    pass


def save_shopping():
    pass


def load_shopping():
    pass


def get_curr_balance():
    return MONEY


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
        MONEY += money
        result = f'Текущий баланс {get_curr_money()} руб'
    return result


def menu_add_money():
    global MONEY
    print('\t', '-' * 20)
    print('\tПополнение счета')
    print(f"\tНа вашем счете {get_curr_money()} руб")
    delta = input_float('\tВведите сумму, на которую вы хотите пополнить счет: ')
    print(add_money(delta))


def menu_add_shopping():
    global MONEY, HISTORY
    print('\t', '-' * 20)
    print('\tНовая покупка')
    k = input('\tВведите название покупки: ')
    v = input_float('\tВведите стоимость покупки: ')
    if v <= MONEY:
        MONEY -= v
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
    print(f'\n{"-" * 20} текущий счет: {MONEY:.2f}')
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



