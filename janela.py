import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit

class MainJanela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Janela')
        self.setGeometry(100, 100, 400, 200)

        self.btn_open_second_janela = QPushButton('Abrir Segunda Janela', self)
        self.btn_open_second_janela.setGeometry(10, 10, 200, 30)
        self.btn_open_second_janela.clicked.connect(self.openSecondJanela)

        self.lbl_second_janela_message = QLabel('', self)
        self.lbl_second_janela_message.setGeometry(10, 50, 380, 30)

    def openSecondJanela(self):
        self.second_janela = SecondJanela(self)
        self.second_janela.show()

    def setSecondJanelaMessage(self, message):
        self.lbl_second_janela_message.setText(f'Mensagem da Segunda Janela: {message}')

class SecondJanela(QWidget):
    def __init__(self, main_janela):
        super().__init__()

        self.main_janela = main_janela
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Segunda Janela')
        self.setGeometry(200, 200, 400, 200)

        layout = QVBoxLayout()

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText('Digite seu nome')
        layout.addWidget(self.name_input)

        self.message_input = QLineEdit(self)
        self.message_input.setPlaceholderText('Digite sua mensagem')
        layout.addWidget(self.message_input)

        btn_send = QPushButton('Enviar', self)
        btn_send.clicked.connect(self.sendMessage)
        layout.addWidget(btn_send)

        self.setLayout(layout)

    def sendMessage(self):
        name = self.name_input.text()
        message = self.message_input.text()

        self.main_janela.setSecondJanelaMessage(f'{name}: {message}')
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_janela = MainJanela()
    main_janela.show()
    sys.exit(app.exec_())
