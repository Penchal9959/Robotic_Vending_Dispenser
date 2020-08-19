########################################################################################################################################### LIBRARIES AND MODULES
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QMovie, QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtWebEngineWidgets import *
import os
import time
import smtplib
from email.message import EmailMessage

############################################################################################################################################### WELCOME WINDOW
class Ui_Welcome(object):
    def setupUi(self, Welcome):   
        Welcome.setObjectName("Welcome")
        Welcome.resize(1440, 870)
        
        #Welcome.setStyleSheet("border-radius : 100px; border-style : outset") 
        self.centralWidget = QtWidgets.QWidget(Welcome)
        #self.centralWidget.setStyle('Fusion')
       
                                         
        #START CODE FROM HERE------------------------------------------------------------#
       
        #self.centralWidget.setGeometry(QtCore.QRect(10, 30, 1100, 1050))
        self.centralWidget = self.set_gif("leranta13.gif")
        self.photo12 = QtWidgets.QLabel(self.centralWidget)
        self.photo12.setGeometry(QtCore.QRect(10, 0, 300, 150))
        self.photo12.setPixmap(QtGui.QPixmap("lerantalogo4.png"))
        #PUSHBUTTON SECTION-------------------------------------------------------------#
        self.pushButton0 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton0.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:30px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
##        self.pushButton0.setStyleSheet("QPushButton":hover {
##                                    "color": #ccc;
##                                    "background": red;
##                                    }")
        self.pushButton0.setGeometry(600, 790, 290, 60)
        font = QtGui.QFont('Comic Sans MS')
        font.setPointSize(25)
        self.pushButton0.setFont(font)
        #---------------------------------------------------------------------------------#
        
        Welcome.setCentralWidget(self.centralWidget)
        self.retranslateUi(Welcome)
        QtCore.QMetaObject.connectSlotsByName(Welcome)
         
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Welcome", "Welcome"))
        
        #*******************************************************************************#
        self.pushButton0.setText(_translate("Welcome", "Select your Juice"))
        #*******************************************************************************#
        
    #***********************************************************************************#   
    def set_gif(self,gif_path):
        movie = QtGui.QMovie()
        movie.setFileName (gif_path)
        movie_label = QtWidgets.QLabel()
        movie_label.setMovie (movie)
        movie.start()
        return movie_label
    #*******************************************************************************#

    #*******************************************************************************#
    def LoadJuices(self):
        Juices = QtWidgets.QMainWindow()
        ui = Ui_Juices()
        ui.setupUi(Juices)
        Juices.show()
    #*******************************************************************************#
        
#################################################################################################################################################### JUICES WINDOW       
class Ui_Juices(object):
    def setupUi(self, Juices):
        Juices.setObjectName("Juices")
        Juices.resize(1440, 870)
        self.centralWidget = QtWidgets.QWidget(Juices)
        #START CODE FROM HERE---------------------------------------------------------------#
        self.centralWidget = self.set_gif("cropped.gif")
        
        #PHOTOS HERE-----------------------------------------------------------------------#
        self.photo12 = QtWidgets.QLabel(self.centralWidget)
        self.photo12.setGeometry(QtCore.QRect(10, 0, 300, 150))
        self.photo12.setPixmap(QtGui.QPixmap("lerantalogo4.png"))
        self.photo1 = QtWidgets.QLabel(self.centralWidget)
        self.photo1.setGeometry(QtCore.QRect(60, 30, 1100, 1050))
        self.photo1.setPixmap(QtGui.QPixmap("orange0.png"))
        self.photo2 = QtWidgets.QLabel(self.centralWidget)
        self.photo2.setGeometry(QtCore.QRect(440, 30, 1100, 1080))
        self.photo2.setPixmap(QtGui.QPixmap("wheatgrass1.png"))
        self.photo3 = QtWidgets.QLabel(self.centralWidget)
        self.photo3.setGeometry(QtCore.QRect(780, 30, 300, 1050))
        self.photo3.setPixmap(QtGui.QPixmap("beetapple2.png"))
        self.photo4 = QtWidgets.QLabel(self.centralWidget)
        self.photo4.setGeometry(QtCore.QRect(1150, 30, 900, 1050))
        self.photo4.setPixmap(QtGui.QPixmap("sweet0.png"))
        #----------------------------------------------------------------------------------#
        
        #PUSHBUTTON SECTION----------------------------------------------------------------#
        self.pushButton1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton1.setGeometry(100, 780, 150, 40)
        self.pushButton1.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        font = QtGui.QFont('DejaVu Serif')
        font.setPointSize(25)
        self.pushButton1.setFont(font)
        #---------------------------------------------------------------------------------#
        
        #---------------------------------------------------------------------------------#
        self.pushButton4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton4.setGeometry(1160, 780, 150, 40)
        self.pushButton4.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        
        font = QtGui.QFont('DejaVu Serif')
        font.setPointSize(25)
        self.pushButton4.setFont(font)
        #---------------------------------------------------------------------------------#
        
        #---------------------------------------------------------------------------------#
        self.pushButton2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton2.setGeometry(470, 780, 150, 40)
        self.pushButton2.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        font = QtGui.QFont('DejaVu Serif')
        font.setPointSize(25)
        self.pushButton2.setFont(font)
        #--------------------------------------------------------------------------------#
        
        #---------------------------------------------------------------------------------#
        self.pushButton3= QtWidgets.QPushButton(self.centralWidget)
        self.pushButton3.setGeometry(830, 780, 150, 40)
        self.pushButton3.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        font = QtGui.QFont('DejaVu Serif')
        font.setPointSize(25)
        self.pushButton3.setFont(font)
        #----------------------------------------------------------------------------------#
        
        #---------------------------------------------------------------------------------#
        self.pushButton6= QtWidgets.QPushButton(self.centralWidget)
        self.pushButton6.setGeometry(1340, 10, 100, 40)
        self.pushButton6.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        font = QtGui.QFont('DejaVu Serif')
        font.setPointSize(25)
        self.pushButton6.setFont(font)
        #--------------------------------------------------------------------------------#
        
       #LABELS HERE-----------------------------------------------------------------------#
        self.label1 = QtWidgets.QLabel(self.centralWidget)
        self.label1.setStyleSheet("color:green");
        self.label1.setGeometry(QtCore.QRect(195, 10, 1200, 200))
        font = QtGui.QFont('Times New Roman')
        font.setPointSize(100)
        self.label1.setFont(font)
        #--------------------------------------------------------------------------------#
        
        #--------------------------------------------------------------------------------#
        self.label2 = QtWidgets.QLabel(self.centralWidget)
        self.label2.setStyleSheet("color:rgb(255, 0, 0)");
        self.label2.setGeometry(QtCore.QRect(70, 720, 300, 50))
        font = QtGui.QFont('Impact')
        font.setPointSize(35)
        self.label2.setFont(font)
        #--------------------------------------------------------------------------------#
        
        #--------------------------------------------------------------------------------#
        self.label3 = QtWidgets.QLabel(self.centralWidget)
        self.label3.setStyleSheet("color:rgb(255, 0, 0)");
        self.label3.setGeometry(QtCore.QRect(390, 720, 350, 50))
        font = QtGui.QFont('Impact')
        font.setPointSize(35)
        self.label3.setFont(font)
        #--------------------------------------------------------------------------------#
        
        #-------------------------------------------------------------------------------#
        self.label4 = QtWidgets.QLabel(self.centralWidget)
        self.label4.setStyleSheet("color:rgb(255, 0, 0)");
        self.label4.setGeometry(QtCore.QRect(780, 720, 320, 50))
        font = QtGui.QFont('Impact')
        font.setPointSize(35)
        self.label4.setFont(font)
        #--------------------------------------------------------------------------------#
        
        #--------------------------------------------------------------------------------#
        self.label5 = QtWidgets.QLabel(self.centralWidget)
        self.label5.setStyleSheet("color:rgb(255, 0, 0)");
        self.label5.setGeometry(QtCore.QRect(1080, 720, 400, 50))
        font = QtGui.QFont('Impact')
        font.setPointSize(35)
        self.label5.setFont(font)
        #--------------------------------------------------------------------------------#
        
        #--------------------------------------------------------------------------------#
        self.label10 = QtWidgets.QLabel(self.centralWidget)
        self.label10.setStyleSheet("color:rgb(51, 0, 102)");
        self.label10.setGeometry(QtCore.QRect(1090, 10, 260, 40))
        font = QtGui.QFont('Comic Sans MS')
        font.setPointSize(20)
        self.label10.setFont(font)
        #--------------------------------------------------------------------------------#
        
        Juices.setCentralWidget(self.centralWidget)
        self.retranslateUi(Juices)
        QtCore.QMetaObject.connectSlotsByName(Juices)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Juices", "Juices"))

        #**********************************************************************************#
        self.pushButton1.setText(_translate("Juices", "Select"))
        self.pushButton2.setText(_translate("Juices", "Select"))
        self.pushButton3.setText(_translate("Juices", "Select"))
        self.pushButton4.setText(_translate("Juices", "Select"))
        self.pushButton6.setText(_translate("Juices", "help"))
        #**********************************************************************************#

        #**********************************************************************************#
        self.label2.setText(_translate("Juices", " Orange Hang"))
        self.label3.setText(_translate("Juices", " Wheat Grass Detox"))
        self.label4.setText(_translate("Juices", " Apple Beet Detox"))
        self.label5.setText(_translate("Juices", " Sweet Spinach Detox"))
        self.label10.setText(_translate("Juices", " Hey!, How can I Help you?"))
        #**********************************************************************************#
        
        
    #**********************************************************************************#
    def LoadHelp(self):
        Help = QtWidgets.QMainWindow()
        ui = Ui_Help()
        ui.setupUi(Help)
        Help.show()
    #**********************************************************************************#
        
    #**********************************************************************************#   
    def LoadOrange(self):
        Orange = QtWidgets.QMainWindow()
        ui = Ui_Orange()
        ui.setupUi(Orange)
        Orange.show()
    #**********************************************************************************#
        
    #**********************************************************************************#    
    def LoadWheat_Grass_Detox(self):
        Wheat_Grass_Detox = QtWidgets.QMainWindow()
        ui = Ui_Wheat_Grass_Detox()
        ui.setupUi(Wheat_Grass_Detox)
        Wheat_Grass_Detox.show()
    #**********************************************************************************#
        
    #**********************************************************************************#
    def LoadApple_Beet_Detox(self):
        Apple_Beet_Detox = QtWidgets.QMainWindow()
        ui = Ui_Apple_Beet_Detox()
        ui.setupUi(Apple_Beet_Detox)
        Apple_Beet_Detox.show()
    #**********************************************************************************#
        
    #**********************************************************************************#
    def LoadSweet_Spinach_Detox(self):
        Sweet_Spinach_Detox = QtWidgets.QMainWindow()
        ui = Ui_Sweet_Spinach_Detox()
        ui.setupUi(Sweet_Spinach_Detox)
        Sweet_Spinach_Detox.show()
    #**********************************************************************************#
    
    #**********************************************************************************#
    def set_gif(self,gif_path):
        movie = QtGui.QMovie()
        movie.setFileName (gif_path)
        movie_label = QtWidgets.QLabel()
        movie_label.setMovie (movie)
        movie.start()
        return movie_label
    #**********************************************************************************#




############################################################################################################################################### ORANGE HANG WINDOW   
class Ui_Orange(object):
    def setupUi(self, Orange):
        
        Orange.setObjectName("Orange")
        Orange.resize(1440, 870)
        self.centralWidget = QtWidgets.QWidget(Orange)
        #START CODE FROM HERE--------------------------------------------------#
        self.centralWidget = self.set_gif("orange12.gif")
        
        #PHOTOS SECTION---------------------------------------------------------#
        self.photo12 = QtWidgets.QLabel(self.centralWidget)
        self.photo12.setGeometry(QtCore.QRect(10, 0, 300, 150))
        self.photo12.setPixmap(QtGui.QPixmap("lerantalogo4.png"))
        self.photo1 = QtWidgets.QLabel(self.centralWidget)
        self.photo1.setGeometry(QtCore.QRect(50, 50, 550, 700))
        self.photo1.setPixmap(QtGui.QPixmap("orange20.png"))
        #-----------------------------------------------------------------------#
        
        #PUSHBUTTON SECTION-----------------------------------------------------#
        self.pushButton2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton2.setGeometry(QtCore.QRect(650, 780, 170, 50))
        self.pushButton2.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton2.setFont(font)
        #----------------------------------------------------------------------#

        #----------------------------------------------------------------------#
        self.pushButton3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton3.setGeometry(QtCore.QRect(1250, 780, 150, 50))
        self.pushButton3.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton3.setFont(font)
        #----------------------------------------------------------------------#
        
        #----------------------------------------------------------------------#
        self.pushButton7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton7.setGeometry(1330, 10, 100, 40)
        self.pushButton7.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        font = QtGui.QFont('DejaVu Serif')
        font.setPointSize(25)
        self.pushButton7.setFont(font)
        #----------------------------------------------------------------------#
        
        #LABELS START FROM HERE------------------------------------------------#
        self.label1 = QtWidgets.QLabel(self.centralWidget)
        self.label1.setGeometry(QtCore.QRect(650, 5, 700, 200))
        self.label1.setStyleSheet("color: rgb(240, 113, 96);")
        font = QtGui.QFont('Comic Sans MS')
        font.setPointSize(70)
        self.label1.setFont(font)
        #----------------------------------------------------------------------#

        #----------------------------------------------------------#
        self.label2 = QtWidgets.QLabel(self.centralWidget)
        self.label2.setGeometry(QtCore.QRect(650, 100, 1400, 200))
        self.label2.setStyleSheet("color:orange");
        font = QtGui.QFont('bold')
        font.setPointSize(40)
        self.label2.setFont(font)
        #----------------------------------------------------------------------#

        #----------------------------------------------------------#
        self.label3 = QtWidgets.QLabel(self.centralWidget)
        self.label3.setGeometry(QtCore.QRect(650, 150, 1000, 200))
        self.label3.setStyleSheet("color:green");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label3.setFont(font)
        #----------------------------------------------------------------------#

        #----------------------------------------------------------#
        self.label4 = QtWidgets.QLabel(self.centralWidget)
        self.label4.setGeometry(QtCore.QRect(650, 180, 1000, 200))
        self.label4.setStyleSheet("color:green");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label4.setFont(font)
        #----------------------------------------------------------------------#

        #----------------------------------------------------------#
        self.label5 = QtWidgets.QLabel(self.centralWidget)
        self.label5.setGeometry(QtCore.QRect(650, 210, 1000, 200))
        self.label5.setStyleSheet("color:green");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label5.setFont(font)
        #----------------------------------------------------------------------#

        #----------------------------------------------------------#
        self.label6 = QtWidgets.QLabel(self.centralWidget)
        self.label6.setGeometry(QtCore.QRect(650, 260, 1400, 200))
        self.label6.setStyleSheet("color:orange");
        font = QtGui.QFont('bold')
        font.setPointSize(30)
        self.label6.setFont(font)
        #----------------------------------------------------------------------#
        
        #----------------------------------------------------------#
        self.label7 = QtWidgets.QLabel(self.centralWidget)
        self.label7.setGeometry(QtCore.QRect(650, 310, 1400, 200))
        self.label7.setStyleSheet("color:green");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label7.setFont(font)
        #----------------------------------------------------------------------#
        
        #----------------------------------------------------------#
        self.label8 = QtWidgets.QLabel(self.centralWidget)
        self.label8.setGeometry(QtCore.QRect(650, 340, 1400, 200))
        self.label8.setStyleSheet("color:green");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label8.setFont(font)
        #----------------------------------------------------------------------#
        
        #----------------------------------------------------------#
        self.label9 = QtWidgets.QLabel(self.centralWidget)
        self.label9.setGeometry(QtCore.QRect(650, 370, 1400, 200))
        self.label9.setStyleSheet("color:green");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label9.setFont(font)
        #----------------------------------------------------------------------#
        
        #----------------------------------------------------------#
        self.label10 = QtWidgets.QLabel(self.centralWidget)
        self.label10.setGeometry(QtCore.QRect(650,400, 1400, 200))
        self.label10.setStyleSheet("color:green");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label10.setFont(font)
        #----------------------------------------------------------------------#

        #----------------------------------------------------------#
        self.label11 = QtWidgets.QLabel(self.centralWidget)
        self.label11.setGeometry(QtCore.QRect(650,450, 1400, 200))
        self.label11.setStyleSheet("color:orange");
        font = QtGui.QFont('bold')
        font.setPointSize(30)
        self.label11.setFont(font)
        #----------------------------------------------------------------------#
        
        #----------------------------------------------------------#
        self.label12 = QtWidgets.QLabel(self.centralWidget)
        self.label12.setGeometry(QtCore.QRect(650, 500, 1400, 200))
        self.label12.setStyleSheet("color:green");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label12.setFont(font)
        #----------------------------------------------------------------------#
        
        #----------------------------------------------------------#
        self.label13 = QtWidgets.QLabel(self.centralWidget)
        self.label13.setGeometry(QtCore.QRect(650, 530, 1400, 200))
        self.label13.setStyleSheet("color:green");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label13.setFont(font)
        #----------------------------------------------------------------------#
        
        #----------------------------------------------------------#
        self.label14 = QtWidgets.QLabel(self.centralWidget)
        self.label14.setGeometry(QtCore.QRect(650, 580, 1400, 200))
        self.label14.setStyleSheet("color:red");
        font = QtGui.QFont('bold')
        font.setPointSize(40)
        self.label14.setFont(font)
        #----------------------------------------------------------------------#

        #----------------------------------------------------------#
        self.label15 = QtWidgets.QLabel(self.centralWidget)
        self.label15.setGeometry(QtCore.QRect(1080, 10, 290, 40))
        self.label15.setStyleSheet("color:rgb(51, 0, 102)");
        font = QtGui.QFont('Comic Sans MS')
        font.setPointSize(20)
        self.label15.setFont(font)
        #----------------------------------------------------------------------#
       
        Orange.setCentralWidget(self.centralWidget)
        self.retranslateUi(Orange)
        QtCore.QMetaObject.connectSlotsByName(Orange)
          
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Orange", "Orange"))

        #**********************************************************************#
        self.pushButton7.setText(_translate("Orange", "help"))
        self.pushButton2.setText(_translate("Orange", "Pay Now"))
        self.pushButton3.setText(_translate("Orange", "Back"))
        #**********************************************************************#
        
        #*********************************************************************************#
        self.label1.setText(_translate("Orange","ORANGE HANG"))
        self.label2.setText(_translate("Orange","Ingredients: Carrot and Orange"))
        self.label3.setText(_translate("Orange","Carrot and  Orange  juice  are  all  high in  Vitamin C,a  powerful"))                  
        self.label4.setText(_translate("Orange","anti-oxident that cleanses your cells of the free radicals that can"))     
        self.label5.setText(_translate("Orange","increase your risk of heart attack,stroke and certain type of cancer."))                                           
        self.label6.setText(_translate("Orange","Benifits:"))                                        
        self.label7.setText(_translate("Orange"," 1)  Prevents cataract and night blindness"))                                                                            
        self.label8.setText(_translate("Orange"," 2)  Cancer- fightining antioxident"))
        self.label9.setText(_translate("Orange"," 3)  Beta-caratene and vitamin A , supports healthy vision"))
        self.label10.setText(_translate("Orange"," 4)  Healthy Immune function"))
        self.label11.setText(_translate("Orange","Nutrition:"))
        self.label12.setText(_translate("Orange","Calories: 240 kcal/ fat 0gm / Sodium 20 mg / Carbohydrates 32 gm"))
        self.label13.setText(_translate("Orange","Sugar 30 gm /  Fiber 2 gm / Protien 0 gm / Calcium 60 mg"))
        self.label14.setText(_translate("Orange","Price:80/-"))
        self.label15.setText(_translate("Orange", " Hey!, How can I Help you?"))
        #**********************************************************************************#

    #*****************************************************#
    def LoadHelp(self):
        Help = QtWidgets.QMainWindow()
        ui = Ui_Help()
        ui.setupUi(Help)
        Help.show()
    #*****************************************************#
        
    #*****************************************************#
    def set_gif(self,gif_path):
        movie = QtGui.QMovie()
        movie.setFileName (gif_path)
        movie_label = QtWidgets.QLabel()
        movie_label.setMovie (movie)
        movie.start()
        return movie_label
    #*****************************************************#
              
    #*****************************************************#
    def LoadPayment_Gateway(self):
        Payment_Gateway = QtWidgets.QMainWindow()
        ui = Ui_Payment_Gateway()
        ui.setupUi(Payment_Gateway)
        Payment_Gateway.show()
    #*****************************************************#
    
########################################################################################################################################### WHEAT GRASS DETOX WINDOW
class Ui_Wheat_Grass_Detox(object):
    def setupUi(self, Wheat_Grass_Detox):
        Wheat_Grass_Detox.setObjectName("Wheat_Grass_Detox")
        Wheat_Grass_Detox.resize(1440, 870)
        self.centralWidget = QtWidgets.QWidget(Wheat_Grass_Detox)
        #START CODE FROM HERE---------------------------------------------------#
        
        self.centralWidget = self.set_gif("wheatgrass.gif")
        
        #PHOTOS SECTION----------------------------------------------------------#
        self.photo12 = QtWidgets.QLabel(self.centralWidget)
        self.photo12.setGeometry(QtCore.QRect(10, 0, 300, 150))
        self.photo12.setPixmap(QtGui.QPixmap("lerantalogo4.png"))
        self.photo1 = QtWidgets.QLabel(self.centralWidget)
        self.photo1.setGeometry(QtCore.QRect(50, 75, 550, 790))
        self.photo1.setPixmap(QtGui.QPixmap("wheat4.png"))
        #------------------------------------------------------------------------#
        
        #PUSHBUTTON SECTION------------------------------------------------------#
        self.pushButton2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton2.setGeometry(QtCore.QRect(580, 750, 170, 50))
        self.pushButton2.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton2.setFont(font)
        #-------------------------------------------------------------------------#
        
        #--------------------------------------------------------------------------#
        self.pushButton3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton3.setGeometry(QtCore.QRect(1200, 750, 190, 50))
        self.pushButton3.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton3.setFont(font)
        #--------------------------------------------------------------------------#
        
        #--------------------------------------------------------------------------#
        self.pushButton4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton4.setGeometry(QtCore.QRect(1340, 10, 100, 40))
        self.pushButton4.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        font = QtGui.QFont()
        font.setPointSize(25)
        self.pushButton4.setFont(font)
        #--------------------------------------------------------------------------#
        
       #LABELS HERE
        self.label1 = QtWidgets.QLabel(self.centralWidget)  
        self.label1.setGeometry(QtCore.QRect(580, 35, 795, 200))
        self.label1.setStyleSheet("color:rgb(255, 255, 153  )");
        font = QtGui.QFont('Comic Sans MS')
        font.setPointSize(70)
        self.label1.setFont(font)
        #--------------------------------------------------------------------------#
        
        #--------------------------------------------------------------------------#
        self.label2 = QtWidgets.QLabel(self.centralWidget)
        self.label2.setGeometry(QtCore.QRect(580, 100, 1400, 200))
        self.label2.setStyleSheet("color:rgb(233, 30, 99)");
        font = QtGui.QFont('bold')
        font.setPointSize(40)
        self.label2.setFont(font)
        #--------------------------------------------------------------------------#
        
       #--------------------------------------------------------------------------#
        self.label3 = QtWidgets.QLabel(self.centralWidget)
        self.label3.setGeometry(QtCore.QRect(580, 150, 1000, 200))
        self.label3.setStyleSheet("color:rgb(136, 14, 79)");
        font = QtGui.QFont('bold')
        font.setPointSize(35)
        self.label3.setFont(font)
        #--------------------------------------------------------------------------#
        
        #--------------------------------------------------------------------------#
        self.label4 = QtWidgets.QLabel(self.centralWidget)
        self.label4.setGeometry(QtCore.QRect(580, 200, 1000, 200))
        self.label4.setStyleSheet("color:rgb(0, 0, 51)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label4.setFont(font)
        #--------------------------------------------------------------------------#
        
        #--------------------------------------------------------------------------#
        self.label5 = QtWidgets.QLabel(self.centralWidget)
        self.label5.setGeometry(QtCore.QRect(580, 230, 1000, 200))
        self.label5.setStyleSheet("color:rgb(0, 0, 51)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label5.setFont(font)
        #--------------------------------------------------------------------------#
        
        #--------------------------------------------------------------------------#
        self.label6 = QtWidgets.QLabel(self.centralWidget)
        self.label6.setGeometry(QtCore.QRect(580, 260, 1400, 200))
        self.label6.setStyleSheet("color:rgb(0, 0, 51)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label6.setFont(font)
        #--------------------------------------------------------------------------#

        #--------------------------------------------------------------------------#
        self.label7 = QtWidgets.QLabel(self.centralWidget)
        self.label7.setGeometry(QtCore.QRect(580, 310, 1400, 200))
        self.label7.setStyleSheet("color:rgb(136, 14, 79)");
        font = QtGui.QFont('bold')
        font.setPointSize(35)
        self.label7.setFont(font)
        #--------------------------------------------------------------------------#

        #--------------------------------------------------------------------------#
        self.label8 = QtWidgets.QLabel(self.centralWidget)
        self.label8.setGeometry(QtCore.QRect(580, 360, 1400, 200))
        self.label8.setStyleSheet("color:rgb(0, 0, 51)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label8.setFont(font)
        #--------------------------------------------------------------------------#

        #--------------------------------------------------------------------------#
        self.label9 = QtWidgets.QLabel(self.centralWidget)
        self.label9.setGeometry(QtCore.QRect(580, 400, 1400, 200))
        self.label9.setStyleSheet("color:rgb(0, 0, 51)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label9.setFont(font)
        #--------------------------------------------------------------------------#

        #--------------------------------------------------------------------------#
        self.label10 = QtWidgets.QLabel(self.centralWidget)
        self.label10.setGeometry(QtCore.QRect(580, 440, 1400, 200))
        self.label10.setStyleSheet("color:rgb(0, 0, 51)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label10.setFont(font)
        #--------------------------------------------------------------------------#

        #--------------------------------------------------------------------------#
        self.label11 = QtWidgets.QLabel(self.centralWidget)
        self.label11.setGeometry(QtCore.QRect(580, 470, 1400, 200))
        self.label11.setStyleSheet("color:rgb(0, 0, 51)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label11.setFont(font)
        #--------------------------------------------------------------------------#

       #--------------------------------------------------------------------------#
        self.label12 = QtWidgets.QLabel(self.centralWidget)
        self.label12.setGeometry(QtCore.QRect(580, 530, 1400, 200))
        self.label12.setStyleSheet("color:red");
        font = QtGui.QFont('bold')
        font.setPointSize(40)
        self.label12.setFont(font)
        #--------------------------------------------------------------------------#

        #--------------------------------------------------------------------------#
        self.label13 = QtWidgets.QLabel(self.centralWidget)
        self.label13.setGeometry(QtCore.QRect(1090, 10, 250, 40))
        self.label13.setStyleSheet("color:rgb(255, 255, 255)");
        font = QtGui.QFont('Comic Sans MS')
        font.setPointSize(20)
        self.label13.setFont(font)
        #--------------------------------------------------------------------------#
    
        Wheat_Grass_Detox.setCentralWidget(self.centralWidget)
        self.retranslateUi(Wheat_Grass_Detox)
        QtCore.QMetaObject.connectSlotsByName(Wheat_Grass_Detox)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Wheat_Grass_Detox", "Wheat_Grass_Detox"))
        
        #*************************************************************************************************#
        self.pushButton2.setText(_translate("Wheat_Grass_Detox", "Pay Now"))
        self.pushButton3.setText(_translate("Wheat_Grass_Detox", "Back"))
        self.pushButton4.setText(_translate("Wheat_Grass_Detox", "help"))
        #*************************************************************************************************#
        
        #*************************************************************************************************#
        self.label1.setText(_translate("Wheat_Grass_Detox","WHEAT GRASS DETOX"))
        self.label2.setText(_translate("Wheat_Grass_Detox","Ingredients: wheat Grass, Orange and Apple."))
        self.label3.setText(_translate("Wheat_Grass_Detox","Benifits:" ))                  
        self.label4.setText(_translate("Wheat_Grass_Detox","1)  Wheat Grass containd daily recommended amount of Vitamins and Minerals"))     
        self.label5.setText(_translate("Wheat_Grass_Detox","2)  Helps to lowering Triglycerides & High cholestrol, Imoroves Immunity "))
        self.label6.setText(_translate("Wheat_Grass_Detox","       and overall health."))
        self.label7.setText(_translate("Wheat_Grass_Detox","Nutrition : "))                                        
        self.label8.setText(_translate("Wheat_Grass_Detox","Calories 180 kcl / Carbohydrates: 46 gm / Protien : 2 gm / Sodium: 3 mg"))                                        
        self.label9.setText(_translate("Wheat_Grass_Detox"," Potassium: 374 mg."))                                          
        self.label10.setText(_translate("Wheat_Grass_Detox","Fiber:6 gm / Sugar:35 gm / Vitamin A:195 U / Vitamin C :87.3 mg / Calcium:32 mg "))
        self.label11.setText(_translate("Wheat_Grass_Detox","Iron: 0.7 mg."))
        self.label12.setText(_translate("Wheat_Grass_Detox","Price:80/-"))
        self.label13.setText(_translate("Wheat_Grass_Detox","Hey!, How can I Help you?"))
        #*************************************************************************************************#
        
    #*************************************************************************************************#
    def LoadHelp(self):
        Help = QtWidgets.QMainWindow()
        ui = Ui_Help()
        ui.setupUi(Help)
        Help.show()
    #*************************************************************************************************#
        
    #*************************************************************************************************#                                               
    def set_gif(self,gif_path):
        movie = QtGui.QMovie()
        movie.setFileName (gif_path)
        movie_label = QtWidgets.QLabel()
        movie_label.setMovie (movie)
        movie.start()
        return movie_label
    #*************************************************************************************************#
    
    #*************************************************************************************************#
    def LoadPayment_Gateway(self):
        Payment_Gateway = QtWidgets.QMainWindow()
        ui = Ui_Payment_Gateway()
        ui.setupUi(Payment_Gateway)
        Payment_Gateway.show()
     #*************************************************************************************************#
        
########################################################################################################################################### APPLE BEET DETOX WINDOW
class Ui_Apple_Beet_Detox(object):
    def setupUi(self, Apple_Beet_Detox):
        Apple_Beet_Detox.setObjectName("Apple_Beet_Detox")
        Apple_Beet_Detox.resize(1440, 870)
        self.centralWidget = QtWidgets.QWidget(Apple_Beet_Detox)
        #START CODE FROM HERE----------------------------------------------------------------#
        
        self.centralWidget = self.set_gif("applebeet.gif")

        #PHOTOS SECTION---------------------------------------------------------------------#
        self.photo12 = QtWidgets.QLabel(self.centralWidget)
        self.photo12.setGeometry(QtCore.QRect(10, 0, 300, 150))
        self.photo12.setPixmap(QtGui.QPixmap("lerantalogo4.png"))
        self.photo1 = QtWidgets.QLabel(self.centralWidget)
        self.photo1.setGeometry(QtCore.QRect(50, 10, 550, 820))
        self.photo1.setPixmap(QtGui.QPixmap("appledetox8.png"))
        #-------------------------------------------------------------------------------------#
        
        #PUSHBUTTON SECTION--------------------------------------------------------------------#
        self.pushButton2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton2.setGeometry(QtCore.QRect(600, 750, 170, 50))
        self.pushButton2.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton2.setFont(font)
        #-------------------------------------------------------------------------------------#

        #-------------------------------------------------------------------------------------#
        self.pushButton3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton3.setGeometry(QtCore.QRect(1200, 750, 170, 50))
        self.pushButton3.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton3.setFont(font)
        #-------------------------------------------------------------------------------------#
        
        #-------------------------------------------------------------------------------------#
        self.pushButton8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton8.setGeometry(1330, 10, 100, 40)
        self.pushButton8.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        font = QtGui.QFont('DejaVu Serif')
        font.setPointSize(25)
        self.pushButton8.setFont(font)
        #-------------------------------------------------------------------------------------#
        
        #LABELS HERE---------------------------------------------------------------------------#
        self.label1 = QtWidgets.QLabel(self.centralWidget)
        self.label1.setGeometry(QtCore.QRect(600, 35, 795, 200))
        self.label1.setStyleSheet("color:rgb(244, 67, 54)");
        font = QtGui.QFont('Comic Sans MS')
        font.setPointSize(70)
        self.label1.setFont(font)
        #-------------------------------------------------------------------------------------#
        
        #---------------------------------------------------------#
        self.label2 = QtWidgets.QLabel(self.centralWidget)
        self.label2.setGeometry(QtCore.QRect(600, 100, 1400, 200))
        self.label2.setStyleSheet("color:rgb(78, 52, 46)");
        font = QtGui.QFont('bold')
        font.setPointSize(40)
        self.label2.setFont(font)
        #-------------------------------------------------------------------------------------#
        
        #---------------------------------------------------------#
        self.label3 = QtWidgets.QLabel(self.centralWidget)
        self.label3.setGeometry(QtCore.QRect(600, 150, 1000, 200))
        self.label3.setStyleSheet("color:rgb(0, 0, 0)");
        font = QtGui.QFont('bold')
        font.setPointSize(35)
        self.label3.setFont(font)
        #-------------------------------------------------------------------------------------#

        #---------------------------------------------------------#
        self.label4 = QtWidgets.QLabel(self.centralWidget)
        self.label4.setGeometry(QtCore.QRect(600, 200, 1000, 200))
        self.label4.setStyleSheet("color:rgb(0, 77, 64  )");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label4.setFont(font)
        #-------------------------------------------------------------------------------------#
        
        #---------------------------------------------------------#
        self.label5 = QtWidgets.QLabel(self.centralWidget)
        self.label5.setGeometry(QtCore.QRect(600, 240, 1000, 200))
        self.label5.setStyleSheet("color:rgb(0, 77, 64)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label5.setFont(font)
        #-------------------------------------------------------------------------------------#
        
        #---------------------------------------------------------#
        self.label6 = QtWidgets.QLabel(self.centralWidget)
        self.label6.setGeometry(QtCore.QRect(600, 280, 1400, 200))
        self.label6.setStyleSheet("color:rgb(0, 77, 64)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label6.setFont(font)
        #-------------------------------------------------------------------------------------#
        
        #---------------------------------------------------------#
        self.label7 = QtWidgets.QLabel(self.centralWidget)
        self.label7.setGeometry(QtCore.QRect(600, 310, 1400, 200))
        self.label7.setStyleSheet("color:rgb(0, 77, 64)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label7.setFont(font)
        #-------------------------------------------------------------------------------------#
        
        #---------------------------------------------------------#
        self.label8 = QtWidgets.QLabel(self.centralWidget)
        self.label8.setGeometry(QtCore.QRect(600, 350, 1400, 200))
        self.label8.setStyleSheet("color:rgb(0, 77, 64)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label8.setFont(font)
        #-------------------------------------------------------------------------------------#
        
        #---------------------------------------------------------#
        self.label9 = QtWidgets.QLabel(self.centralWidget)
        self.label9.setGeometry(QtCore.QRect(600, 390, 1400, 200))
        self.label9.setStyleSheet("color:rgb(0,0,0)");
        font = QtGui.QFont('bold')
        font.setPointSize(35)
        self.label9.setFont(font)
        #-------------------------------------------------------------------------------------#
        
        #---------------------------------------------------------#
        self.label10 = QtWidgets.QLabel(self.centralWidget)
        self.label10.setGeometry(QtCore.QRect(600, 430, 1400, 200))
        self.label10.setStyleSheet("color:rgb(0, 77, 64)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label10.setFont(font)
        #-------------------------------------------------------------------------------------#

        #---------------------------------------------------------#
        self.label11 = QtWidgets.QLabel(self.centralWidget)
        self.label11.setGeometry(QtCore.QRect(600, 470, 1400, 200))
        self.label11.setStyleSheet("color:rgb(0, 77, 64)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label11.setFont(font)
        #-------------------------------------------------------------------------------------#
        
        #---------------------------------------------------------#
        self.label12 = QtWidgets.QLabel(self.centralWidget)
        self.label12.setGeometry(QtCore.QRect(600, 530, 1400, 200))
        self.label12.setStyleSheet("color:rgb(255, 0, 40)");
        font = QtGui.QFont('bold')
        font.setPointSize(40)
        self.label12.setFont(font)
        #-------------------------------------------------------------------------------------#
        
        #---------------------------------------------------------#
        self.label13 = QtWidgets.QLabel(self.centralWidget)
        self.label13.setGeometry(QtCore.QRect(1088, 10, 250, 40))
        self.label13.setStyleSheet("color:rgb(51, 0, 102)");
        font = QtGui.QFont('Comic Sans MS')
        font.setPointSize(20)
        self.label13.setFont(font)
        #-------------------------------------------------------------------------------------#
        
        Apple_Beet_Detox.setCentralWidget(self.centralWidget)
        self.retranslateUi(Apple_Beet_Detox)
        QtCore.QMetaObject.connectSlotsByName(Apple_Beet_Detox)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Apple_Beet_Detox", "Apple_Beet_Detox"))
        
        #**************************************************************************************#
        self.pushButton2.setText(_translate("Apple_Beet_Detox", "Pay Now"))
        self.pushButton3.setText(_translate("Apple_Beet_Detox", "Back"))
        self.pushButton8.setText(_translate("Apple_Beet_Detox", "help"))
        #**************************************************************************************#

        #**************************************************************************************#
        self.label1.setText(_translate("Apple_Beet_Detox","APPLE BEET DETOX"))
        self.label2.setText(_translate("Apple_Beet_Detox","Ingredients:Apple, Beatroot, Ginger and Lemon."))
        self.label3.setText(_translate("Apple_Beet_Detox","Benifits:" ))                  
        self.label4.setText(_translate("Apple_Beet_Detox","1) Improve blood flow, Reduce blood pleasure."  ))     
        self.label5.setText(_translate("Apple_Beet_Detox","2) Detoxifies the liver, good for Muscles"))                                           
        self.label6.setText(_translate("Apple_Beet_Detox","3) Helps with IronDifecency and Anemia"))                                        
        self.label7.setText(_translate("Apple_Beet_Detox","4) Treats Inflamation, Alkalising"))                                        
        self.label8.setText(_translate("Apple_Beet_Detox","5) Poly phenols offers more Antioxidents and helps to Regulate Blood Sugar."))
        self.label9.setText(_translate("Apple_Beet_Detox","Nutrition:"))
        self.label10.setText(_translate("Apple_Beet_Detox","Calaries: 257 Kcal,Sodim: 209mg, Potassium: 917mg,Carbohydrates: 43gm."))
        self.label11.setText(_translate("Apple_Beet_Detox","Sugar: 30g/ Protien: 3g/ Vitamin A: 21400 IU/ Vitamin C: 141.1mg")) 
        self.label12.setText(_translate("Apple_Beet_Detox","Price:80/-"))
        self.label13.setText(_translate("Wheat_Grass_Detox","Hey!, How can I Help you?"))
        #**************************************************************************************#

        
    #**************************************************************************************#
    def LoadHelp(self):
        Help = QtWidgets.QMainWindow()
        ui = Ui_Help()
        ui.setupUi(Help)
        Help.show()
    #**************************************************************************************#

    #**************************************************************************************#    
    def set_gif(self,gif_path):
        movie = QtGui.QMovie()
        movie.setFileName (gif_path)
        movie_label = QtWidgets.QLabel()
        movie_label.setMovie (movie)
        movie.start()
        return movie_label
     #**************************************************************************************#
    
    #**************************************************************************************#
    def LoadPayment_Gateway(self):
        Payment_Gateway = QtWidgets.QMainWindow()
        ui = Ui_Payment_Gateway()
        ui.setupUi(Payment_Gateway)
        Payment_Gateway.show()
    #**************************************************************************************#
    
########################################################################################################################################### SWEET SPINACH DETOX WINDOW
class Ui_Sweet_Spinach_Detox(object):
    def setupUi(self, Sweet_Spinach_Detox):
        Sweet_Spinach_Detox.setObjectName("Sweet_Spinach_Detox")
        Sweet_Spinach_Detox.resize(1440, 870)
        self.centralWidget = QtWidgets.QWidget(Sweet_Spinach_Detox)
        #START CODE FROM HERE----------------------------------------------------#
        
        self.centralWidget = self.set_gif("spinach.gif")

        #PHOTOS SECTION----------------------------------------------------------#
        self.photo12 = QtWidgets.QLabel(self.centralWidget)
        self.photo12.setGeometry(QtCore.QRect(10, 0, 300, 150))
        self.photo12.setPixmap(QtGui.QPixmap("lerantalogo4.png"))
        self.photo1 = QtWidgets.QLabel(self.centralWidget)
        self.photo1.setGeometry(QtCore.QRect(100, 30, 550, 800))
        self.photo1.setPixmap(QtGui.QPixmap("sweet14.png"))
        #------------------------------------------------------------------------#
        
        #PUSHBUTTON SECTION-------------------------------------------------------#
        self.pushButton2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton2.setGeometry(QtCore.QRect(550, 750, 170, 50))
        self.pushButton2.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton2.setFont(font)
        #------------------------------------------------------------------------#

        #-------------------------------------------------------------------------#
        self.pushButton3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton3.setGeometry(QtCore.QRect(1200, 750, 170, 50))
        self.pushButton3.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton3.setFont(font)
        #------------------------------------------------------------------------#
        
        #------------------------------------------------------------------------#
        self.pushButton9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton9.setGeometry(1330, 10, 100, 40)
        self.pushButton9.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        font = QtGui.QFont('DejaVu Serif')
        font.setPointSize(25)
        self.pushButton9.setFont(font)
        #--------------------------------------------------------------------------#
        
        #LABELS HERE--------------------------------------------------------------#
        self.label1 = QtWidgets.QLabel(self.centralWidget)
        self.label1.setGeometry(QtCore.QRect(550, 40, 900, 200))
        self.label1.setStyleSheet("color:rgb(0, 121, 107 )");
        font = QtGui.QFont('Comic Sans MS')
        font.setPointSize(70)
        self.label1.setFont(font)
        #-------------------------------------------------------------------------#
        
        #------------------------------------------------------------#
        self.label2 = QtWidgets.QLabel(self.centralWidget)
        self.label2.setGeometry(QtCore.QRect(550, 100, 1400, 200))
        self.label2.setStyleSheet("color:rgb(204, 51, 102)");
        font = QtGui.QFont('bold')
        font.setPointSize(40)
        self.label2.setFont(font)
        #-------------------------------------------------------------------------#
        
        #------------------------------------------------------------#
        self.label3 = QtWidgets.QLabel(self.centralWidget)
        self.label3.setGeometry(QtCore.QRect(550, 150, 1000, 200))
        self.label3.setStyleSheet("color:rgb(224, 247, 250)");
        font = QtGui.QFont('bold')
        font.setPointSize(35)
        self.label3.setFont(font)
        #-------------------------------------------------------------------------#
        
        #------------------------------------------------------------#
        self.label4 = QtWidgets.QLabel(self.centralWidget)
        self.label4.setGeometry(QtCore.QRect(550, 200, 1000, 200))
        self.label4.setStyleSheet("color:rgb(255, 235, 59)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label4.setFont(font)
        #-------------------------------------------------------------------------#
        
        #------------------------------------------------------------#
        self.label5 = QtWidgets.QLabel(self.centralWidget)
        self.label5.setGeometry(QtCore.QRect(550, 240, 1000, 200))
        self.label5.setStyleSheet("color:rgb(255, 235, 59)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label5.setFont(font)
        #-------------------------------------------------------------------------#
        
        #------------------------------------------------------------#
        self.label6 = QtWidgets.QLabel(self.centralWidget)
        self.label6.setGeometry(QtCore.QRect(550, 280, 1400, 200))
        self.label6.setStyleSheet("color:rgb(255, 235, 59)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label6.setFont(font)
        #-------------------------------------------------------------------------#
        
        #------------------------------------------------------------#
        self.label7 = QtWidgets.QLabel(self.centralWidget)
        self.label7.setGeometry(QtCore.QRect(550, 330, 1400, 200))
        self.label7.setStyleSheet("color:rgb(224, 247, 250)");
        font = QtGui.QFont('bold')
        font.setPointSize(35)
        self.label7.setFont(font)
        #-------------------------------------------------------------------------#
        
        #------------------------------------------------------------#
        self.label8 = QtWidgets.QLabel(self.centralWidget)
        self.label8.setGeometry(QtCore.QRect(550, 370, 1400, 200))
        self.label8.setStyleSheet("color:rgb(255, 235, 59)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label8.setFont(font)
        #-------------------------------------------------------------------------#
        
        #------------------------------------------------------------#
        self.label9 = QtWidgets.QLabel(self.centralWidget)
        self.label9.setGeometry(QtCore.QRect(550, 410, 1400, 200))
        self.label9.setStyleSheet("color:rgb(255, 235, 59)");
        font = QtGui.QFont('bold')
        font.setPointSize(25)
        self.label9.setFont(font)
        #-------------------------------------------------------------------------#
        
        #------------------------------------------------------------#
        self.label10 = QtWidgets.QLabel(self.centralWidget)
        self.label10.setGeometry(QtCore.QRect(550, 480, 1400, 200))
        self.label10.setStyleSheet("color:rgb(255, 51, 0)");
        font = QtGui.QFont('bold')
        font.setPointSize(40)
        self.label10.setFont(font)
        #-------------------------------------------------------------------------#
        
        #------------------------------------------------------------#
        self.label11 = QtWidgets.QLabel(self.centralWidget)
        self.label11.setGeometry(QtCore.QRect(1088, 10, 250, 40))
        self.label11.setStyleSheet("color:rgb(51, 0, 102)");
        font = QtGui.QFont('Comic Sans MS')
        font.setPointSize(20)
        self.label11.setFont(font)
        #-------------------------------------------------------------------------#
        
        Sweet_Spinach_Detox.setCentralWidget(self.centralWidget)
        self.retranslateUi(Sweet_Spinach_Detox)
        QtCore.QMetaObject.connectSlotsByName(Sweet_Spinach_Detox)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Sweet_Spinach_Detox", "Sweet_Spinach_Detox"))
        
        #*************************************************************************#
        self.pushButton2.setText(_translate("Sweet_Spinach_Detox", "Pay Now"))
        self.pushButton3.setText(_translate("Sweet_Spinach_Detox", "Back"))
        self.pushButton9.setText(_translate("Sweet_Spinach_Detox", "Back"))
        #*************************************************************************#
        
        #*****************************************************************************************#
        self.label1.setText(_translate("Sweet_Spinach_Detox","SWEET SPINACH DETOX"))
        self.label2.setText(_translate("Sweet_Spinach_Detox","Ingredients: Apple, Pineapple and Spinach."))
        self.label3.setText(_translate("Sweet_Spinach_Detox","Benifits:" ))                  
        self.label4.setText(_translate("Sweet_Spinach_Detox","1) Pineapple increse your Appetite and speeds your Digestion."))     
        self.label5.setText(_translate("Sweet_Spinach_Detox","2) It contains Caroten which demonstrate Anti cancer effect"))
        self.label6.setText(_translate("Sweet_Spinach_Detox","3) Strengthen Immune system and protect your skin."))
        self.label7.setText(_translate("Sweet_Spinach_Detox","Nutrition : " ))                                        
        self.label8.setText(_translate("Sweet_Spinach_Detox","Calories: 177 kcal/ Protien: 2 gm/ Carbohydrates: 38.5gm/"))                                                                             
        self.label9.setText(_translate("Sweet_Spinach_Detox","Fiber: 11.1 gm/ Fat: 1.3 gm/ Cholestrol @0 mg"))
        self.label10.setText(_translate("Sweet_Spinach_Detox","Price:80/-"))
        self.label11.setText(_translate("Wheat_Grass_Detox","Hey!, How can I Help you?"))
        #*****************************************************************************************#

    #*************************************************************************#
    def LoadHelp(self):
        Help = QtWidgets.QMainWindow()
        ui = Ui_Help()
        ui.setupUi(Help)
        Help.show()
    #*************************************************************************#
        
    #*************************************************************************#   
    def set_gif(self,gif_path):
        movie = QtGui.QMovie()
        movie.setFileName (gif_path)
        movie_label = QtWidgets.QLabel()
        movie_label.setMovie (movie)
        movie.start()
        return movie_label
    #*************************************************************************#
    
    #*************************************************************************#
    def LoadPayment_Gateway(self):
        Payment_Gateway = QtWidgets.QMainWindow()
        ui = Ui_Payment_Gateway()
        ui.setupUi(Payment_Gateway)
        Payment_Gateway.show()
    #*************************************************************************#

######################################################################################################################################################### HELP WINDOW
class Ui_Help(object):
    def setupUi(self, Help):
        Help.setObjectName("Help")
        Help.resize(1440, 870)
        self.centralWidget = QtWidgets.QWidget(Help)
        #START CODE FROM HERE------------------------------------------------------#
        self.photo12 = QtWidgets.QLabel(self.centralWidget)
        self.photo12.setGeometry(QtCore.QRect(10, 0, 300, 150))
        self.photo12.setPixmap(QtGui.QPixmap("lerantalogo4.png"))
   
        #PUSHBUTTON SECTION--------------------------------------------------------#
        self.pushButton7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton7.setGeometry(QtCore.QRect(650, 800, 170, 50))
        self.pushButton7.setStyleSheet(" QPushButton"
                             "{"
                             "background-color : green; border-radius:20px; color:white; border-style: outset; border-width: 6px; border-color: orange"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : orange;"
                             "}");
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton7.setFont(font)
        #---------------------------------------------------------------------------#

        Help.setCentralWidget(self.centralWidget)
        self.retranslateUi(Help)
        QtCore.QMetaObject.connectSlotsByName(Help)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Help", "Help"))
        
        #***********************************************************************#
        self.pushButton7.setText(_translate("Help", "Continue"))
        #***********************************************************************#

    
############################################################################################################################################## PAYMENTGATEWAY WINDOW        
class Ui_Payment_Gateway(object):  
    def setupUi(self, Payment_Gateway):
        Payment_Gateway.resize(1440, 870)
        self.centralWidget = QtWidgets.QWidget(Payment_Gateway)

        self.centralWidget = self.set_gif("timer2.gif")
        self.centralWidget.setAlignment(Qt.AlignRight)

        self.Payment_Gateway = QWebEngineView(self.centralWidget)
        self.Payment_Gateway.resize(1200, 800)
        self.Payment_Gateway.setGeometry(QtCore.QRect(80, 60, 1290, 860))
        self.Payment_Gateway.load(QUrl("http://127.0.0.1:8000/payment"))
      
        self.label1 = QtWidgets.QLabel(self.centralWidget)
        self.label1.setGeometry(QtCore.QRect(1250, 0, 1250, 50))
        self.label1.setStyleSheet("color:rgb(255,0,0)");
        font = QtGui.QFont('bold')
        font.setPointSize(20)
        self.label1.setFont(font)

        self.label2 = QtWidgets.QLabel(self.centralWidget)
        self.label2.setGeometry(QtCore.QRect(580, 9, 1230, 50))
        self.label2.setStyleSheet("color:rgb(205,100,0)");
        font = QtGui.QFont('Arial Black')
        font.setPointSize(35)
        self.label2.setFont(font)

        self.label = QtWidgets.QLabel(self.centralWidget)
        #self.label.setWindowTitle('Single shot')
        #self.label.setText('This window will close after 3 seconds.')
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignCenter)

        QtCore.QTimer.singleShot(35000, Payment_Gateway.close)
        
        #Payment_Gateway.setStyleSheet("background-color : green")
        Payment_Gateway.setCentralWidget(self.centralWidget)
        self.retranslateUi(Payment_Gateway)
        QtCore.QMetaObject.connectSlotsByName(Payment_Gateway)  
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Payment_Gateway", "Payment_Gateway"))
        self.label1.setText(_translate("Payment_Gateway","Time Remaining:"))
        self.label2.setText(_translate("Payment_Gateway","Leranta Billing"))

        #QtCore.QTimer.singleShot(4000, Welcome.open)
        
    def set_gif(self,gif_path):
        movie = QtGui.QMovie()
        movie.setFileName (gif_path)
        movie_label = QtWidgets.QLabel()
        movie_label.setMovie (movie)
        movie.start()
        return movie_label

        
######################################################################################################################################### ALL WINDOWS CONTROLER        
class Controller:

    def __init__(self):
        pass
    
    #WELCOME WINDOW----------------------------------------------------------#
    def Show_Welcome(self):
        self.Welcome = QtWidgets.QMainWindow()
        self.ui = Ui_Welcome()
        self.ui.setupUi(self.Welcome)
        self.ui.pushButton0.clicked.connect(self.Show_Juices)
        #self.ui.pushButton0.clicked.connect(self.hide_Welcome)
        
        self.Welcome.show()

##    def hide_Welcome(self):
##        self.Window = QtWidgets.QMainWindow()
##        self.ui = Ui_Welcome()
##        self.ui.setupUi(self.Welcome)
##        self.Welcome.hide()
    #-------------------------------------------------------------------------#
        
    #JUICESES WINDOW----------------------------------------------------------#
    def Show_Juices(self):
        self.Juices = QtWidgets.QMainWindow()
        self.ui = Ui_Juices()
        self.ui.setupUi(self.Juices)
        
        self.ui.pushButton1.clicked.connect(self.Show_Orange)
        self.ui.pushButton1.clicked.connect(self.hide_Juices)
        self.ui.pushButton2.clicked.connect(self.Show_Wheat_Grass_Detox)
        self.ui.pushButton2.clicked.connect(self.hide_Juices)
        self.ui.pushButton3.clicked.connect(self.Show_Apple_Beet_Detox)
        self.ui.pushButton3.clicked.connect(self.hide_Juices)
        self.ui.pushButton4.clicked.connect(self.Show_Sweet_Spinach_Detox)
        self.ui.pushButton4.clicked.connect(self.hide_Juices)
        self.ui.pushButton6.clicked.connect(self.Show_Help)
        self.ui.pushButton6.clicked.connect(self.hide_Juices)

        self.Juices.show()
        
    def hide_Juices(self):
        self.Juices = QtWidgets.QMainWindow()
        self.ui = Ui_Juices()
        self.ui.setupUi(self.Juices)
        self.Juices.hide()
    #-------------------------------------------------------------------------#
      
    #ORANGE HANG WINDOW--------------------------------------------------------#
    def Show_Orange(self):
        self.Orange = QtWidgets.QMainWindow()
        self.ui = Ui_Orange()
        self.ui.setupUi(self.Orange)
        
        self.ui.pushButton3.clicked.connect(self.Show_Juices)
        self.ui.pushButton2.clicked.connect(self.Show_Payment_Gateway)
        self.ui.pushButton3.clicked.connect(self.hide_Orange)
        self.ui.pushButton2.clicked.connect(self.hide_Orange)
        self.ui.pushButton7.clicked.connect(self.Show_Help)
        self.ui.pushButton7.clicked.connect(self.hide_Juices)

        self.Orange.show()
       
    def hide_Orange(self):
        
        self.Orange = QtWidgets.QMainWindow()
        self.ui = Ui_Orange()
        self.ui.setupUi(self.Orange)
        self.Orange.hide()
    #-------------------------------------------------------------------------#
        
    #WHEAT GRASS DETOX WINDOW--------------------------------------------------#
    def Show_Wheat_Grass_Detox(self):
        self.Wheat_Grass_Detox = QtWidgets.QMainWindow()
        self.ui = Ui_Wheat_Grass_Detox()
        self.ui.setupUi(self.Wheat_Grass_Detox)
        
        self.ui.pushButton3.clicked.connect(self.Show_Juices)
        self.ui.pushButton2.clicked.connect(self.Show_Payment_Gateway)
        self.ui.pushButton3.clicked.connect(self.hide_Wheat_Grass_Detox)
        self.ui.pushButton2.clicked.connect(self.hide_Wheat_Grass_Detox)
        self.ui.pushButton4.clicked.connect(self.Show_Help)
        self.ui.pushButton4.clicked.connect(self.hide_Wheat_Grass_Detox)
        
        self.Wheat_Grass_Detox.show()

    def hide_Wheat_Grass_Detox(self):
        self.Wheat_Grass_Detox = QtWidgets.QMainWindow()
        self.ui = Ui_Wheat_Grass_Detox()
        self.ui.setupUi(self.Wheat_Grass_Detox)
        self.Wheat_Grass_Detox.hide()
    #-------------------------------------------------------------------------#
        
    #APPLE BEET DETOX WINDOW--------------------------------------------------#
    def Show_Apple_Beet_Detox(self):
        self.Apple_Beet_Detox = QtWidgets.QMainWindow()
        self.ui = Ui_Apple_Beet_Detox()
        self.ui.setupUi(self.Apple_Beet_Detox)
        
        self.ui.pushButton3.clicked.connect(self.Show_Juices)
        self.ui.pushButton2.clicked.connect(self.Show_Payment_Gateway)
        self.ui.pushButton3.clicked.connect(self.hide_Apple_Beet_Detox)
        self.ui.pushButton2.clicked.connect(self.hide_Apple_Beet_Detox)
        self.ui.pushButton8.clicked.connect(self.Show_Help)
        self.ui.pushButton8.clicked.connect(self.hide_Apple_Beet_Detox)
        
        self.Apple_Beet_Detox.show()

    def hide_Apple_Beet_Detox(self):
        self.Apple_Beet_Detox = QtWidgets.QMainWindow()
        self.ui = Ui_Apple_Beet_Detox()
        self.ui.setupUi(self.Apple_Beet_Detox)
        self.Apple_Beet_Detox.hide()
    #-------------------------------------------------------------------------#
        
    #SWEET SPINACH DETOX WINDOW-----------------------------------------------#
    def Show_Sweet_Spinach_Detox(self):
        self.Sweet_Spinach_Detox = QtWidgets.QMainWindow()
        self.ui = Ui_Sweet_Spinach_Detox()
        self.ui.setupUi(self.Sweet_Spinach_Detox)
        
        self.ui.pushButton3.clicked.connect(self.Show_Juices)
        self.ui.pushButton2.clicked.connect(self.Show_Payment_Gateway)
        self.ui.pushButton3.clicked.connect(self.hide_Sweet_Spinach_Detox)
        self.ui.pushButton2.clicked.connect(self.hide_Sweet_Spinach_Detox)
        self.ui.pushButton9.clicked.connect(self.Show_Help)
        self.ui.pushButton9.clicked.connect(self.hide_Sweet_Spinach_Detox)
        
        self.Sweet_Spinach_Detox.show()  

    def hide_Sweet_Spinach_Detox(self):
        self.Sweet_Spinach_Detox = QtWidgets.QMainWindow()
        self.ui = Ui_Sweet_Spinach_Detox()
        self.ui.setupUi(self.Sweet_Spinach_Detox)
        self.Sweet_Spinach_Detox.hide()
    #-------------------------------------------------------------------------#
        
    #HELP WINDOW--------------------------------------------------------------#
    def Show_Help(self):
        self.Help = QtWidgets.QMainWindow()
        self.ui = Ui_Help()
        self.ui.setupUi(self.Help)
        
        self.ui.pushButton7.clicked.connect(self.Show_Juices)
        self.ui.pushButton7.clicked.connect(self.hide_Help)
       
        self.Help.show()

    def hide_Help(self):
        self.Help = QtWidgets.QMainWindow()
        self.ui = Ui_Help()
        self.ui.setupUi(self.Help)
        self.Help.hide()
    #-------------------------------------------------------------------------#
        
    #PAYMENT GATEWAY WINDOW---------------------------------------------------#
    def Show_Payment_Gateway(self):
        
        self.Payment_Gateway = QtWidgets.QMainWindow()
        self.ui = Ui_Payment_Gateway()
        self.ui.setupUi(self.Payment_Gateway)
        self.Payment_Gateway.show()
        
##        self.Welcome.show()


##        self.Welcome = QtWidgets.QMainWindow()
##        self.ui = Ui_Welcome()
##        self.ui.setupUi(self.Welcome)
##        self.ui.pushButton.clicked.connect(self.Show_Juices)
##        self.ui.pushButton.clicked.connect(self.hide_Welcome)
##       
##
##        self.Welcome.show()
    #-------------------------------------------------------------------------#



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()
    Controller.Show_Welcome()
    sys.exit(app.exec_())

