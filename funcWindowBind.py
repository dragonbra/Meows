import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from news import Ui_MainWindow
import sys
import os
import tqdm
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
        self.defaultFilePath = "./example/"

        # singlePredict Widget's Functions
        self.singleFileButton.clicked.connect(self.singleGetNewsFromFile)

        self.predictButton.clicked.connect(self.singleNewsPredict)
        self.predictButton2.clicked.connect(self.singleNewsPredict)

        # multiPredict Widget's Function
        self.multiNewsSize = 0
        self.multiFileButton.clicked.connect(self.multiGetNewsFromFile)
        self.multiPredictButton.clicked.connect(self.multiNewsPredict)

    def singleGetNewsFromFile(self):
        filePath, fileType = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', self.defaultFilePath, "单新闻文件(*.txt)")

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

    def singleNewsPredict(self):
        newsTitle = self.singleNewslineEdit.text()
        newsContent = self.singleNewsPaperEdit.toPlainText()
        newsTextOri = str.strip(dataProcUtils.newsMerge(newsTitle, newsContent))

        if len(newsTextOri) == 0:
            self.singleResultBroswer.setText("请输入新闻")

        else:
            predictChannel = self.classifier.predict(newsTextOri)
            self.singleResultBroswer.setText(predictChannel)
            self.db.dataInsert(predictChannel=predictChannel, channelName="", title=newsTitle, content=newsContent)

    def multiNewsInsertTableWidget(self, index, channelName, newsTitle, newsContent):
        # TODO
        # Insert news into table widget in multiNewsWidget
        self.multiNewsTable.insertRow(self.multiNewsTable.rowCount())
        pass

    def multiGetNewsFromFile(self):
        self.multiNewsTable.clear()
        self.multiResultsTable.clear()
        filePath, fileType = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', self.defaultFilePath, "多新闻文件(*.csv, *.xls, *.xlsx)")

        if not os.path.getsize(filePath):
            pass

        try:
            self.channelNameList, self.newsTitleList, self.newsContentList = dataProcUtils.readCorpus(filePath)
            self.multiNewsSize = len(self.newsTitleList)
            for index in range(self.multiNewsSize):
                channelName = self.channelNameList[index]
                newsTitle = self.newsTitleList[index]
                newsContent = self.newsContentList[index]
                self.multiNewsInsertTableWidget(index, channelName, newsTitle, newsContent)

        except Exception as e:
            pass

    def multiNewsPredict(self):
        if self.multiNewsSize == 0:
            return
        for index in range(self.multiNewsSize):
            print(index)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = funcWindow()
    window.show()
    sys.exit(app.exec_())
