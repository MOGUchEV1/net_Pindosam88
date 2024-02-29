# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt, QTimer, QTime 
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
        self.age_ld=QLineEdit("10")
        
        self.timer_t=QLabel()

        self.rec1=QLabel(txt_test1)
        self.rec2=QLabel(txt_test2)
        self.rec3=QLabel(txt_test3)
        self.res1=QLineEdit("20")
        self.res2=QLineEdit("40")
        self.res3=QLineEdit("30")
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
        self.lay.addWidget(self.but1)
        self.lay.addWidget(self.res1)
        self.lay.addWidget(self.rec2)
        self.lay.addWidget(self.but2)
        self.lay.addWidget(self.res2)
        self.lay.addWidget(self.rec3)
        self.lay.addWidget(self.but3)
        self.lay.addWidget(self.res3)
        self.lay.addWidget(self.timer_t)
        self.lay.addWidget(self.next)
        self.setLayout(self.lay)
        
    
    def connects(self):
        self.next.clicked.connect(self.to_third)
        self.but1.clicked.connect(self.time1)
        self.but2.clicked.connect(self.time2)
        self.but3.clicked.connect(self.time3)


    def to_third(self):
        self.hide()
        self.exp=Rezilt(self.age_ld.text(), self.res1.text(), self.res2.text(), self.res3.text())
        self.next_screen= final_win(self.exp)

    def time1(self):
        self.timer=QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.handle1)
        self.time=0
        self.timer.start()

    def handle1(self):
        print("1")
        self.time+=1
        self.timer_t.setText(str(self.time))
        if self.time>=15:
            self.timer.stop()


    def time2(self):
        self.timer=QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.handle2)
        self.time=0
        self.timer.start()

    def handle2(self):
        print("2")
        self.time+=1
        self.timer_t.setText(str(self.time))
        if self.time>=30:
            self.timer.stop()


    def time3(self):
        self.timer=QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.handle3)
        self.time=0
        self.timer.start()

    def handle3(self):
        print("1")
        self.time+=1
        self.timer_t.setText(str(self.time))
        if self.time>=15:
            self.timer.stop()





class Rezilt():
    def __init__(self, age, test1, test2, test3):
        self.age=int(age)
        self.t1=int(test1)
        self.t2=int(test2)
        self.t3=int(test3)  
