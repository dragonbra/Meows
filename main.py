import sys
from ui.bindfuncwindow import FuncWindow
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = FuncWindow()
    mainWindow.show()
    sys.exit(app.exec_())
