#!/usr/bin/evn python
import subprocess, os, requests, shutil, sys, glob, version
from tkinter import Tk, Button, LEFT, TOP, LabelFrame, X, Label, Canvas
from footer import add_footer
from dotenv import load_dotenv
from git import Repo


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

def check_version():
    api_url = f'https://api.github.com/repos/s4n7s/tsk-me-apps/releases/latest'
    response = requests.get(api_url)
    latest_release = response.json()
    latest_version = latest_release['tag_name']
    current_version = '1.1'
    if current_version != latest_version:
        return True

def update_files():
    if os.path.exists(local_path):
        for filename in os.listdir(local_path):
            file_path = os.path.join(local_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
    Repo.clone_from(repo_url, local_path, branch='main')
    '''python_files = glob.glob('*.py')
    for file in python_files:
        os.chmod(file, 0o755)'''
    restart_application()

def restart_application():
    python_executable = sys.executable
    script_path = os.path.abspath(__file__)
    subprocess.Popen([python_executable, script_path])
    sys.exit()
    

load_dotenv()

github_token = os.getenv('GITHUB_TOKEN')
repo_url = 'https://github.com/S4n7s/tsk-me-apps.git'
name_path = 'tsk-me-apps'
home_dir = os.path.expanduser("~")
local_path = os.path.join(home_dir, name_path)

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

if check_version():
    main.geometry("305x175")
    label_update = Label(main, text='Доступно обновление!', justify='center', wraplength=500,
                                     font=("Arial", 10), fg="black", bg='#FFF')
    label_update.pack(fill=X, anchor="nw", padx=10, pady=5)
    button = Button(main, text="Обновить", font=("Arial", 10), command=update_files)
    button.pack(side=TOP, padx=10, pady=3)

    canvas = Canvas(main, width=main.winfo_screenwidth(), height=1, highlightthickness=0)
    canvas.pack()

    canvas.create_line(0, 0, main.winfo_screenwidth(), 0, fill="#808080")

add_footer()

main.mainloop()
