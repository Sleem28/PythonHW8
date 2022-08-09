import tkinter as tk
from pathlib import Path
from GUI.CFunctions import Functions as func
from GUI.CAddPersonWindow import AddPersonWindow
from GUI.CExport import Export


def start_phonebook():

    def search_contact():              # Ищем контакт в файле csv и выводим его в текстовое поле
        value       = entry.get()
        result_list = list()
        f_text      = field.get(1.0, 'end') # беру весь текст из поля вывода

        if len(f_text) > 0:
            field.delete(1.0, 'end')   # если он есть удаляю при каждом новом нажатии кнопки
        if value:                      # если Entry не пустой
            result_list = func().get_contacts(value)
            entry.delete(0, len(value))
        if len(result_list)>0:
            for item in result_list:
                field.insert(0.0, item)
        
    def add_contact(): # Добавляет контакт в csv по нажатию кнопки. Сделал отдельный класс
        AddPersonWindow()   

    def export():
        Export()

    

    button_width = 8

    main_window = tk.Tk()
    main_window.title('Телефонная книга')
    main_window.geometry('700x300+100+100')
    main_window.resizable(False, False)
    photo = tk.PhotoImage(file=Path('GUI\icons8-phone-book-32.png'))
    main_window.iconphoto(False, photo)


    tk.Label(main_window, text='Поиск:',font='Arial').grid(row=0,column=0, sticky='w')# label для поиска
    main_window.columnconfigure(0, minsize=60)
    main_window.rowconfigure(0, minsize=80)


    tk.Label(main_window, text='',font='Arial').grid(row=2,column=0, sticky='w')# label для расширения текстового поля
    main_window.columnconfigure(0, minsize=60)
    main_window.rowconfigure(0, minsize=80)


    entry = tk.Entry(main_window, font='Arial',relief='solid', width=55) # Поле ввода для поиска контакта
    entry.grid(row=0, column=1)
    main_window.columnconfigure(1, minsize=450)


    tk.Button(main_window, text='Найти', # Кнопка "Найти"
            command=search_contact,
            font='Arial', 
            width=button_width).grid(row=0,column=3)                                
    main_window.columnconfigure(2, minsize=40)


    tk.Button(main_window, text='Добавить', # Кнопка "Добавить контакт"
            command=add_contact,
            font='Arial', 
            width=button_width).grid(row=1,column=3, sticky='n') 
    main_window.columnconfigure(2, minsize=40)


    tk.Button(main_window, text='Експорт', # Кнопка "Експорт"
            command=export,
            font='Arial', 
            width=button_width).grid(row=2,column=3, sticky='n') 
    main_window.columnconfigure(2, minsize=40)


    field = tk.Text(main_window, width=62, height=10, relief='solid') # Текстовое поле
    field.grid(row=1, column=1, rowspan=2)
    scroll_bar = tk.Scrollbar(main_window, command=field.yview)
    scroll_bar.grid(row=1, column=1, rowspan=2, sticky='sne', padx=2, pady=2)
    field.config(yscrollcommand=scroll_bar.set)


    main_window.rowconfigure(1, minsize=80)

    main_window.mainloop()

