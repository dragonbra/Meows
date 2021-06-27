from PyQt5 import QtWidgets
from funcWindowBind import funcWindow
import sys
import torch

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = funcWindow()
    mainWindow.show()
    sys.exit(app.exec_())
