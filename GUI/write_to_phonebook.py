import os


def write_to_book(person: str):
    path = os.path.join('GUI','Export', 'DataBase', 'phonebook.csv')

    with open(path, 'a', encoding='utf-8') as adder:
        adder.write(person + '\n')