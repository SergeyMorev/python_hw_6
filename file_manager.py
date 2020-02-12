import os
import sys

from my_current_account import start_account
from my_quiz_game import start_quiz_game


# После запуска программы пользователь видит меню, состоящее из следующих пунктов:
#
#  1- создать папку;
#  2- удалить (файл/папку);
#  3- копировать (файл/папку);
#  4- просмотр содержимого рабочей директории;
#  5- посмотреть только папки;
#  6- посмотреть только файлы;
#  7- просмотр информации об операционной системе;
#  8- создатель программы;
#  9- играть в викторину;
# 10- мой банковский счет;
# 11- смена рабочей директории (*необязательный пункт);
# 12- выход.
#
# После выполнения какого либо из пунктов снова возвращаемся в меню, пока пользователь не выберет выход
#


# 1
def my_create():
    print('--- Создание папки ---------')
    try:
        folder_name = input('\tВведите имя папки:')
        os.mkdir(folder_name)
    except Exception as error:
        print(error)


# 2
def my_delete():
    print('--- Удаление папки ---------')
    try:
        folder_name = input('\tВведите имя папки:')
        os.rmdir(folder_name)
    except Exception as error:
        print(error)


# 3
def my_copy():
    pass


# 4
def my_print_list():
    print('\n--- Список файлов и папок ------')
    print(f'\n{os.getcwd()}')
    file_list = os.listdir()
    for f in file_list:
        print(f'\t{f}')
    pass


# 5
def my_print_folders():
    print('\n--- Список папок -----------')
    my_path = os.getcwd()
    print(my_path)
    for i in os.listdir('.'):
        if os.path.isdir(os.path.join(my_path, i)):
            print(f'\t./{i}')


# 6
def my_print_files():
    print('--- Список файлов ----------')
    my_path = os.getcwd()
    print(my_path)
    for i in os.listdir('.'):
        if os.path.isfile(os.path.join(my_path, i)):
            print(f'\t./{i}')

    # for current_dir, dirs, files in os.walk("."):
    #     print(current_dir, dirs, files)


# 7
def my_os_info():
    print('--- Информация об OS -------')
    info = os.uname()
    print(f'\tOS: {info.sysname} {info.release}')


# 8
def my_print_author():
    print('--- Информация об авторе ---')
    print('\tМорев С.А.')
    pass


# 9
def my_victory_game():
    print('--- Игра "Викторина" -------')
    start_quiz_game()


# 10
def my_bill():
    print('--- Личный счет ------------')
    start_account()


# 11
def my_change_dir():
    print('--- Перейти в папку --------')
    try:
        my_path = os.getcwd()
        print(my_path)
        folder_name = input('\tВведите имя папки:')
        if os.path.isdir(folder_name):
            os.chdir(folder_name)
        elif os.path.isdir(my_path + folder_name):
            os.chdir(my_path + folder_name)
        else:
            print('Папка не найдена')

        print(os.getcwd())

    except Exception as error:
        print(error)
    pass


# 12  Exit !
def my_exit():
    print('--- Выход ---')


def show_menu():
    print(f'\n{os.getcwd()}')

    print(' 1- Создать папку')
    print(' 2- Удалить (файл/папку)')
    print(' 3- Копировать (файл/папку)')
    print(' 4- Просмотр содержимого рабочей директории')
    print(' 5- Посмотреть только папки')
    print(' 6- Посмотреть только файлы')
    print(' 7- Просмотр информации об операционной системе')
    print(' 8- Создатель программы')
    print(' 9- Играть в викторину')
    print('10- Мой банковский счет')
    print('11- Смена рабочей директории')
    print('12- Выход')
    item = -1
    try:
        item = int(input('Выберите пункт меню: '))
    except ValueError:
        pass
    except Exception as err:
        print(err)

    return item


def main_menu():
    while True:
        choice = show_menu()
        if choice == 1:
            my_create()
        elif choice == 2:
            my_delete()
        elif choice == 3:
            my_copy()
        elif choice == 4:
            my_print_list()
        elif choice == 5:
            my_print_folders()
        elif choice == 6:
            my_print_files()
        elif choice == 7:
            my_os_info()
        elif choice == 8:
            my_print_author()
        elif choice == 9:
            my_victory_game()
        elif choice == 10:
            my_bill()
        elif choice == 11:
            my_change_dir()
        elif choice == 12:
            my_exit()
            break


if __name__ == '__main__':
    main_menu()