from PyQt5 import QtWidgets, QtGui, QtCore, uic
from asrInterface import Ui_MainWindow
import sys,threading,os,time
import speech_recognition as sr
import difflib

from playsound import playsound
import requests,json

#字符串相似度
def string_similarity(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.isWake = False
    
    #开始语音识别
    def runASR(self):
        self.timer = threading.Timer(0,self.audio_recognition)
        self.timer.start()
    
    #语音识别
    def audio_recognition(self):

        #每隔5秒识别一次，防止语音识别时间太长
        self.timer = threading.Timer(5,self.audio_recognition)
        self.timer.start()

        print("开始语音识别！")

        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        #监听麦克风，语音识别
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source,timeout=10)  
            except:
                print("Listen time out!")
        
        #识别命令
        try:
            command = recognizer.recognize_sphinx(audio)
        except:
            print("读取语音内容失败！")
        else:
            print(f"您说: {command}")

            #Hey Siri唤醒
            similarity = string_similarity(command,"Hey Siri")
            print(f"相似度: {similarity}")

            if similarity > 0.1:
                self.wakeSuccess()
            else:
                print("唤醒Siri失败！")
        
    #成功唤醒
    def wakeSuccess(self):
        if self.isWake:
            return
        self.isWake = True
        print("成功唤醒Siri!")
        self.ui.asrUI()
        threading.Thread(target=playAudio,args=("siri/wake.mp3",)).start()

        if self.timer:
            self.timer.cancel()

        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        #监听麦克风，语音识别
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source,timeout=10)  
            except:
                print("Listen time out!")

        #识别命令
        try:
            command = recognizer.recognize_sphinx(audio)
        except:
            print("读取语音内容失败！")
            self.recognitionFail()
        else:
            print(f"您说: {command}")

            command_list = [ "music","notepad","time","weather"]

            similarity_list = [ string_similarity(command,c) for c in command_list ]

            #找到相似度最大的命令
            similarity_max = max(similarity_list)
            index_max = similarity_list.index(similarity_max)

            if similarity_max < 0.3:
                print("无法识别命令！")
                self.recognitionFail()
            else:
                print("Command:{}".format(command_list[index_max]))
                threading.Thread(target=playAudio,args=("siri/success.mp3",)).start()
                self.ui.recSuccessUI(command_list[index_max])
                #执行命令
                if index_max==0:
                    os.startfile("music\\Canon.mp3")
                elif index_max==1:
                    os.system("notepad")
                elif index_max==2:
                    self.ui.displayTime()
                elif index_max==3:
                    weather = getWeather()
                    self.ui.displayWeather(weather)

                time.sleep(5)

        self.ui.mainUI()
        self.timer = threading.Timer(0,self.audio_recognition)
        self.timer.start()
        self.isWake = False

    #无法识别命令
    def recognitionFail(self):
        self.ui.recFailUI()
        time.sleep(2)
 
#开始
def start():
    application.ui.mainUI()
    application.runASR()

#播放音频
def playAudio(sound):
    playsound(sound)

#查询今日上海天气
def getWeather():
    rb = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=上海')
    data = json.loads(rb.text)
    return data['data']['forecast'][0]

if __name__=="__main__":
    app = QtWidgets.QApplication([])
    application = myWindow()
    application.show()

    #播放启动音频，5s后开始
    threading.Thread(target=playAudio,args=("siri/start.mp3",)).start()
    timer = threading.Timer(5,start)
    timer.start()
    

    sys.exit(app.exec())

