# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from instr import *
from final_win import *
from PyQt5.QtMultimedia import QSound
import sys 

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
        self.FIO_l =QLabel(txt_name)
        self.FiO_ld=QLineEdit()
        self.age_l=QLabel(txt_age)
        self.age_ld=QLineEdit("10")
        
        self.rec1=QLabel(txt_test1)
        self.rec2=QLabel(txt_test2)
        self.rec3=QLabel(txt_test3)
        self.res1=QLineEdit("20")
        self.res2=QLineEdit("40")
        self.res3=QLineEdit("30")
        self.but1=QPushButton('Запуск таймера')
        self.but2=QPushButton('Запуск таймера')
        self.but3=QPushButton('Запуск таймера')
        self.next=QPushButton(txt_sendresults)
        
        
        
        self.lay=QVBoxLayout()
        self.lay.addWidget(self.FIO_l)
        self.lay.addWidget(self.FiO_ld)
        self.lay.addWidget(self.age_l)
        self.lay.addWidget(self.age_ld)
        self.lay.addWidget(self.rec1)
        self.lay.addWidget(self.but1)
        self.lay.addWidget(self.res1)
        self.lay.addWidget(self.rec2) 
        self.lay.addWidget(self.but2)
        self.lay.addWidget(self.res2)
        self.lay.addWidget(self.rec3)
        self.lay.addWidget(self.but3)
        self.lay.addWidget(self.res3)
        self.lay.addWidget(self.next)
        self.setLayout(self.lay)
        
    
    def connects(self):
        self.next.clicked.connect(self.to_third)

    def to_third(self):
        self.hide()
        self.exp=Rezilt(self.age_ld.text(), self.res1.text(), self.res2.text(), self.res3.text())
        self.next_screen= final_win(self.exp)

class Rezilt():
    def __init__(self, age, test1, test2, test3):
        self.age=int(age)
        self.t1=int(test1)
        self.t2=int(test2)
        self.t3=int(test3)  