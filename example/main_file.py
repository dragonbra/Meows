from PyQt5 import QtCore, QtGui, QtWidgets
from file import Ui_Form
import os

class Window(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.count = 0

    def scan(self):
        input = self.lineEdit.text()
        self.ope(input)

    def ope(self, input):
        if (os.path.isfile(input)):
            # self.count += 1
            # for i in range(0, self.count):
            #     self.textBrowser.(' ')
            self.textBrowser.append(input)
            # self.count = 0
        else:
            # self.count += 1
            # for i in range(0, self.count):
            #     self.textBrowser.print(' ')
            self.textBrowser.append(input)
            for file in os.listdir(input):
                #保证完整路径
                self.ope(input + '\\' + file)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
