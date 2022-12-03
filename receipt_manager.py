import os
from pathlib import Path
from os import system, name
import shutil


def clear_console():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def start_process(options):
    # clear_console()
    print(f'Existing number of receipts: {number_of_files}')
    print_options(options)
    chosen_option = int(input(f"Choose one: "))
    choose_option(chosen_option, options)


def print_options(options):
    for option in options:
        print(f"[{option['id']}]-{option['name']}")


def choose_option(id, options):
    clear_console()
    options[id - 1]['function']()


def read_receipt():
    clear_console()
    receipt = input('Enter receipt: ')
    find_and_read(receipt, main_path)
    start_process(actions)


def create_receipt():
    new_receipt = input('Enter receipt name: ') + '.txt'
    entered_type = input('Enter type of food: ')
    entered_receipt = input('Write the receipt: ')
    new_path = Path(main_path / entered_type / new_receipt)
    check_and_create_category(entered_type)
    new_path.write_text(entered_receipt)
    start_process(actions)


def create_category():
    entered_type = input('Enter type of food: ')
    check_and_create_category(entered_type)
    start_process(actions)


def check_and_create_category(category):
    new_path = Path(main_path / category)
    os.makedirs(Path(new_path), exist_ok=True)


def delete_receipt():
    entered_receipt = input('Enter the receipt: ').lower()
    find_and_delete(entered_receipt, main_path)
    start_process(actions)


def find_and_read(name, path):
    for root, dirs, files in os.walk(path):
        print(root, dirs, files)
        if name in files:
            print(Path(os.path.join(root, name)).read_text())


def find_and_delete(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            Path(os.path.join(root, name)).unlink()


def delete_category():
    entered_category = input('Enter the category: ').lower()
    find_and_delete_dic(entered_category, main_path)
    start_process(actions)


def find_and_delete_dic(name, path):
    for root, dirs, files in os.walk(path):
        if name in dirs:
            shutil.rmtree(Path(os.path.join(root, name)))


def exit_program():
    print('Closing program')


extension_type = '.txt'
main_path = Path('C:/Users/atzar/projects/learning/python-proyects/receipts/')
number_of_files = len(list(Path(main_path).glob(f'**/*{extension_type}')))
actions = [
    {
        'id': 1,
        'name': 'Read receipt',
        'function': read_receipt
    },
    {
        'id': 2,
        'name': 'Create receipt',
        'function': create_receipt
    },
    {
        'id': 3,
        'name': 'Create category',
        'function': create_category
    },
    {
        'id': 4,
        'name': 'Delete receipt',
        'function': delete_receipt
    },
    {
        'id': 5,
        'name': 'Delete category',
        'function': delete_category
    },
    {
        'id': 6,
        'name': 'Finish process',
        'function': exit_program
    }
]

# We start the program
start_process(actions)


