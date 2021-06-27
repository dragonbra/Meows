import time

import pandas as pd
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
        self.multiNewsTable.setColumnWidth(0, 300)
        self.multiNewsTable.setColumnWidth(1, 500)
        self.multiFileButton.clicked.connect(self.multiGetNewsFromFile)
        self.multiPredictButton.clicked.connect(self.multiNewsPredict)

        self.multiSaveButton.clicked.connect(self.multiNewsSave)

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
        if index != 0:
            self.multiNewsTable.insertRow(index)
        self.multiNewsTable.setItem(index, 0, QtWidgets.QTableWidgetItem(newsTitle))
        self.multiNewsTable.setItem(index, 1, QtWidgets.QTableWidgetItem(newsContent))
        # QApplication.processEvents()
        pass

    def multiGetNewsFromFile(self):
        self.multiNewsTable.setRowCount(1)
        self.multiNewsTable.clearContents()
        self.multiResultsTable.setRowCount(1)
        self.multiResultsTable.clearContents()

        filePath, fileType = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', self.defaultFilePath, "多新闻文件(*.csv, *.xls, *.xlsx)")

        print(filePath)
        print(len(filePath))
        if len(filePath) == 0:
            pass

        else:
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
            newsTitle = self.multiNewsTable.item(index, 0).text()
            newsContent = self.multiNewsTable.item(index, 1).text()
            newsTextOri = str.strip(dataProcUtils.newsMerge(newsTitle, newsContent))

            if index != 0:
                self.multiResultsTable.insertRow(index)

            if len(newsTextOri) == 0:
                self.multiResultsTable.setItem(index, 0, "空")
            else:
                predictChannel = self.classifier.predict(newsTextOri)
                self.multiResultsTable.setItem(index, 0, QtWidgets.QTableWidgetItem(predictChannel))

            QApplication.processEvents()

    def multiNewsSave(self):
        filePath, fileType = QtWidgets.QFileDialog.getSaveFileName(self, "导出结果", self.defaultFilePath, ".csv文件(*.csv)")

        try:
            newsTitleList = []
            newsContentList = []
            channelNameList = []

            for index in range(self.multiNewsSize):
                newsTitle = self.multiNewsTable.item(index, 0).text()
                newsContent = self.multiNewsTable.item(index, 1).text()
                channelName = self.multiResultsTable.item(index, 0).text()

                newsTitleList.append(newsTitle)
                newsContentList.append(newsContent)
                channelNameList.append(channelName)

            output_excel = {'content': newsContentList, 'channelName': channelNameList, 'title': newsTitleList}
            output = pd.DataFrame(output_excel)
            print(filePath)
            output.to_csv(filePath, index=False, encoding="gb18030", header=None)

        except Exception as e:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = funcWindow()
    window.show()
    sys.exit(app.exec_())
