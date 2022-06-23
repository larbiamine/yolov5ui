import sys
import os
import inspect
import subprocess
# IMPORT MODULES
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal
import PySide6.QtQuick
import videoplayer 
from PyQt5.QtWidgets import QApplication

# app = QApplication(sys.argv)  
# v = videoplayer.VideoPlayer() 
# v.abrir("C:/Users/Jay Liam/Videos/2022-04-27 20-48-22.mp4")
# # v.abrir(sauce)
# v.setWindowTitle("Player")
# v.resize(600, 400)
# v.show()


# app = QApplication(sys.argv)
# player = videoplayer.VideoPlayer() 
# player.abrir("C:/Users/Jay Liam/Videos/2022-04-27 20-48-22.mp4")
# player.setWindowTitle("Player")
# player.resize(600, 400)
# player.show()
# sys.exit(app.exec_())

# def playVideo(sauce):  
#     v.abrir("C:/Users/Jay Liam/Documents/yolov5ui/yolov5ui/2.mp4")
#     # v.abrir(sauce)
#     v.setWindowTitle("Player")
#     v.resize(600, 400)
#     v.show()

# Main Window Class
class MainWindow(QObject):
    def __init__(self):
        QObject.__init__(self)

    detectionEnd = Signal(bool, str, str)
    @Slot(str)
    def playVideo(self, sauce): 
        app = QApplication(sys.argv)  
        v = videoplayer.VideoPlayer() 
        #v.abrir("C:/Users/Jay Liam/Documents/yolov5ui/yolov5/runs/detect/exp/a.mp4")
        v.abrir(sauce)
        v.setWindowTitle("Player")
        v.resize(600, 400)
        v.show()
        sys.exit(app.exec_())
    
    @Slot(str, str, str)
    def runYolo(self, type, model, source):

        currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        detect = '"' + os.path.dirname(currentdir) + "\yolov5\detect.py" + '"'
        pythopath = '"' + os.path.dirname(currentdir) + "yolo\Scripts" + '"'
        weights = '"' + os.path.dirname(currentdir) + "\yolov5\\finalmodel.pt" + '"' 
        if(type == "webcam"):
            source = "0"
        else:
            source = '"' + source + '"'
        command = "python "+detect+" --weights "+weights+" --source "+source+" --exist-ok"
        process = subprocess.run(command, shell=True)
        if(process.returncode == 0):
            if(type == "directory"):
                result ="file:" + os.path.dirname(currentdir) + "\yolov5\\runs\detect\exp\\" 
                self.detectionEnd.emit(True, result, "Resultat sauvgardé dans: "+result)
                #open result folder in explorer
                explorer = 'explorer ' + result
                subprocess.run(explorer, shell=True)
            else:    
                result ="file:" + os.path.dirname(currentdir) + "\yolov5\\runs\detect\exp\\" + os.path.basename(source)
            result = result.replace("/", "\\\\")
            result = result[:len(result) - 1]
            if (type == "video"):
                
                result = result.replace("file:", "")
                result = result.replace("\\", "/")

                self.playVideo(result)
                self.detectionEnd.emit(True, result,"")
                
            else:
                self.detectionEnd.emit(True, result,"")

    @Slot()
    def leave(self):
        exit()

# INSTACE CLASS

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()

application_path = (
    sys._MEIPASS
    if getattr(sys, "frozen", False)
    else os.path.dirname(os.path.abspath(__file__))
)

# Get Context
main = MainWindow()
engine.rootContext().setContextProperty("backend", main)

# Load QML File
engine.load(os.path.join(application_path, "main.qml"))

# Check Exit App
if not engine.rootObjects():
    sys.exit(-1)
sys.exit(app.exec())
