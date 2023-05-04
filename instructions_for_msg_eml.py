#!/usr/bin/evn python
from tkinter import Tk, Label, CENTER, LEFT, X


def instructions():
    info = Tk()
    info.title("Инструкция")
    info.geometry('550x450')
    info.configure(bg="#fff")
    label_info = Label(info, text='\nИнструкция для преобразования писем Outlook в РЕД ОС', justify=CENTER, wraplength=500,
                                 font=("Arial", 16), fg="black", bg='#FFF')
    label_info.pack(fill=X, anchor="nw", padx=10, pady=5)
    instruction = Label(info,
                           text='   Для того чтобы преобразовать письма Outlook в формат писем в РЕД ОС:' \
                                '\n\n   1) В разделе выбора каталога с файлами .msg нажмите кнопку "Обзор..."' \
                                '\n   2) Зайдите в папку, в которой находятся файлы писем Outlook;' \
                                '\n   3) Нажмите кнопку "Выбор папки";' \
                                '\n   4) В разделе выбора каталога для сохранения файлов .eml нажмите кнопку "Обзор..."' \
                                '\n   5) Зайдите в папку, в которую хотите сохранить преобразованные письма;' \
                                '\n   6) Нажмите кнопку "Выбор папки";' \
                                '\n   7) Нажмите кнопку "Преобразовать".' \
                                '\n\n   После этого все письма Outlook будут сохранены в выбранной Вами папке в преобразованном формате.'
                                '\n\n\n   По всем вопросам обращайтесь в службу технической поддержки пользователей: sd@tsk-mosenergo.ru',
                           justify=LEFT, wraplength=500,
                           font=("Helvetica", 12), fg="black", bg='#FFF')
    instruction.pack(fill=X, anchor="nw", padx=10, pady=5)