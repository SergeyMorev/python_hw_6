import os
import platform

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


# --- 4 ---------------------------------------------------
def get_files_and_dirs(path):
    all_list = list()
    try:
        all_list = os.listdir(path)
    except:
        pass

    return all_list


def menu_print_files_and_dirs():
    print('\n--- Список файлов и папок ------')
    curr_path = os.getcwd()
    print(f'\n{curr_path}')
    for f in get_files_and_dirs(curr_path):
        print(f'\t./{f}')


# --- 5 ---------------------------------------------------
def get_dirs(path):
    folders = []
    try:
        for i in os.listdir(path):
            if os.path.isdir(os.path.join(path, i)):
                folders.append(i)
    except:
        pass

    return folders


def menu_print_dirs():
    print('\n--- Список папок -----------')
    curr_path = os.getcwd()
    print(curr_path)
    for f in get_dirs(curr_path):
        print(f'\t./{f}')


# --- 6 ---------------------------------------------------
def get_file_list(path):
    files = []
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path, i)):
            files.append(i)

    return files


def menu_print_files():
    print('--- Список файлов ----------')
    curr_path = os.getcwd()
    print(curr_path)

    for file in get_file_list(curr_path):
        print(f'\t./{file}')


# --- 7 ---------------------------------------------------
def get_os_info():
    """
    Возвращает информацию об операционной системе в виде словаря.
    :return:
    """
    info = dict()
    info['platform-name']    = platform.system()
    info['platform-release'] = platform.release()
    info['platform-version'] = platform.version()
    info['architecture']     = platform.machine()
    return info


def menu_os_info():
    print('--- Информация об OS -------')
    info = get_os_info()
    for name, param in info.items():
        print(f'\t {name} = {param}')


# --- 8 ---------------------------------------------------
def author_info():
    return 'Морев С.А.'


def menu_print_author():
    print('--- Информация об авторе ---')
    print(f'\t{author_info()}')


# --- 9 ---------------------------------------------------
def menu_victory_game():
    print('--- Игра "Викторина" -------')
    start_quiz_game()


# --- 10 --------------------------------------------------
def menu_bill():
    print('--- Личный счет ------------')
    start_account()


# --- 11 --------------------------------------------------
def set_current_dir(dest_path):
    res = ''
    try:
        curr_path = os.getcwd()
        if os.path.isdir(dest_path):
            os.chdir(dest_path)
            res = os.getcwd()
        elif os.path.isdir(curr_path + dest_path):
            os.chdir(curr_path + dest_path)
            res = os.getcwd()
        else:
            res = 'Папка не найдена'
    except Exception as error:
        res = error

    return res


def menu_change_dir():
    print('--- Перейти в папку --------')
    print(os.getcwd())
    folder_name = input('\tВведите имя папки:')
    print(set_current_dir(folder_name))


# --- 12  Exit ! ------------------------------------------
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
            menu_print_files_and_dirs()
        elif choice == 5:
            menu_print_dirs()
        elif choice == 6:
            menu_print_files()
        elif choice == 7:
            menu_os_info()
        elif choice == 8:
            menu_print_author()
        elif choice == 9:
            menu_victory_game()
        elif choice == 10:
            menu_bill()
        elif choice == 11:
            menu_change_dir()
        elif choice == 12:
            my_exit()
            break


if __name__ == '__main__':
    main_menu()