#!/usr/bin/evn python
from tkinter import Tk, Button, LEFT, LabelFrame, X, font
from footer import add_footer
import subprocess, os


def open_link_convert():
    home = os.path.expanduser("~")
    path = os.path.join(home, "tsk-me-app", "link_convert.py")
    subprocess.Popen(['python', path])
    main.destroy()


def open_msg_eml():
    home = os.path.expanduser("~")
    path = os.path.join(home, "tsk-me-app", "msg_eml.py")
    subprocess.Popen(['python', path])
    main.destroy()


main = Tk()

main.title("Программы")
main.geometry("305x115")
main.configure(bg="#fff")

frame_soft = LabelFrame(main, bg='#fff')
frame_soft.pack(fill=X)
button1 = Button(frame_soft, text="Преобразование ссылок", font=("Arial", 10), command=open_link_convert, wraplength=120, fg="white", bg="#0079C0")
button1.pack(side=LEFT, padx=10, pady=15)
button2 = Button(frame_soft, text="Преобразование писем", font=("Arial", 10), command=open_msg_eml, wraplength=120, fg="white", bg="#0079C0")
button2.pack(side=LEFT, padx=10, pady=15)

add_footer()

main.mainloop()
