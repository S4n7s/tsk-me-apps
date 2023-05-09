import os
import subprocess
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QLabel, QPushButton, QMessageBox
from PyQt5.QtCore import QBasicTimer, Qt


class UpdateChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Обновление')
        self.setGeometry(500, 500, 400, 100)

        self.progress_label = QLabel(self)
        self.progress_label.setGeometry(50, 50, 300, 25)
        self.progress_label.setAlignment(Qt.AlignCenter)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(50, 25, 300, 20)

        self.check_for_updates()

    def check_for_updates(self):
        repo_url = 'https://api.github.com/repos/S4n7s/tsk-me-apps/releases/latest'
        try:
            response = requests.get(repo_url)
            response.raise_for_status()
            latest_version = response.json()['tag_name']
            current_version = 'v.1.0'  # Replace with the current version of your app
            if latest_version != current_version:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle('Доступно обновление')
                msg_box.setText(f'Доступна новая версия ({latest_version}). Хотите запустить обновление?')
                msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                # Get the "Yes" and "No" buttons and change their text
                yes_button = msg_box.button(QMessageBox.Yes)
                yes_button.setText("Да")
                no_button = msg_box.button(QMessageBox.No)
                no_button.setText("Нет")
                msg_box.setDefaultButton(QMessageBox.Yes)
                result = msg_box.exec_()
                if result == QMessageBox.Yes:
                    self.start_download()
                    #self.close()
                else:
                    self.open_app_window()
                    self.close()
                    #sys.exit()

            else:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle('Актуальная версия')
                msg_box.setText('Обновление приложения не требуется.')
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.setDefaultButton(QMessageBox.Ok)
                msg_box.exec_()
                self.open_app_window()
                self.close()
        except requests.exceptions.RequestException as e:
            # Handle any errors that may occur during the API request
            print(f'Error checking for updates: {e}')

    def start_download(self):
        self.progress_label.setText('Загрузка...')
        self.progress_bar.setValue(0)
        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(100, self)

        # Replace this with code to download the new version of the app
        # For example:
        file_url = 'https://example.com/new_app_version.zip'
        response = requests.get(file_url, stream=True)
        file_size = int(response.headers.get('Content-Length', 0))

        with open('new_app_version.zip', 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    downloaded_size = f.tell()
                    progress = int((downloaded_size / file_size) * 100)
                    self.progress_bar.setValue(progress)

        # Once the file has been downloaded, start the new version of the app
        self.progress_label.setText('Загрузка завершена.')
        self.open_app_window()

    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.progress_label.setText('Загрузка завершена.')
            self.open_app_window()
            return
        self.step += 1
        self.progress_bar.setValue(self.step)

    def open_app_window(self):
        app_file = os.path.join(os.path.dirname(__file__), 'main.py')
        subprocess.Popen(['python', app_file])
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UpdateChecker()
    ex.show()
    sys.exit(app.exec_())