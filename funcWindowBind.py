import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from news import Ui_MainWindow
import sys
import os
import dataProcUtils
import dataBaseUtils
from dataProcUtils import Classifier


class funcWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        st = time.time()
        self.classifier = Classifier()
        print(time.time() - st)

        self.db = dataBaseUtils.DataBase()
        self.defaultFilePath = "./"

        self.singleFileButton.clicked.connect(self.singleGetNewsFromFile)

        self.predictButton.clicked.connect(self.singleNewsPredict)
        self.predictButton2.clicked.connect(self.singleNewsPredict)

    def singleNewsPredict(self):
        newsTitle = self.singleNewslineEdit.text()
        newsContent = self.singleNewsPaperEdit.toPlainText()
        newsTextOri = dataProcUtils.newsMerge(newsTitle, newsContent)

        print(newsTextOri)
        predictChannel = self.classifier.predict(newsTextOri)
        self.singleResultBroswer.setText(predictChannel)

        self.db.dataInsert(predictChannel=predictChannel, channelName="", title=newsTitle, content=newsContent)
        dataList = self.db.dataQuery()
        print(len(dataList))
        for dataRow in dataList:
            print(dataRow)

    def singleGetNewsFromFile(self):
        filePath, fileType = QtWidgets.QFileDialog.getOpenFileName(self, '打开文件', self.defaultFilePath, "News(*.txt)")

        try:
            file_name = os.path.basename(filePath)
            self.defaultFilePath = os.path.dirname(filePath)
            title, suffix = os.path.splitext(file_name)

            file = open(filePath, "r", encoding="utf-8")
            content = file.read()
            file.close()

            self.singleNewslineEdit.setText(title)
            self.singleNewsPaperEdit.setText(content)
        except Exception as e:
            return


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = funcWindow()
    window.show()
    sys.exit(app.exec_())
