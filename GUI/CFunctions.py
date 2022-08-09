import tkinter as tk
import csv
from pathlib import Path


class Functions:

    def __init__(self, *args, **kwargs):
        pass

    def get_contacts(self,text: str):
        res_list = list()
        with open (Path('GUI', 'Export', 'DataBase', 'phonebook.csv'), encoding='utf-8') as r_file:
            reader = csv.reader(r_file, delimiter=';')
            counter = 0
            for row in reader:
                if counter == 0: 
                    phone  = row[2]
                    adr    = row[3]
                else:
                    string = f'{row[0]}{row[1]}, {phone}:{row[2]}, {adr}:{row[3]}.\n\n' if len(row) >=4 else \
                            f'info_error!!!'
                    if text in string:
                        res_list.append(string)
                counter += 1 
        return res_list
