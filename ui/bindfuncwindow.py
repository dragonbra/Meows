import time
import sys
import os
import pandas as pd
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication
from config import Const
from ui.mainwindow import Ui_MainWindow
from utils import dataProcUtil
from utils import dataBaseUtil
from utils.classifyUtil import Classifier


class FuncWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.newsDB = dataBaseUtil.DataBase()
        self.DEFAULT_FILE_PATH = Const.DEFAULT_FILE_PATH
        self.DEFAULT_SINGLE_FILE_PATH = self.DEFAULT_FILE_PATH + '单条新闻\\'
        self.DEFAULT_MULTI_FILE_PATH = self.DEFAULT_FILE_PATH + '多条新闻\\'
        self.TAB_ICON_DIR = Const.TAB_ICON_DIR
        self.CHANNEL_IMG_DIR = Const.CHANNEL_IMG_DIR
        self.LOGO_IMG_PATH = Const.LOGO_IMG_PATH
        self.LOGO_ICON_PATH = Const.LOGO_ICON_PATH
        self.MASK_IMG_PATH = Const.MASK_IMG_PATH

        st = time.time()
        self.classifier = Classifier()
        print("加载模型花费:%.2f" % (time.time() - st), "秒")

        # mainWindow
        self.setWindowIcon(QtGui.QIcon(self.LOGO_ICON_PATH))
        self.mainTabWidget.setIconSize(QtCore.QSize(45, 45))
        self.mainTabWidget.setTabIcon(0, QtGui.QIcon(self.TAB_ICON_DIR + '0_singlePredict.png'))
        self.mainTabWidget.setTabIcon(1, QtGui.QIcon(self.TAB_ICON_DIR + '1_multiPredict.png'))
        self.mainTabWidget.setTabIcon(2, QtGui.QIcon(self.TAB_ICON_DIR + '2_searchDB.png'))
        self.mainTabWidget.setTabIcon(3, QtGui.QIcon(self.TAB_ICON_DIR + '3_wordCloud.png'))
        self.mainTabWidget.setTabIcon(4, QtGui.QIcon(self.TAB_ICON_DIR + '4_Meows.ico'))

        # singlePredict Widget's Functions
        self.singleClearButton.clicked.connect(self.singleClear)
        self.singlePredictResultLabel.setScaledContents(True)
        self.singlePredictResultLabel. \
            setPixmap(QtGui.QPixmap.
                      fromImage(QtGui.QImage(self.CHANNEL_IMG_DIR + '其他' + '.png')))
        self.singleFileButton.clicked.connect(self.singleGetNewsFromFile)
        self.predictButton.clicked.connect(self.singleNewsPredict)
        self.predictButton2.clicked.connect(self.singleNewsPredict)

        # multiPredict Widget's Function
        self.multiNewsSize = 0
        self.multiFileButton.clicked.connect(self.multiGetNewsFromFile)
        self.multiPredictButton.clicked.connect(self.multiNewsPredict)
        self.multiSaveButton.clicked.connect(self.multiNewsSave)
        self.multiResultsTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.multiResultsTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

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
        path, file = os.path.split(self.MASK_IMG_PATH)
        fileName, fileFmt = os.path.splitext(file)
        self.wordCloudMask.setText(fileName)
        self.wordCouldMaskSelectButton.clicked.connect(self.wordCloudMaskSelect)

        # intro Widget's Function
        self.introLogoLabel.setPixmap(QtGui.QPixmap.
                                      fromImage(QtGui.QImage(self.LOGO_IMG_PATH).
                                                scaled(self.introLogoLabel.width(),
                                                       self.introLogoLabel.height())))

    def singleClear(self):
        self.singlePredictResultLabel. \
            setPixmap(QtGui.QPixmap.
                      fromImage(QtGui.QImage(self.CHANNEL_IMG_DIR + '其他' + '.png')))
        self.singleResultBroswer.setText("请输入新闻")
        self.singleResultBroswer.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)

    def singleGetNewsFromFile(self):
        filePath, fileType = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', self.DEFAULT_SINGLE_FILE_PATH, "单新闻文件(*.txt)")

        try:
            file_name = os.path.basename(filePath)
            self.DEFAULT_SINGLE_FILE_PATH = os.path.dirname(filePath)
            title, suffix = os.path.splitext(file_name)

            file = open(filePath, "r", encoding="utf-8")
            content = file.read()
            file.close()

            self.singleNewslineEdit.setText(title)
            self.singleNewsPaperEdit.setText(content)
        except Exception as e:
            print(e)
            return

    def singleNewsPredict(self):
        newsTitle = self.singleNewslineEdit.text()
        newsContent = self.singleNewsPaperEdit.toPlainText()
        newsTextOri = str.strip(dataProcUtil.newsMerge(newsTitle, newsContent))

        if len(newsTextOri) == 0:
            self.singlePredictResultLabel. \
                setPixmap(QtGui.QPixmap.
                          fromImage(QtGui.QImage(self.CHANNEL_IMG_DIR + '其他' + '.png')))
            self.singleResultBroswer.setText("请输入新闻")
            self.singleResultBroswer.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)

        else:
            predictChannel = self.classifier.predict(newsTextOri)
            self.singlePredictResultLabel. \
                setPixmap(QtGui.QPixmap.
                          fromImage(QtGui.QImage(self.CHANNEL_IMG_DIR + predictChannel + '.png')))
            self.singleResultBroswer.setText(predictChannel)
            self.singleResultBroswer.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
            self.newsDB.dataInsert(predictChannel=predictChannel, channelName="", title=newsTitle, content=newsContent)

    def multiNewsInsertTableWidget(self, index, channelName, newsTitle, newsContent):
        # Insert news into table widget in multiNewsWidget
        if index != 0:
            self.multiNewsTable.insertRow(index)
            self.multiResultsTable.insertRow(index)

        if str(channelName) == 'nan':
            self.multiResultsTable.setItem(index, 1, QtWidgets.QTableWidgetItem("(空)"))
        else:
            self.multiResultsTable.setItem(index, 1, QtWidgets.QTableWidgetItem(str(channelName)))
        self.multiResultsTable.setItem(index, 0, QtWidgets.QTableWidgetItem(' '))
        self.multiResultsTable.item(index, 0).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.multiResultsTable.item(index, 1).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.multiNewsTable.setItem(index, 0, QtWidgets.QTableWidgetItem(str(newsTitle)))
        self.multiNewsTable.setItem(index, 1, QtWidgets.QTableWidgetItem(str(newsContent)))
        # QApplication.processEvents()

    def multiGetNewsFromFile(self):
        self.multiNewsTable.setRowCount(1)
        self.multiNewsTable.clearContents()
        self.multiResultsTable.setRowCount(1)
        self.multiResultsTable.clearContents()

        filePath, fileType = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', self.DEFAULT_MULTI_FILE_PATH,
                                                                   "多新闻文件(*.csv *.xlsx *.xls)")
        if len(filePath) == 0:
            pass
        else:
            self.DEFAULT_MULTI_FILE_PATH = os.path.dirname(filePath)
            try:
                channelNameList, newsTitleList, newsContentList = dataProcUtil.readCorpus(filePath)
                self.multiNewsSize = len(newsTitleList)
                for index in range(self.multiNewsSize):
                    channelName = channelNameList[index]
                    newsTitle = newsTitleList[index]
                    newsContent = newsContentList[index]
                    self.multiNewsInsertTableWidget(index, channelName, newsTitle, newsContent)
                print(filePath, "has been loaded!")

            except Exception as e:
                print(e)
                pass

    def multiNewsPredict(self):
        if self.multiNewsSize == 0:
            return
        self.multiLoadingLine.setRange(0, self.multiNewsSize - 1)
        for index in range(self.multiNewsSize):
            channelName = self.multiResultsTable.item(index, 1).text()
            if str(channelName) == 'nan':
                channelName = "(空)"
            newsTitle = self.multiNewsTable.item(index, 0).text()
            newsContent = self.multiNewsTable.item(index, 1).text()
            newsTextOri = str.strip(dataProcUtil.newsMerge(newsTitle, newsContent))

            if len(newsTextOri) == 0:
                self.multiResultsTable.setItem(index, 0, "(空)")
            else:
                predictChannel = self.classifier.predict(newsTextOri)
                self.multiResultsTable.setItem(index, 0, QtWidgets.QTableWidgetItem(predictChannel))
                self.newsDB.dataInsert(predictChannel, channelName, newsTitle, newsContent)

            colorStr = "cyan"
            if str(channelName) != "(空)" and len(str(channelName)) != 0:
                if predictChannel == channelName:
                    colorStr = "lightgreen"
                else:
                    colorStr = "#ff6565"
            self.multiResultsTable.item(index, 0).setBackground(QtGui.QColor(colorStr))

            self.multiResultsTable.item(index, 0).setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

            self.multiNewsTable.selectRow(index)
            self.multiResultsTable.selectRow(index)
            self.multiLoadingLine.setValue(index)
            QApplication.processEvents()

    def multiNewsSave(self):
        filePath, fileType = QtWidgets.QFileDialog.getSaveFileName(self, "导出结果", self.DEFAULT_MULTI_FILE_PATH + "result.csv",
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
            output.to_csv(filePath, index=False, encoding="utf_8_sig", header=None)
            print(filePath, " has been saved successfully!")

        except Exception as e:
            print(e)
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

        f1ScoreResList = [0 for _ in range(10)]
        tp = [0 for _ in range(10)]
        tn = [0 for _ in range(10)]
        fp = [0 for _ in range(10)]
        fn = [0 for _ in range(10)]
        precision = [0 for _ in range(10)]
        recall = [0 for _ in range(10)]
        dataList = self.newsDB.dataQuery()
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
        for _ in range(10):
            print(_, f1ScoreResList[_])

        if f1ScoreNum:
            f1ScoreRes /= f1ScoreNum
        self.searchF1Result.setText("%.2f" % f1ScoreRes)

    def searchDBtoTable(self):
        self.searchDBTable.setRowCount(1)
        self.searchDBTable.clearContents()

        keyword = self.searchLineEdit.text()
        dataList = self.newsDB.dataQuery(keyword)
        dataListSize = len(dataList)

        for index in range(dataListSize):
            dataRow = dataList[index]
            predictChannel = dataRow[1]
            channelName = dataRow[2]
            newsTitle = dataRow[3]
            newsContent = dataRow[4]
            self.searchDBInsertTableWidget(index, predictChannel, channelName, newsTitle, newsContent)

    def wordCloudMaskSelect(self):
        filePath, fileType = QtWidgets.QFileDialog.getOpenFileName(self, '选择蒙版', self.MASK_IMG_PATH,
                                                                   "图片文件(*.png *.jpg *.jpeg)")
        if len(filePath) == 0:
            return
        self.MASK_IMG_PATH = filePath
        path, file = os.path.split(self.MASK_IMG_PATH)
        fileName, fileFmt = os.path.splitext(file)
        self.wordCloudMask.setText(fileName)

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
        # print(len(self.para))

    def wordCloudDraw(self):
        self.wordCloudinit()
        self.txtfile = self.wordCloudSrc.currentText()
        print(self.txtfile)
        self.imgfile = self.MASK_IMG_PATH

        if self.swf == 1:  # 如果按照词频来绘制
            try:
                self.WordCountWidget.mpl.wordfreqplot(self.txtfile)
                self.wordCloudTabWidget.setCurrentIndex(1)
            except Exception as e:
                print(e)
                return

        # self.mpl  是MyMplCanvas() 对象
        # print(self.para)

        self.WordCloudWidget.mpl.wordcloud_plot(self.txtfile, self.imgfile, self.para)
        self.wordCloudTabWidget.setCurrentIndex(0)
        # self.mytips.setPlainText("正在生成图像，请稍等...")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = FuncWindow()
    window.show()
    sys.exit(app.exec_())
