#!/usr/bin/evn python
from tkinter import *
import pyperclip
import os
from footer import add_footer
from instructions_for_link_convert import instructions
import urllib.parse


def paste_redos():
    link_for_redos.delete(0, END)
    link_for_redos.insert(0, pyperclip.paste())


def paste_windows():
    link_for_windows.delete(0, END)
    link_for_windows.insert(0, pyperclip.paste())


def copy():
    link_convertor.clipboard_clear()
    link_convertor.clipboard_append(link_convertor.get().rstrip())

def escape_special_chars(string):
    escaped_chars = ['\'', ' ', '&', ';', '(', ')', '[', ']', '{', '}']
    for char in escaped_chars:
        string = string.replace(char, '\\' + char)
    return string

def convert_under_redos():
    url = link_for_redos.get()
    if url.startswith('file://'):
        link = urllib.parse.unquote(url).replace('file:', '')
    else:
        link = url.replace('\\', '/')
    os.system(rf'caja smb:{escape_special_chars(link)}')

def convert_under_windows():
    link = link_for_windows.get()
    link_convertor.insert(0, link.replace('smb:', '').replace('/', '\\').replace('%20', ' '))


root = Tk()

root.title("Преобразование ссылок")
root.geometry('585x450')
root.configure(bg="#fff")

# ----------------------INSTRUCTIONS----------------------

info_button = Button(text="Инструкция", fg="white", bg="#0079C0",
                     command=instructions, font=("Arial", 10))
info_button.pack(anchor='ne', padx=10, pady=10)

# ----------------------RED-OS----------------------

frame_for_redos = LabelFrame(text="Для РЕД ОС", bg='#FFF')
frame_for_redos.pack(expand=True, fill=X, padx=10)
label_for_redos = Label(frame_for_redos, text="Вставьте ссылку на файловый сервер:",
                        wraplength=585, font=("Arial", 16), fg="black", bg='#FFF')
label_for_redos.pack(anchor="nw", padx=10, pady=5)
link_for_redos = Entry(frame_for_redos, font=("Arial", 12), bg="silver")
link_for_redos.pack(expand=True, fill=X, anchor="n", padx=10, pady=5)
open_button = Button(frame_for_redos, text="Открыть", fg="white", bg="#0079C0",
                     command=convert_under_redos, font=("Arial Bold", 12))
open_button.pack(side=RIGHT, anchor="ne", padx=10, pady=10)
paste_button = Button(frame_for_redos, text="Вставить", fg="white", bg="#0079C0",
                      command=paste_redos, font=("Arial Bold", 12))
paste_button.pack(side=RIGHT, anchor="ne", pady=10)

# ----------------------WINDOWS----------------------

frame_for_windows = LabelFrame(text="Для Windows", bg='#FFF')
frame_for_windows.pack(expand=True, fill=X, padx=10)
frame_link_redos = LabelFrame(frame_for_windows, text="Ссылка из РЕД ОС", bg='#FFF')
frame_link_redos.pack(expand=True, fill=X, padx=10)
label_for_windows = Label(frame_link_redos, text="Вставьте ссылку на файловый сервер:",
                          wraplength=585, font=("Arial", 16), fg="black", bg="#FFF")
label_for_windows.pack(anchor="nw", padx=10, pady=5)
link_for_windows = Entry(frame_link_redos, font=("Arial", 12), bg="silver")
link_for_windows.pack(expand=True, fill=X, anchor="n", padx=10, pady=5)
frame_link_windows = LabelFrame(frame_for_windows, text="Ссылка для Windows", bg='#FFF')
frame_link_windows.pack(expand=True, fill=X, padx=10)
link_convertor = Entry(frame_link_windows, font=("Arial", 12), bg="silver")
link_convertor.pack(expand=True, fill=X, anchor="n", padx=10, pady=5)
copy_button = Button(frame_for_windows, text="Копировать", fg="white", bg="#0079C0",
                     command=copy, font=("Arial Bold", 12))
copy_button.pack(side=RIGHT, anchor="ne", padx=10, pady=10)
convert_button = Button(frame_for_windows, text="Преобразовать", fg="white", bg="#0079C0",
                        command=convert_under_windows, font=("Arial Bold", 12))
convert_button.pack(side=RIGHT, anchor="ne", pady=10)
paste_button = Button(frame_for_windows, text="Вставить", fg="white", bg="#0079C0",
                      command=paste_windows, font=("Arial Bold", 12))
paste_button.pack(side=RIGHT, anchor="ne", padx=10, pady=10)

# ----------------------FOOTER----------------------

add_footer()

# --------------------------------------------------

root.mainloop()
