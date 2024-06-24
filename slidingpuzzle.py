import sys
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

leveldif = 3
color3 = 'color:red;'
color4 = 'color:black;'
color5 = 'color:black;'
    

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sliding Puzzle")
        self.setGeometry(500, 250, 700, 500)
        self.UIComponents()
        self.show()
        
    def UIComponents(self):
        labelTitle = QLabel('Sliding Puzzle', self)
        labelTitle.setGeometry(100, 125, 500, 100)
        labelTitle.setStyleSheet('font-size:50px; font-weight:bold; font-family:Gotham Black;')
        labelTitle.setAlignment(Qt.AlignCenter)
        labelAuthor = QLabel('Popoacă Georgian', self)
        labelAuthor.setGeometry(100, 175, 500, 100)
        labelAuthor.setAlignment(Qt.AlignCenter)
        labelAuthor.setStyleSheet('font-size:25px; font-family:Gotham;')
        lNivel = QLabel(self)
        lNivel.setText('Nivel ales: ' + str(leveldif) + 'x' + str(leveldif))
        lNivel.setGeometry(100, 225, 500, 100)
        lNivel.setAlignment(Qt.AlignCenter)
        lTimp = QLabel(self)
        lTimp.setGeometry(100, 250, 500, 100)
        lTimp.setAlignment(Qt.AlignCenter)
        
        button1 = QPushButton('Joaca!', self)
        button1.setGeometry(100, 400, 100, 25)
        button1.setStyleSheet('font-family:Gotham;')
        button1.clicked.connect(self.openGame)
        
        button2 = QPushButton('Setari', self)
        button2.setStyleSheet('font-family:Gotham;')
        button2.setGeometry(300, 400, 100, 25)
        button2.clicked.connect(self.openSettings)
        
        button3 = QPushButton('Ieșire', self)
        button3.setStyleSheet('font-family:Gotham;')
        button3.setGeometry(500, 400, 100, 25)
        button3.clicked.connect(self.exit)
        
    def openGame(self):
        self.gw = gameWindow()
        self.gw.show()
        self.hide()
        
    def openSettings(self):
        self.sw = settingsWindow()
        self.sw.show()
        self.hide()
        
    def exit(self):
        QApplication.quit()
            
   
class settingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Setări")
        self.setGeometry(500, 250, 700, 500)
        self.settingsUIComp()
        
    def settingsUIComp(self):
        title = QLabel('Setari', self)
        title.setGeometry(100, 10, 500, 100)
        title.setStyleSheet('font-size:50px; font-family:Gotham Black;')
        title.setAlignment(Qt.AlignCenter)
        
        buttonHome = QPushButton('Home', self)
        buttonHome.setGeometry(100, 400, 100, 25)
        buttonHome.setStyleSheet('font-family:Gotham;')
        buttonHome.clicked.connect(self.openHome)
        
        labelDif = QLabel('Seteaza Dificultatea:', self)
        labelDif.setGeometry(100, 200, 500, 20)
        labelDif.setStyleSheet('font-family:Gotham; font-size:20px;')
        
        b3 = QPushButton('3', self)
        b3.setGeometry(325, 200, 100, 25)
        b3.clicked.connect(self.b3click)
        b3.setStyleSheet(color3)
        
        b4 = QPushButton('4', self)
        b4.setGeometry(450, 200, 100, 25)
        b4.clicked.connect(self.b4click)
        b4.setStyleSheet(color4)
        
        b5 = QPushButton('5', self)
        b5.setGeometry(575, 200, 100, 25)
        b5.clicked.connect(self.b5click)
        b5.setStyleSheet(color5)
        
        
    def b3click(self):
        global color3
        global color4
        global color5
        color3 = 'color:red;'
        color4 = 'color:black;'
        color5 = 'color:black;'
        global leveldif
        leveldif = 3
        self.hide()
        self.show()
        
    def b4click(self):
        global color3
        global color4
        global color5
        color4 = 'color:red;'
        color3 = 'color:black;'
        color5 = 'color:black;'
        global leveldif
        leveldif = 4
        self.hide()
        self.show()
        
    def b5click(self):
        global color3
        global color4
        global color5
        color5 = 'color:red;'
        color3 = 'color:black;'
        color4 = 'color:black;'
        global leveldif
        leveldif = 5
         
    def openHome(self):
        self.w = Window()
        self.w.show()
        self.hide()
        
class gameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sliding Puzzle")
        self.setGeometry(300, 150, 700, 700)
        self.gwUIcomp()
        self.show()
        
    def gwUIcomp(self):
        self.buttons = []
        rand = np.random.permutation(leveldif*leveldif)
        
        k = 0
        for i in range(leveldif):
            for j in range(leveldif):
                button = QPushButton(str(rand[k]), self)
                button.setGeometry(100*j, 100*i, 100, 100)
                button.setStyleSheet('font-size:30px; font-family:Gotham Black;')
                self.buttons.append(button)
                k+=1
        k = 0
        for i in range(leveldif):
            for j in range(leveldif):
                button = self.buttons[k]
                button.clicked.connect(lambda checked, k=k,rand=rand, button=button, buttons = self.buttons: self.click(k, rand, button, buttons))
                k+=1
                
        back = QPushButton('Inapoi', self)
        back.setGeometry(100, 100*leveldif, 100, 25)
        back.clicked.connect(self.back)
                
                
                
    def click(self, k, rand, button, buttons):
        row = k // leveldif
        if k + 1 < len(rand) and rand[k + 1] == 0 and (k + 1) // leveldif == row:
            button.setText(str(rand[k + 1]))
            buttons[k + 1].setText(str(rand[k]))
            rand[k], rand[k+1] = rand[k+1], rand[k]
        elif k - 1 >= 0 and rand[k - 1] == 0 and (k - 1) // leveldif == row:
            button.setText(str(rand[k - 1]))
            buttons[k - 1].setText(str(rand[k]))
            rand[k], rand[k-1] = rand[k-1], rand[k]
        elif k + leveldif < len(rand) and rand[k+leveldif] == 0:
            button.setText(str(rand[k+leveldif]))
            buttons[k + leveldif].setText(str(rand[k]))
            rand[k], rand[k+leveldif] = rand[k+leveldif], rand[k]
        elif k - leveldif >=0 and rand[k-leveldif] == 0:
            button.setText(str(rand[k-leveldif]))
            buttons[k - leveldif].setText(str(rand[k]))
            rand[k], rand[k-leveldif] = rand[k-leveldif], rand[k]
        self.verif(rand)
            
    def verif(self, rand):
        ok = 1
        if rand[0] != 1 or rand[-1] != 0:
            ok = 0
        else:
            for i in range(len(rand) - 1):
                if rand[i + 1] != rand[i] + 1:
                    if rand[i + 1] != 0 or rand[i] != len(rand) - 1:
                        ok = 0
                        break
        if ok == 0:
            print('Puzzle-ul nu este rezolvat')
        else:
            self.c = congrats()
            self.c.show()
            self.hide()
                
    def back(self):
        self.w = Window()
        self.w.show()
        self.hide()
        
class congrats(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sliding Puzzle")
        self.setGeometry(250, 150, 700, 300)
        self.cUIcomp()
        self.show()
    
    def cUIcomp(self):
        Congrats = QLabel('Felicitari! Ati rezolvat puzzle-ul!', self)
        Congrats.setGeometry(0, 0, 700, 300)
        Congrats.setStyleSheet('color:green; font-family:Gotham; font-size:30px;')
        Congrats.setAlignment(Qt.AlignCenter)
        back = QPushButton('Inapoi', self)
        back.setGeometry(300, 200, 100, 25)
        back.clicked.connect(self.back)
        
    def back(self):
        self.w = Window()
        self.w.show()
        self.hide()
        
        
        
        
            
        

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())