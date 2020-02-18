import os
import file_manager as fm


def clear_folder(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

# --- 6 ---
def test_fm_file_list():
    file_list = ['file_1.txt', 'file_2.txt', 'index.html', 'some_file.dat']

    # ========= Подготовим тестовую папку с файлами: ======
    curr_dir = os.getcwd()
    test_folder = 'test_temp_folder'
    test_path = os.path.join(curr_dir, test_folder)

    # Удаляем папку если уже существует
    if os.path.exists(test_path):
        if os.path.isdir(test_path):
            clear_folder(test_path)
            os.rmdir(test_path)
        else:
            assert "Wrong name for test folder"

    # Создаем папку заново
    os.mkdir(test_path)

    # Создаем список файлов
    for file in file_list:
        with open(os.path.join(test_path, file), 'tw') as f:
            pass
    # =====================================================

    files = fm.get_file_list(test_path)
    for file in file_list:
        assert file in files, f'file:"{file}" not in list:"{files}"'


# --- 7 ---
def test_fm_os_info():
    info = fm.get_os_info()
    assert len(info) == 4
    assert [k in info for k in ('platform-name', 'platform-release', 'platform-version', 'architecture')]
    assert [v is not None for k, v in info.items()]


# --- 8 ---
def test_fm_author():
    assert fm.get_author_info() == 'Морев С.А.'


