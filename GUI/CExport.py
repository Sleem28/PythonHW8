import tkinter as tk
import os
import webbrowser
from GUI.Export.export_file_to_html import export_file_to_html
from GUI.Export.print_csv import print_csv


class Export:

    def __init__(self):
        self.win = tk.Tk()
        self.win_geometry = '600x500+300+300'
        self.title = 'Экспорт'
        self.window_modify(self.win, self.title, self.win_geometry)
        print(os.path)
        self.btn = self.add_button(self.win, command=self.show_html, text='Конвертировать в html', row=0)

        self.lbl_col_Minsize = 50
        self.name_lbl = self.add_label(self.win, 'Все контакты', 1,self.lbl_col_Minsize)

        self.t_field = self.add_field(self.win, 2)
        self.win.mainloop()

    def add_field(self, win: tk.Tk, row: int,):
        field = tk.Text(win, width=72, height=27, relief='solid') 
        field.grid(row=row, column=0)

        scroll_bar = tk.Scrollbar(win, command=field.yview)
        scroll_bar.grid(row=row, column=0, sticky='sne', padx=12, pady=2)
        field.config(yscrollcommand=scroll_bar.set)
        text = print_csv()
        field.insert("end", text)

        return field

    def add_label(self, win: tk.Tk, 
                  text: str,
                  row: int,
                  col_minsize: int):
        lbl = tk.Label(win, text=text, font='arial')
        lbl.grid(row=row, column=0, sticky='ew')
        win.columnconfigure(1, minsize=col_minsize)
        return lbl

    def show_html(self):
        export_file_to_html()
        webbrowser.open('GUI\Export\DataBase\phonebook.html')

    def add_button(self, win: tk.Tk, command, text: str, row: int):
        btn = tk.Button(win, command=command, text=text, width=25)
        btn.grid(column=0, row=row, sticky="ew")
        win.columnconfigure(0, minsize=600)
        return btn

    def window_modify(self, win: tk.Tk,
                      title: str, 
                      win_geometry: str):
        win.title(title)
        win.geometry(win_geometry)
        win.resizable(False, False)

