#!/usr/bin/evn python
from tkinter import Label, BOTTOM


def add_footer():
    footer = Label(text="©️2023, ТСК Мосэнерго", compound='bottom', fg="black", bg="#fff")
    footer.pack(side=BOTTOM, anchor='s', pady=10)
