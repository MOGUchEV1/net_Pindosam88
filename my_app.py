# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt, QTimer, QTime 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from instr import *
from second_win import *
        
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_win()
        self.initUI()
        self.connects()
        self.show()
    
    def set_win(self):
        self.setWindowTitle('Тест Руфье')
        self.resize(400,400)
    
    def initUI(self):
        self.hello = QLabel(txt_hello)
        self.desc=QLabel(txt_next)
        self.next= QPushButton('Начать')
        self.lay=QVBoxLayout()
        self.lay.addWidget(self.hello)
        self.lay.addWidget(self.desc)
        self.lay.addWidget(self.next)
        self.setLayout(self.lay)
    
    def connects(self):
        self.next.clicked.connect(self.to_second)

    def to_second(self):
        self.hide()
        self.next_screen= Second_win() 
app=QApplication([])
my_r=MainWin()        
app.exec()