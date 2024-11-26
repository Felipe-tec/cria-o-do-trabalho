import sys
# importar os componentes para a
# construção da janela
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QTableView, QHBoxLayout, QVBoxLayout, QWidget
# Construção da classe janela com o nome de caixa
class Caixa(QWidget):
    #Criação do método __init__ que inicia a janela 
    # e exibe ela em tela
    def __init__(self):
        super().__init__()
        # vamos definir a posição e o tamanho da
        # tela
        self.setGeometry(0,30,1000,800)

        # Vamos definir o triufo da nossa janela
        self.setWindowTitle("Caixa da loja")

        # Vamos criar as labels  que representam 
        # as colunas esquerda e direitas 

        # label da esquerda
        self.label_coluna_esquerda = QLabel()
        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color:#0c0}")

        #label da direita
        self.label_coluna_direita = QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#c00}")

        #criar o layout horinzontal para
        # as colunas
        self.h_layout = QHBoxLayout()

        # vamos adicionar as colunas 
        # esquerda e direita ao layout
        #horinzontal
        self.h_layout.addWidget(self.label_coluna_esquerda)
        self.h_layout.addWidget(self.label_coluna_direita)

        # adicionar o layout na tela 
        self.setLayout(self.h_layout)

        


app = QApplication(sys.argv)
cx = Caixa()
cx.show()
app.exec_()