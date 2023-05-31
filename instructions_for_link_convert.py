#!/usr/bin/evn python
from tkinter import Tk, Label, X


def instructions():
    info = Tk()
    info.title("Инструкция")
    info.geometry('550x580')
    info.configure(bg="#fff")
    label_info_for_redos = Label(info, text='\n1. Инструкция для открытия ссылки на файловый сервер в РЕД ОС', justify='center', wraplength=500,
                                 font=("Arial", 16), fg="black", bg='#FFF')
    label_info_for_redos.pack(fill=X, anchor="nw", padx=10, pady=5)
    info_for_redos = Label(info,
                           text='Для того чтобы открыть ссылку на файловый сервер: \n   1) Cкопируйте ссылку из почты;' \
                                '\n   2) В разделе "Для РЕД ОС", нажмите кнопку "Вставить"; \n   3) Нажмите кнопку "Открыть".' \
                                '\nПосле этого откроется папка по вашей ссылке.',
                           justify='left', wraplength=500, font=("Arial", 12), fg="black", bg='#FFF')
    info_for_redos.pack(fill=X, anchor="nw", padx=10, pady=5)

    label_info_for_windows = Label(info,
                                   text='\n2. Инструкция для отправки ссылки на папку с файлового сервера пользователям, которые работают на Windows',
                                   justify='center', wraplength=500, font=("Arial", 16), fg="black", bg='#FFF')
    label_info_for_windows.pack(fill=X, anchor="nw", padx=10, pady=5)
    info_for_windows = Label(info,
                             text='Для того чтобы отправить ссылку на файловый сервер: \n   1) Cкопируйте ссылку на папку:' \
                                  '\n      1.1) Откройте папку, в которой находится необходимая информация;' \
                                  '\n      1.2) Нажмите на карандаш (находится над всеми файлами), появится путь к папке;' \
                                  '\n      1.3) Выделите путь и правой кнопкой мыши (или нажатием CTRL+С) скопируйте его.' \
                                  '\n   2) В разделе "Для Windows", нажмите кнопку "Вставить"; \n   3) Нажмите кнопку "Преобразовать";' \
                                  '\n   4) Нажмите кнопку "Копировать";' \
                                  '\n   5) Откройте созданное письмо в почте и вставьте (правой кнопкой мыши или нажатием CTRL+V) вашу ссылку.' \
                                  '\n\n\n По всем вопросам обращайтесь в службу технической поддержки пользователей: sd@tsk-mosenergo.ru',
                             justify='left', wraplength=500, font=("Arial", 12), fg="black", bg='#FFF')
    info_for_windows.pack(fill=X, anchor="nw", padx=10, pady=5)