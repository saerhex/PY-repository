import os
import threading
import sys
import socket
from window import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5.QtCore import pyqtSlot
from window import Ui_MainWindow

DEST_PORT = input()
SRC_PORT = input()

DEST_ADDRESS = ('localhost', int(DEST_PORT))
SRC_ADDRESS = ('localhost', int(SRC_PORT))


def setup():
    os.environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    os.environ["QT_SCALE_FACTOR"] = "1"


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.text = []

        self.ui.pushButton.clicked.connect(self.click_send_msg)

        self.get_msg()

    @pyqtSlot()
    def click_send_msg(self):
        text = self.ui.lineEdit.text()
        if not text:
            QMessageBox.critical(self, "Error", "Enter text under the button!", QMessageBox.Ok)
            return
        else:
            with TCPClient(DEST_ADDRESS).server as serv:
                serv.send(bytes(text, encoding='UTF-8'))

    def get_msg(self):
        thread = threading.Thread(target=self.worker)
        thread.start()

    def worker(self):
        while True:
            with TCPServer(10, SRC_ADDRESS).server as server:
                try:
                    client, address = server.accept()
                except socket.error:
                    pass
                else:
                    self.text.append(str(client.recv(1024).decode('utf-8')))
                    self.ui.lineEdit_2.setText('\n'.join(self.text))
                    client.close()


class TCPServer:

    def __init__(self, query_len, address=None):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(address)
        self.server.listen(query_len)


class TCPClient:

    def __init__(self, address):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect(address)


if __name__ == '__main__':
    setup()
    app = QApplication([])
    application = Window()
    application.show()
    sys.exit(app.exec())
