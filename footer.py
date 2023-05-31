#!/usr/bin/evn python
from tkinter import Label, BOTTOM
import version


def add_footer():
    footer_text = "v." + version.current_version + " ©️ 2023, ТСК Мосэнерго"
    footer = Label(text=footer_text, compound='bottom', fg="black", bg="#fff")
    footer.pack(side=BOTTOM, anchor='s', pady=10)
