# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from instr import *
class final_win(QWidget):
    def __init__(self):
        super().__init__()
        self.set_win()
        self.initUI()
        self.show()
    
    def set_win(self):
        self.setWindowTitle('Тест Руфье')
        self.resize(400,400)
    
    def initUI(self):
        self.ans1= QLabel('Тудак')
        self.ans2=QLabel('Судак')
        self.next= QPushButton('Начать')
        self.lay=QVBoxLayout()
        self.lay.addWidget(self.ans2)
        self.lay.addWidget(self.ans1)
        self.setLayout(self.lay)
