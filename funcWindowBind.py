import time

import pandas as pd
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

from mainWindowLayout import Ui_MainWindow
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
        print("加载模型花费:%.2f" % (time.time() - st), "秒")

        self.db = dataBaseUtils.DataBase()
        self.defaultFilePath = "./example/"
        self.LOGOPATH = "./data/logo.jpg"

        # mainWindow
        self.setWindowIcon(QtGui.QIcon("./data/icon.ico"))

        # singlePredict Widget's Functions
        self.singleFileButton.clicked.connect(self.singleGetNewsFromFile)
        logoImg = QtGui.QImage(self.LOGOPATH).scaled(self.singleLogoLabel.width(), self.singleLogoLabel.height())
        self.singleLogoLabel.setPixmap(QtGui.QPixmap.fromImage(logoImg))
        self.predictButton.clicked.connect(self.singleNewsPredict)
        self.predictButton2.clicked.connect(self.singleNewsPredict)

        # multiPredict Widget's Function
        self.multiNewsSize = 0
        self.multiNewsTable.setColumnWidth(0, 200)
        self.multiNewsTable.setColumnWidth(1, 400)
        self.multiFileButton.clicked.connect(self.multiGetNewsFromFile)
        self.multiPredictButton.clicked.connect(self.multiNewsPredict)
        self.multiSaveButton.clicked.connect(self.multiNewsSave)

        # searchDB Widget's Function
        self.searchDBTable.setColumnWidth(0, 75)
        self.searchDBTable.setColumnWidth(1, 75)
        self.searchDBTable.setColumnWidth(2, 200)
        self.searchDBTable.setColumnWidth(3, 400)
        self.searchButton.clicked.connect(self.searchDBtoTable)
        self.searchClearButton.clicked.connect(self.searchTableClear)
        self.searchF1Button.clicked.connect(self.searchCalF1)

        # wordCloud Widget's Function
        self.wordDrawButton.clicked.connect(self.wordCloudDraw)

        # intro Widget's Function
        self.introLogoLabel.setPixmap(QtGui.QPixmap.fromImage(logoImg))

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
        # Insert news into table widget in multiNewsWidget
        if index != 0:
            self.multiNewsTable.insertRow(index)
        self.multiNewsTable.setItem(index, 0, QtWidgets.QTableWidgetItem(str(newsTitle)))
        self.multiNewsTable.setItem(index, 1, QtWidgets.QTableWidgetItem(str(newsContent)))
        # QApplication.processEvents()

    def multiGetNewsFromFile(self):
        self.multiNewsTable.setRowCount(1)
        self.multiNewsTable.clearContents()
        self.multiResultsTable.setRowCount(1)
        self.multiResultsTable.clearContents()

        filePath, fileType = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', self.defaultFilePath,
                                                                   "多新闻文件(*.csv, *.xls, *.xlsx)")
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
                print(filePath, "has been loaded!")

            except Exception as e:
                print(e)
                pass

    def multiNewsPredict(self):
        self.multiResultsTable.setRowCount(1)
        self.multiResultsTable.clearContents()
        if self.multiNewsSize == 0:
            return
        self.multiLoadingLine.setRange(0, self.multiNewsSize - 1)
        for index in range(self.multiNewsSize):
            channelName = self.channelNameList[index]
            if str(channelName) == "nan":
                channelName = "(空)"
            newsTitle = self.multiNewsTable.item(index, 0).text()
            newsContent = self.multiNewsTable.item(index, 1).text()
            newsTextOri = str.strip(dataProcUtils.newsMerge(newsTitle, newsContent))

            if index != 0:
                self.multiResultsTable.insertRow(index)

            if len(newsTextOri) == 0:
                self.multiResultsTable.setItem(index, 0, "(空)")
                self.multiResultsTable.setItem(index, 1, QtWidgets.QTableWidgetItem(str(channelName)))
            else:
                predictChannel = self.classifier.predict(newsTextOri)
                self.multiResultsTable.setItem(index, 0, QtWidgets.QTableWidgetItem(predictChannel))
                self.multiResultsTable.setItem(index, 1, QtWidgets.QTableWidgetItem(str(channelName)))
                self.db.dataInsert(predictChannel, channelName, newsTitle, newsContent)

            self.multiNewsTable.selectRow(index)
            self.multiResultsTable.selectRow(index)
            self.multiLoadingLine.setValue(index)
            QApplication.processEvents()

    def multiNewsSave(self):
        filePath, fileType = QtWidgets.QFileDialog.getSaveFileName(self, "导出结果", self.defaultFilePath + "result.csv",
                                                                   ".csv文件(*.csv)")
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
            output.to_csv(filePath, index=False, encoding="gb18030", header=None)
            print(filePath, "Succeeded!")

        except Exception as e:
            pass

    def searchDBInsertTableWidget(self, index, predictChannel, channelName, newsTitle, newsContent):
        # Insert news into table widget in multiNewsWidget
        if index != 0:
            self.searchDBTable.insertRow(index)
        self.searchDBTable.setItem(index, 0, QtWidgets.QTableWidgetItem(str(predictChannel)))
        self.searchDBTable.setItem(index, 1, QtWidgets.QTableWidgetItem(str(channelName)))
        self.searchDBTable.setItem(index, 2, QtWidgets.QTableWidgetItem(str(newsTitle)))
        self.searchDBTable.setItem(index, 3, QtWidgets.QTableWidgetItem(str(newsContent)))

        colorStr = "cyan"
        if str(channelName) != "(空)" and len(str(channelName)) != 0:
            if predictChannel == channelName:
                colorStr = "lightgreen"
            else:
                colorStr = "#ff6565"
        self.searchDBTable.item(index, 0).setBackground(QtGui.QColor(colorStr))
        # QApplication.processEvents()

    def searchTableClear(self):
        self.searchDBTable.setRowCount(1)
        self.searchDBTable.clearContents()

    def searchCalF1(self):
        targetDict = {"财经": 0, "房产": 1, "教育": 2, "科技": 3, "军事": 4, "汽车": 5, "体育": 6, "游戏": 7, "娱乐": 8, "其他": 9}

        f1ScoreResList = [0 for i in range(10)]
        tp = [0 for i in range(10)]
        tn = [0 for i in range(10)]
        fp = [0 for i in range(10)]
        fn = [0 for i in range(10)]
        precision = [0 for i in range(10)]
        recall = [0 for i in range(10)]
        dataList = self.db.dataQuery()
        dataSize = len(dataList)
        for index in range(dataSize):
            dataRow = dataList[index]
            predictChannel = dataRow[1]
            channelName = dataRow[2]
            if channelName == "(空)" or len(channelName) == 0:
                continue
            else:
                if predictChannel == channelName:
                    tp[targetDict[predictChannel]] += 1
                else:
                    fn[targetDict[channelName]] += 1
                    fp[targetDict[predictChannel]] += 1

        f1ScoreRes = 0
        f1ScoreNum = 0
        try:
            for index in range(10):
                if tp[index] + fp[index] == 0 or tp[index] + fn[index] == 0:
                    continue
                precision[index] = tp[index] / (tp[index] + fp[index])
                recall[index] = tp[index] / (tp[index] + fn[index])
                f1ScoreResList[index] = 2 * precision[index] * recall[index] / (precision[index] + recall[index])
                f1ScoreNum += 1
                f1ScoreRes += f1ScoreResList[index]
        except Exception as e:
            print(e)
            pass
        print(f1ScoreNum, f1ScoreRes)
        if f1ScoreNum:
            f1ScoreRes /= f1ScoreNum
        self.searchF1Result.setText("%.2f" % f1ScoreRes)


    def searchDBtoTable(self):
        self.searchDBTable.setRowCount(1)
        self.searchDBTable.clearContents()

        keyword = self.searchLineEdit.text()
        dataList = self.db.dataQuery(keyword)
        dataListSize = len(dataList)

        for index in range(dataListSize):
            dataRow = dataList[index]
            predictChannel = dataRow[1]
            channelName = dataRow[2]
            newsTitle = dataRow[3]
            newsContent = dataRow[4]
            self.searchDBInsertTableWidget(index, predictChannel, channelName, newsTitle, newsContent)

    def wordCloudinit(self):
        self.tc = True
        self.swf = True
        self.pscale = 2
        self.number = 200
        self.pheight = 1000
        self.pwidth = 1000
        self.pstopwords = ""
        self.pcontour_width = 0
        self.prelative_scaling = 0.5
        self.pcolormap = "viridis"
        sfont = "宋体"

        if sfont == "宋体":
            self.font_path = "simsun.ttc"

        list = [('tc', self.tc),
                ('scale', self.pscale),
                ('font_path', self.font_path),
                ('number', self.number),
                ('width', self.pwidth),
                ('height', self.pheight),
                ('stopwords', self.pstopwords),
                ('contour_width', self.pcontour_width),
                ('colormap', self.pcolormap),
                ('relative_scaling', self.prelative_scaling),
                ('swf', self.swf)]

        self.para = dict(list)  # 将列表转化为字典
        print(len(self.para))

    def wordCloudDraw(self):
        self.wordCloudinit()
        self.txtfile = "./月光.txt"
        self.imgfile = "./wordSizeImages/皮卡丘.png"

        if self.swf == 1:  # 如果按照词频来绘制
            try:
                self.WordCountWidget.mpl.wordfreqplot(self.txtfile)
                self.wordCloudTabWidget.setCurrentIndex(1)
            except Exception as e:
                print(e)
                return

        # self.mpl  是MyMplCanvas() 对象
        print(self.para)

        self.WordCloudWidget.mpl.wordcloud_plot(self.txtfile, self.imgfile, self.para)
        self.wordCloudTabWidget.setCurrentIndex(0)
        # self.mytips.setPlainText("正在生成图像，请稍等...")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = funcWindow()
    window.show()
    sys.exit(app.exec_())
