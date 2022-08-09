import tkinter as tk
from pathlib import os
from GUI.import_person import import_person


class AddPersonWindow:

    def __init__(self,):
        self.win = tk.Tk()
        self.win_geometry = '500x230+200+200'
        self.title = 'Добавляем контакт'
        self.icon_path = os.path.join('GUI', 'contact.png')
        self.window_modify(self.win, self.title, self.win_geometry,self.icon_path)

        self.entry_witdh = 30
        self.e_col_minsize = 400
        self.e_row_minsize = 50
        self.name_entry = self.add_entry(self.win, self.entry_witdh, 0, 1, self.e_row_minsize, self.e_row_minsize)
        self.last_name_entry = self.add_entry(self.win, self.entry_witdh, 1, 1, self.e_row_minsize, self.e_row_minsize)
        self.phone_entry = self.add_entry(self.win, self.entry_witdh, 2, 1, self.e_row_minsize, self.e_row_minsize)
        self.address_entry = self.add_entry(self.win, self.entry_witdh, 3, 1, self.e_row_minsize, self.e_row_minsize)
        
        self.lbl_col_Minsize = 50
        self.name_lbl = self.add_label(self.win, 'Имя', 0,self.lbl_col_Minsize)
        self.last_name_lbl = self.add_label(self.win, 'Фамилия', 1,self.lbl_col_Minsize)
        self.phone_lbl = self.add_label(self.win, 'Телефон', 2,self.lbl_col_Minsize)
        self.address_lbl = self.add_label(self.win, 'Адрес', 3,self.lbl_col_Minsize)

        self.add_btn = self.add_button(self.win, command=self.add_contact, text='Добавить контакт', row=0, )
        self.win.mainloop()

    def get_info(self):
        f_name = self.name_entry.get()
        self.name_entry.delete(0, len(f_name))
        l_name = self.last_name_entry.get()
        self.last_name_entry.delete(0, len(l_name))
        phone = self.phone_entry.get()
        self.phone_entry.delete(0, len(phone))
        address = self.address_entry.get()
        self.address_entry.delete(0,len(address))
        
        info = f_name + '; ' + l_name + '; ' + phone + '; ' + address
        return info

    def add_contact(self,):
        info = self.get_info()
        if len(info) > 6:
            import_person(info)

    def add_label(self, win: tk.Tk, 
                  text: str,
                  row: int,
                  col_minsize: int):
        lbl = tk.Label(win, text=text, font='arial')
        lbl.grid(row=row, column=0, sticky='ew')
        win.columnconfigure(0, minsize=col_minsize)
        return lbl

    def add_entry(self, win: tk.Tk,
                  width: int,
                  row: int,
                  column: int,
                  col_minsize,
                  row_minsize):
        entry = tk.Entry(win, font='Arial', relief='solid', width=width)
        entry.grid(row=row, column=column)
        win.columnconfigure(column, minsize=col_minsize)
        win.rowconfigure(row, minsize=row_minsize)
        return entry

    def window_modify(self, win: tk.Tk,
                      title: str, 
                      win_geometry: str, 
                      icon_path: str):
        win.title(title)
        win.geometry(win_geometry)
        win.resizable(False, False)
        # icon = tk.PhotoImage(file=self.icon_path)  #При запуске из phonebook_gui.py не видит фото иконки. При запуске от сюда все ОК.
        # win.iconphoto(False, icon)

    def add_button(self, win: tk.Tk, command, text: str, row: int):
        btn = tk.Button(win, command=command, text=text, width=15)
        btn.grid(column=2, row=row, sticky="e")
        win.columnconfigure(2, minsize=150)
        return btn
        
