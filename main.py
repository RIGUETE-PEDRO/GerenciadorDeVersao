import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel

app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle("Minha primeira tela")
janela.resize(400, 300)

label = QLabel("Olá, esta é minha tela!", janela)
label.move(100, 130)

janela.show()

sys.exit(app.exec())