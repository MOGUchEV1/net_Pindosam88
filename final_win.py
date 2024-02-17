# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from instr import *
class final_win(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp=exp
        self.get_index()
        self.set_win()
        self.initUI()
        self.show()
    
    def set_win(self):
        self.setWindowTitle('Тест Руфье')
        self.resize(400,400)
    
    def initUI(self):
        self.ans2=QLabel(txt_workheart + str(self.result()))
        self.ans1= QLabel(txt_index + str(self.index))
        self.next= QPushButton('Начать')
        self.lay=QVBoxLayout()
        self.lay.addWidget(self.ans2)
        self.lay.addWidget(self.ans1)
        self.setLayout(self.lay)
    def result(self):
        print("AAAAA")
        if self.exp.age >= 15:
            return self.my_fun(self.index, 0)
        elif self.exp.age >= 13:
            return self.my_fun(self.index, 1)
        elif self.exp.age >= 11 :
            return self.my_fun(self.index, 2)
        elif self.exp.age >= 9:
            return self.my_fun(self.index, 3)
        elif  self.exp.age>=7:
            return self.my_fun(self.index, 4)
    def my_fun(self,x ,i):
        print(x, i)
        if x > 15 + 1.5*i:
            return text_res1
        elif x > 11 + 1.5*i:
            return text_res2
        elif x > 6 + 1.5*i:
            return text_res3
        elif x > 0.5 + 1.5*i:
            return text_res4
        else:
            return text_res5

    def  get_index(self):
        self.index=(4*(int(self.exp.t1) + int(self.exp.t2) +int(self.exp.t3))-200)/10