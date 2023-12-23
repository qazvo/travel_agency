import sys
from PyQt6 import QtWidgets

from settings import server_url

from source.login_form import LoginForm
from source.base_worker import BaseWorker

base_worker = BaseWorker(server_url)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginForm(base_worker)
    login_window.show()
    app.exec()