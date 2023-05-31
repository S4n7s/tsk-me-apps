#!/usr/bin/evn python
from tkinter import Tk, Entry, Button, LabelFrame, X, END, filedialog, RIGHT, LEFT
import os
import subprocess
from footer import add_footer
from instructions_for_msg_eml import instructions


def convert():
    for file in os.listdir(directory_input_entry.get()):
        if file.endswith('.msg'):
            infile = os.path.join(directory_input_entry.get(), file)
            outfile = os.path.join(directory_output_entry.get(), file[:-4] + '.eml')
            subprocess.run(['msgconvert', infile, '-o', outfile])


def browse_button_input():
    directory = filedialog.askdirectory()
    directory_input_entry.delete(0, END)
    directory_input_entry.insert(0, directory)


def browse_button_output():
    directory = filedialog.askdirectory()
    directory_output_entry.delete(0, END)
    directory_output_entry.insert(0, directory)


msg_eml = Tk()

msg_eml.title("Преобразование писем")
msg_eml.geometry("500x270")
msg_eml.configure(bg="#fff")

# ----------------------INSTRUCTIONS----------------------

info_button = Button(text="Инструкция", fg="white", bg="#0079C0", command=instructions, font=("Arial", 10))
info_button.pack(anchor='ne', padx=10, pady=10)

# ----------------------MSG----------------------

frame_input = LabelFrame(text="Выберите каталог с файлами .msg:", bg='#FFF')
frame_input.pack(fill=X, padx=5, pady=5)
directory_input_entry = Entry(frame_input, font=("Arial", 12), bg="silver")
directory_input_entry.pack(side=LEFT, expand=True, fill=X, anchor="n", padx=10, pady=10)
button_browse = Button(frame_input, text="Обзор...", command=browse_button_input, fg="white", bg="#0079C0", font=("Arial", 10))
button_browse.pack(side=RIGHT, padx=10)

# ----------------------EML----------------------

frame_output = LabelFrame(text="Выберите каталог для сохранения файлов .eml:", bg='#FFF')
frame_output.pack(fill=X, padx=5, pady=10)
directory_output_entry = Entry(frame_output, font=("Arial", 12), bg="silver")
directory_output_entry.pack(side=LEFT, expand=True, fill=X, anchor="n", padx=10, pady=10)
button_browse = Button(frame_output, text="Обзор...", command=browse_button_output, fg="white", bg="#0079C0", font=("Arial", 10))
button_browse.pack(side=RIGHT, padx=10)
button_convert = Button(msg_eml, text="Преобразовать", command=convert, fg="white", bg="#0079C0", font=("Arial Bold", 10))
button_convert.pack(padx=5)

# ----------------------FOOTER----------------------

add_footer()

# --------------------------------------------------

msg_eml.mainloop()
