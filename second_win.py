from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from final_win import *
class Second_win(QWidget):
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
        self.FIO_l =QLabel('Введите Ф.И.О')
        self.FiO_ld=QLineEdit()
        self.age_l=QLabel('Введите возраст')
        self.age_ld=QLineEdit()
        
        self.rec1=QLabel('Ляг')
        self.rec2=QLabel('Присядай')
        self.rec3=QLabel('Отдыхай')
        self.res1=QLineEdit()
        self.res2=QLineEdit()
        self.res3=QLineEdit()
        self.but1=QPushButton('Жми как готов')
        self.but2=QPushButton('Жми как готов')
        self.but3=QPushButton('Жми как готов')
        self.next=QPushButton('Показать на сколько ты стар')
        
        
        
        self.lay=QVBoxLayout()
        self.lay.addWidget(self.FIO_l)
        self.lay.addWidget(self.FiO_ld)
        self.lay.addWidget(self.age_l)
        self.lay.addWidget(self.age_ld)
        self.lay.addWidget(self.rec1)
        self.lay.addWidget(self.res1)
        self.lay.addWidget(self.but1)
        self.lay.addWidget(self.rec2)
        self.lay.addWidget(self.res2)
        self.lay.addWidget(self.but2)
        self.lay.addWidget(self.rec3)
        self.lay.addWidget(self.res3)
        self.lay.addWidget(self.but3)
        self.lay.addWidget(self.next)
        self.setLayout(self.lay)
        
    
    def connects(self):
        self.next.clicked.connect(self.to_third)

    def to_third(self):
        self.hide()
        self.next_screen= final_win()