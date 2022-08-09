import csv
import os

r_path = os.path.join('GUI', 'Export', 'DataBase', 'phonebook.csv')


def print_csv() -> str:
    with open (r_path, encoding='utf-8') as r_file:
            reader = csv.reader(r_file, delimiter=';')
            counter = 0
            text = ''
            for row in reader:
                if counter == 0: 
                    f_name = row[0]
                    l_name = row[1]
                    phone  = row[2]
                    adr    = row[3]
                else:
                    text += f'{row[0]}{row[1]},{phone}={row[2]},{adr} ={row[3]}.\n'

                counter += 1
    return text

