from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QMovie,QPixmap
from PyQt5.QtWidgets import QLCDNumber,QVBoxLayout
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 800)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Siri"))
        MainWindow.setWindowIcon(QIcon("icon/phone.png"))

        #麦克风图片
        self.phoneFig = QtWidgets.QLabel(self.centralwidget)
        self.phoneFig.setGeometry(QtCore.QRect(125, 100, 250, 250))
        self.phoneFig.setPixmap(QPixmap("icon/audio.png"))
        self.phoneFig.setScaledContents(True)
        self.phoneFig.setObjectName("phoneFig")

        #语音识别图片
        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(50, 100, 400, 300))
        self.voiceFig.setText("")
        self.gif = QMovie("icon/voice.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")


        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)

        #提示Hey Siri
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText(_translate("MainWindow", "Speak 'Hey Siri' to wake me"))
        self.label.setGeometry(QtCore.QRect(50, 400, 400, 50))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        #提示How Can I help you
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setText(_translate("MainWindow", "How can I help you?"))
        self.label1.setGeometry(QtCore.QRect(50, 400, 400, 50))
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setFont(font)
        self.label1.setStyleSheet("color: rgb(0, 117, 210);")
        self.label1.setTextFormat(QtCore.Qt.AutoText)
        self.label1.setWordWrap(True)
        self.label1.setObjectName("label1")

        self.label11 = QtWidgets.QLabel(self.centralwidget)
        self.label11.setText(_translate("MainWindow", "You can:"))
        self.label11.setGeometry(QtCore.QRect(75, 450, 400, 50))
        self.label11.setFont(font)
        self.label11.setStyleSheet("color: rgb(0, 117, 210);")
        self.label11.setTextFormat(QtCore.Qt.AutoText)
        self.label11.setWordWrap(True)
        self.label11.setObjectName("label11")

        font.setPointSize(12)
        self.label12 = QtWidgets.QLabel(self.centralwidget)
        self.label12.setText(_translate("MainWindow", "1.Enjoy music by saying 'Music'."))
        self.label12.setGeometry(QtCore.QRect(90, 500, 400, 50))
        self.label12.setFont(font)
        self.label12.setStyleSheet("color: rgba(255, 255, 255 , 0.8);")
        self.label12.setTextFormat(QtCore.Qt.AutoText)
        self.label12.setWordWrap(True)
        self.label12.setObjectName("label12")
        self.label13 = QtWidgets.QLabel(self.centralwidget)
        self.label13.setText(_translate("MainWindow", "2.Take some notes by saying 'Notepad'."))
        self.label13.setGeometry(QtCore.QRect(90, 550, 350, 60))
        self.label13.setFont(font)
        self.label13.setStyleSheet("color: rgba(255, 255, 255 ,0.8);")
        self.label13.setTextFormat(QtCore.Qt.AutoText)
        self.label13.setWordWrap(True)
        self.label13.setObjectName("label13")
        self.label14 = QtWidgets.QLabel(self.centralwidget)
        self.label14.setText(_translate("MainWindow", "3.See the current time by saying 'Time'."))
        self.label14.setGeometry(QtCore.QRect(90, 610, 350, 60))
        self.label14.setFont(font)
        self.label14.setStyleSheet("color: rgba(255, 255, 255 ,0.8);")
        self.label14.setTextFormat(QtCore.Qt.AutoText)
        self.label14.setWordWrap(True)
        self.label14.setObjectName("label14")
        self.label15 = QtWidgets.QLabel(self.centralwidget)
        self.label15.setText(_translate("MainWindow", "4.View weather forecast by saying 'Weather'."))
        self.label15.setGeometry(QtCore.QRect(90, 670, 350, 60))
        self.label15.setFont(font)
        self.label15.setStyleSheet("color: rgba(255, 255, 255 ,0.8);")
        self.label15.setTextFormat(QtCore.Qt.AutoText)
        self.label15.setWordWrap(True)
        self.label15.setObjectName("label15")
    
        font.setPointSize(16)
        #读取语音内容失败
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setText(_translate("MainWindow", "Sorry, I can't hear you!"))
        self.label2.setGeometry(QtCore.QRect(50, 400, 400, 50))
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setFont(font)
        self.label2.setStyleSheet("color: rgb(0, 117, 210);")
        self.label2.setTextFormat(QtCore.Qt.AutoText)
        self.label2.setWordWrap(True)
        self.label2.setObjectName("label2")

        #语音识别成功
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(50, 400, 400, 50))
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setFont(font)
        self.label3.setStyleSheet("color: rgb(0, 117, 210);")
        self.label3.setTextFormat(QtCore.Qt.AutoText)
        self.label3.setWordWrap(True)
        self.label3.setObjectName("label3")

        #天气
        self.weather_label = QtWidgets.QLabel(self.centralwidget)
        self.weather_label.setText(_translate("MainWindow", "The weather today is:"))
        self.weather_label.setGeometry(QtCore.QRect(50, 450, 400, 50))
        self.weather_label.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_label.setFont(font)
        self.weather_label.setStyleSheet("color: rgba(255, 255, 255 , 0.8);")
        self.weather_label.setTextFormat(QtCore.Qt.AutoText)
        self.weather_label.setWordWrap(True)
        self.weather_label.setObjectName("weather_label")
        font.setPointSize(12)
        self.weather_label1 = QtWidgets.QLabel(self.centralwidget)
        self.weather_label1.setText(_translate("MainWindow", "Date："))
        self.weather_label1.setGeometry(QtCore.QRect(150, 500, 200, 50))
        self.weather_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_label1.setFont(font)
        self.weather_label1.setStyleSheet("color: rgba(255, 255, 255 , 0.8);")
        self.weather_label1.setTextFormat(QtCore.Qt.AutoText)
        self.weather_label1.setWordWrap(True)
        self.weather_label1.setObjectName("weather_label1")
        self.weather_label2 = QtWidgets.QLabel(self.centralwidget)
        self.weather_label2.setText(_translate("MainWindow", "Type："))
        self.weather_label2.setGeometry(QtCore.QRect(150, 550, 200, 50))
        self.weather_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_label2.setFont(font)
        self.weather_label2.setStyleSheet("color: rgba(255, 255, 255 , 0.8);")
        self.weather_label2.setTextFormat(QtCore.Qt.AutoText)
        self.weather_label2.setWordWrap(True)
        self.weather_label2.setObjectName("weather_labe2")
        self.weather_label3 = QtWidgets.QLabel(self.centralwidget)
        self.weather_label3.setText(_translate("MainWindow", "Low："))
        self.weather_label3.setGeometry(QtCore.QRect(150, 600, 200, 50))
        self.weather_label3.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_label3.setFont(font)
        self.weather_label3.setStyleSheet("color: rgba(255, 255, 255 , 0.8);")
        self.weather_label3.setTextFormat(QtCore.Qt.AutoText)
        self.weather_label3.setWordWrap(True)
        self.weather_label3.setObjectName("weather_labe3")
        self.weather_label4 = QtWidgets.QLabel(self.centralwidget)
        self.weather_label4.setText(_translate("MainWindow", "High："))
        self.weather_label4.setGeometry(QtCore.QRect(150, 650, 200, 50))
        self.weather_label4.setAlignment(QtCore.Qt.AlignCenter)
        self.weather_label4.setFont(font)
        self.weather_label4.setStyleSheet("color: rgba(255, 255, 255 , 0.8);")
        self.weather_label4.setTextFormat(QtCore.Qt.AutoText)
        self.weather_label4.setWordWrap(True)
        self.weather_label4.setObjectName("weather_labe4")

        #时钟
        font.setPointSize(32)
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(50, 550, 400, 50))
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setFont(font)
        self.label_time.setStyleSheet("color: rgba(255,255,255,0.6);")
        self.label_time.setTextFormat(QtCore.Qt.AutoText)
        self.label_time.setWordWrap(True)
        self.label_time.setObjectName("label_time")

        #定时器
        self.timer=QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.update_time)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.startUI()
    
    def update_time(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_time.setText(_translate("MainWindow",time.strftime('%X', time.localtime())))
    
    #开始界面
    def startUI(self):
        self.phoneFig.setVisible(True)
        self.voiceFig.setVisible(False)
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Hey, I'm Siri. I'm here."))
        self.label.setVisible(True)
        self.label1.setVisible(False)
        self.label2.setVisible(False)
        self.label3.setVisible(False)

        self.label11.setVisible(False)
        self.label12.setVisible(False)
        self.label13.setVisible(False)
        self.label14.setVisible(False)
        self.label15.setVisible(False)

        self.weather_label.setVisible(False)
        self.weather_label1.setVisible(False)
        self.weather_label2.setVisible(False)
        self.weather_label3.setVisible(False)
        self.weather_label4.setVisible(False)

        self.label_time.setVisible(False)

    #主界面
    def mainUI(self):
        self.phoneFig.setVisible(False)
        self.voiceFig.setVisible(True)
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Speak 'Hey Siri' to wake me."))
        self.label.setVisible(True)
        self.label1.setVisible(False)
        self.label2.setVisible(False)
        self.label3.setVisible(False)

        self.label11.setVisible(False)
        self.label12.setVisible(False)
        self.label13.setVisible(False)
        self.label14.setVisible(False)
        self.label15.setVisible(False)

        self.weather_label.setVisible(False)
        self.weather_label1.setVisible(False)
        self.weather_label2.setVisible(False)
        self.weather_label3.setVisible(False)
        self.weather_label4.setVisible(False)

        self.label_time.setVisible(False)

    #唤醒界面
    def asrUI(self):
        self.phoneFig.setVisible(False)
        self.voiceFig.setVisible(True)
        self.label.setVisible(False)
        self.label1.setVisible(True)
        self.label2.setVisible(False)
        self.label3.setVisible(False)

        self.label11.setVisible(True)
        self.label12.setVisible(True)
        self.label13.setVisible(True)
        self.label14.setVisible(True)
        self.label15.setVisible(True)

        self.weather_label.setVisible(False)
        self.weather_label1.setVisible(False)
        self.weather_label2.setVisible(False)
        self.weather_label3.setVisible(False)
        self.weather_label4.setVisible(False)

        self.label_time.setVisible(False)
        
    #识别失败界面
    def recFailUI(self):
        self.phoneFig.setVisible(False)
        self.voiceFig.setVisible(True)
        self.label.setVisible(False)
        self.label1.setVisible(False)
        self.label2.setVisible(True)
        self.label3.setVisible(False)

        self.label11.setVisible(False)
        self.label12.setVisible(False)
        self.label13.setVisible(False)
        self.label14.setVisible(False)
        self.label15.setVisible(False)

        self.weather_label.setVisible(False)
        self.weather_label1.setVisible(False)
        self.weather_label2.setVisible(False)
        self.weather_label3.setVisible(False)
        self.weather_label4.setVisible(False)

        self.label_time.setVisible(False)
    
    #识别成功界面
    def recSuccessUI(self,command):
        self.phoneFig.setVisible(False)
        self.voiceFig.setVisible(True)
        self.label.setVisible(False)
        self.label1.setVisible(False)
        self.label2.setVisible(False)
        self.label3.setVisible(True)
        _translate = QtCore.QCoreApplication.translate
        self.label3.setText(_translate("MainWindow", f"You said '{command}'."))

        self.label11.setVisible(False)
        self.label12.setVisible(False)
        self.label13.setVisible(False)
        self.label14.setVisible(False)
        self.label15.setVisible(False)

        self.weather_label.setVisible(False)
        self.weather_label1.setVisible(False)
        self.weather_label2.setVisible(False)
        self.weather_label3.setVisible(False)
        self.weather_label4.setVisible(False)

        self.label_time.setVisible(False)

    #显示天气
    def displayWeather(self,weather):
        date = weather['date']
        type = weather['type']
        low = weather['low']
        high = weather['high']

        self.weather_label.setVisible(True)
        self.weather_label1.setVisible(True)
        self.weather_label2.setVisible(True)
        self.weather_label3.setVisible(True)
        self.weather_label4.setVisible(True)
        _translate = QtCore.QCoreApplication.translate
        self.weather_label1.setText(_translate("MainWindow", "Date："+date))
        self.weather_label2.setText(_translate("MainWindow", "Type："+type))
        self.weather_label3.setText(_translate("MainWindow", "Low："+low))
        self.weather_label4.setText(_translate("MainWindow", "High："+high))
    
    def displayTime(self):
        self.label_time.setVisible(True)

        


 
