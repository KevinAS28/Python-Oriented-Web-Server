import sys
import os
import time
from threading import Thread
from PyQt4 import QtCore, QtGui, uic

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

qtCreatorFile = os.path.join(dir_path, "OWS_MAIN_GUI.ui") # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class GUI(QtGui.QMainWindow, Ui_MainWindow):
    @property
    def GUI_Name(self):
        return "OWS_MAIN_GUI"
    def Start(self):
        print("Start")
    def Stop(self):
        print("Stop")
    def Restart(self):
        print("Restart")
    def About(self):
        print("About")
    def Write_Status(self, txt):
        if (not (txt.endswith("\n"))):
            txt += "\n"
        self.STATUS.insertPlainText(txt)
    def __init__(self, inputs=[Start, Stop, Restart]):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Inputs = inputs
        self.Outputs = [self.Write_Status]
        self.SInputs = ["Start", "Stop", "Restart"]
        self.SOutputs = ["Write Status"]
        self.START.clicked.connect(self.Inputs[0])
        self.STOP.clicked.connect(self.Inputs[1])
        self.RESTART.clicked.connect(self.Inputs[2])
        self.ABOUT.clicked.connect(self.Inputs[3])
window = []
def Start_GUI(args=[]):
    app = QtGui.QApplication(sys.argv)
    if len(args):
        window.append(GUI(args))
    else:
        window.append(GUI())
    window[0].show()
    sys.exit(app.exec_())
def GUI_Output(txt, ke=0):
    window[0].Outputs[0](txt)
module_name = "OWS_MAIN_GUI"