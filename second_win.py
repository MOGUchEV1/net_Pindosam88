# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from instr import *
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
        self.FIO_l =QLabel(txt_name)
        self.FiO_ld=QLineEdit()
        self.age_l=QLabel(txt_age)
        self.age_ld=QLineEdit()
        
        self.rec1=QLabel(txt_test1)
        self.rec2=QLabel(txt_test2)
        self.rec3=QLabel(txt_test3)
        self.res1=QLineEdit()
        self.res2=QLineEdit()
        self.res3=QLineEdit()
        self.but1=QPushButton('Жми как готов')
        self.but2=QPushButton('Жми как готов')
        self.but3=QPushButton('Жми как готов')
        self.next=QPushButton(txt_sendresults)
        
        
        
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