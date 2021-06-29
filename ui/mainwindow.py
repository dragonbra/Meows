# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 658)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.mainTabWidget.setGeometry(QtCore.QRect(30, 30, 871, 591))
        self.mainTabWidget.setMinimumSize(QtCore.QSize(661, 500))
        self.mainTabWidget.setStyleSheet("QTabWidget::pane{\n"
"}\n"
"QTabWidget::tab-bar{\n"
"    alignment:left;\n"
"}\n"
"QTabBar::tab{\n"
"    color:white;\n"
"    background:rgb(0, 170, 255);\n"
"    min-width:150px;\n"
"    min-height:50px;\n"
"    font:13pt \'微软雅黑\';\n"
"}\n"
"QTabBar::tab:hover{\n"
"    color:rgb(0, 170, 255);\n"
"    background:rgb(255, 255, 255, 100);\n"
"}\n"
"QTabBar::tab:selected{\n"
"    border-color:rgb(0, 170, 255);\n"
"    background:white;\n"
"    color:rgb(0, 170, 255);\n"
"}")
        self.mainTabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.mainTabWidget.setUsesScrollButtons(False)
        self.mainTabWidget.setDocumentMode(False)
        self.mainTabWidget.setTabsClosable(False)
        self.mainTabWidget.setObjectName("mainTabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setStyleSheet("")
        self.tab_1.setObjectName("tab_1")
        self.widget_1 = QtWidgets.QWidget(self.tab_1)
        self.widget_1.setGeometry(QtCore.QRect(0, 0, 871, 491))
        self.widget_1.setStyleSheet("")
        self.widget_1.setObjectName("widget_1")
        self.singleNewsPaperEdit = QtWidgets.QTextEdit(self.widget_1)
        self.singleNewsPaperEdit.setGeometry(QtCore.QRect(40, 110, 521, 301))
        self.singleNewsPaperEdit.setStyleSheet("QTextEdit {\n"
"    background-color: white;\n"
"    border-width: 2px;\n"
"    border-color: #3D74BB;\n"
"    border-style: solid;\n"
"}")
        self.singleNewsPaperEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.singleNewsPaperEdit.setObjectName("singleNewsPaperEdit")
        self.singleFileButton = QtWidgets.QPushButton(self.widget_1)
        self.singleFileButton.setGeometry(QtCore.QRect(450, 30, 111, 51))
        self.singleFileButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: white;\n"
"    color:rgb(0, 170, 255);\n"
"    border-style: inset;\n"
"}")
        self.singleFileButton.setObjectName("singleFileButton")
        self.predictButton2 = QtWidgets.QPushButton(self.widget_1)
        self.predictButton2.setGeometry(QtCore.QRect(585, 300, 61, 61))
        self.predictButton2.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: white;\n"
"    color:rgb(0, 170, 255);\n"
"    border-style: inset;\n"
"}")
        self.predictButton2.setObjectName("predictButton2")
        self.layoutWidget = QtWidgets.QWidget(self.widget_1)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 420, 791, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.clearButton = QtWidgets.QPushButton(self.layoutWidget)
        self.clearButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-height:3em;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: white;\n"
"    color:rgb(0, 170, 255);\n"
"    border-style: inset;\n"
"}")
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.predictButton = QtWidgets.QPushButton(self.layoutWidget)
        self.predictButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-height:3em;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: white;\n"
"    color:rgb(0, 170, 255);\n"
"    border-style: inset;\n"
"}")
        self.predictButton.setObjectName("predictButton")
        self.horizontalLayout.addWidget(self.predictButton)
        self.exitButton = QtWidgets.QPushButton(self.layoutWidget)
        self.exitButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-height:3em;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: white;\n"
"    color:rgb(0, 170, 255);\n"
"    border-style: inset;\n"
"}")
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout.addWidget(self.exitButton)
        self.singleResultBroswer = QtWidgets.QTextBrowser(self.widget_1)
        self.singleResultBroswer.setGeometry(QtCore.QRect(670, 250, 161, 161))
        self.singleResultBroswer.setStyleSheet("background-color: white;\n"
"border-width: 2px;\n"
"border-color: #3D74BB;\n"
"border-style: solid;")
        self.singleResultBroswer.setObjectName("singleResultBroswer")
        self.label = QtWidgets.QLabel(self.widget_1)
        self.label.setGeometry(QtCore.QRect(40, 10, 76, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(62, 0))
        self.label.setTabletTracking(False)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setStyleSheet("QLabel{\n"
"    color:#3D74BB;\n"
"    border: 2px solid blue;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    ScaledContents: true;\n"
"}")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_1)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 76, 23))
        self.label_2.setStyleSheet("QLabel{\n"
"    color:#3D74BB;\n"
"    border: 2px solid blue;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.singleNewslineEdit = QtWidgets.QLineEdit(self.widget_1)
        self.singleNewslineEdit.setGeometry(QtCore.QRect(40, 30, 401, 51))
        self.singleNewslineEdit.setStyleSheet("background-color: white;\n"
"border-width: 2px;\n"
"border-color: #3D74BB;\n"
"border-style: solid;")
        self.singleNewslineEdit.setObjectName("singleNewslineEdit")
        self.singleLogoLabel = QtWidgets.QLabel(self.widget_1)
        self.singleLogoLabel.setGeometry(QtCore.QRect(670, 30, 161, 161))
        self.singleLogoLabel.setStyleSheet("background-color:rgb(255, 170, 0)")
        self.singleLogoLabel.setObjectName("singleLogoLabel")
        self.label_5 = QtWidgets.QLabel(self.widget_1)
        self.label_5.setGeometry(QtCore.QRect(670, 230, 76, 23))
        self.label_5.setStyleSheet("QLabel{\n"
"    color:#3D74BB;\n"
"    border: 2px solid blue;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.mainTabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget_4 = QtWidgets.QWidget(self.tab_2)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 871, 541))
        self.widget_4.setStyleSheet("table:center;")
        self.widget_4.setObjectName("widget_4")
        self.layoutWidget1 = QtWidgets.QWidget(self.widget_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 440, 621, 91))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.multiFileButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.multiFileButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    min-height: 2em;\n"
"\n"
"    padding: 6px;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: white;\n"
"    color:rgb(0, 170, 255);\n"
"    border-style: inset;\n"
"}")
        self.multiFileButton.setObjectName("multiFileButton")
        self.horizontalLayout_2.addWidget(self.multiFileButton)
        self.multiPredictButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.multiPredictButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    min-height: 2em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: white;\n"
"    color:rgb(0, 170, 255);\n"
"    border-style: inset;\n"
"}")
        self.multiPredictButton.setObjectName("multiPredictButton")
        self.horizontalLayout_2.addWidget(self.multiPredictButton)
        self.multiSaveButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.multiSaveButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    min-height: 2em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: white;\n"
"    color:rgb(0, 170, 255);\n"
"    border-style: inset;\n"
"}")
        self.multiSaveButton.setObjectName("multiSaveButton")
        self.horizontalLayout_2.addWidget(self.multiSaveButton)
        self.multiLoadingLine = QtWidgets.QProgressBar(self.widget_4)
        self.multiLoadingLine.setGeometry(QtCore.QRect(30, 390, 621, 41))
        self.multiLoadingLine.setStyleSheet("QProgressBar{\n"
"   border: 2px solid #2196F3;/*边框以及边框颜色*/\n"
"    border-radius: 5px;\n"
"    background-color: #E0E0E0;\n"
"\n"
"}\n"
"/*\n"
"QProgressBar::chunk{\n"
"    background-color: #2196F3;\n"
"    width: 10px; \n"
"    margin: 0.5px;\n"
"\n"
"}\n"
"*/")
        self.multiLoadingLine.setProperty("value", 0)
        self.multiLoadingLine.setTextVisible(False)
        self.multiLoadingLine.setObjectName("multiLoadingLine")
        self.multiNewsTable = QtWidgets.QTableWidget(self.widget_4)
        self.multiNewsTable.setGeometry(QtCore.QRect(30, 30, 621, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multiNewsTable.sizePolicy().hasHeightForWidth())
        self.multiNewsTable.setSizePolicy(sizePolicy)
        self.multiNewsTable.setStyleSheet("/*\n"
"tabelwidget*/\n"
"QTableWidget{\n"
"border:1px solid #242424;\n"
"gridline-color:#242424;\n"
"\n"
"    background-color: white;\n"
"    border-width: 2px;\n"
"    border-color: #3D74BB;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"/*选中item*/\n"
"QTableWidget::item:selected{\n"
"color:rgb(255, 255, 255);\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 rgb(0, 170, 255));\n"
"}\n"
"\n"
"/*悬浮item*/\n"
"QTableWidget::item:hover{\n"
"background:rgb(0, 170, 255);\n"
"}\n"
"/*表头*/\n"
"QHeaderView::section{\n"
"text-align:center;\n"
"font: 14px;\n"
"padding:3px;\n"
"margin:0px;\n"
"border:1px solid #242424;\n"
"border-left-width:0;\n"
"}\n"
"\n"
"")
        self.multiNewsTable.setShowGrid(True)
        self.multiNewsTable.setObjectName("multiNewsTable")
        self.multiNewsTable.setColumnCount(2)
        self.multiNewsTable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.multiNewsTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.multiNewsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.multiNewsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.multiNewsTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.multiNewsTable.setItem(0, 1, item)
        self.multiNewsTable.horizontalHeader().setDefaultSectionSize(200)
        self.multiResultsTable = QtWidgets.QTableWidget(self.widget_4)
        self.multiResultsTable.setGeometry(QtCore.QRect(680, 30, 171, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multiResultsTable.sizePolicy().hasHeightForWidth())
        self.multiResultsTable.setSizePolicy(sizePolicy)
        self.multiResultsTable.setStyleSheet("/*\n"
"tabelwidget*/\n"
"QTableWidget{\n"
"border:1px solid #242424;\n"
"gridline-color:#242424;\n"
"\n"
"    background-color: white;\n"
"    border-width: 2px;\n"
"    border-color: #3D74BB;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"/*选中item*/\n"
"QTableWidget::item:selected{\n"
"color:rgb(255, 255, 255);\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 rgb(0, 170, 255));\n"
"}\n"
"\n"
"/*悬浮item*/\n"
"QTableWidget::item:hover{\n"
"background:rgb(0, 170, 255);\n"
"}\n"
"/*表头*/\n"
"QHeaderView::section{\n"
"text-align:center;\n"
"font: 14px;\n"
"padding:3px;\n"
"margin:0px;\n"
"border:1px solid #242424;\n"
"border-left-width:0;\n"
"}\n"
"\n"
"")
        self.multiResultsTable.setShowGrid(True)
        self.multiResultsTable.setObjectName("multiResultsTable")
        self.multiResultsTable.setColumnCount(2)
        self.multiResultsTable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.multiResultsTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.multiResultsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.multiResultsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.multiResultsTable.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.multiResultsTable.setItem(0, 1, item)
        self.multiResultsTable.horizontalHeader().setDefaultSectionSize(70)
        self.mainTabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.widget_3 = QtWidgets.QWidget(self.tab_3)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 881, 551))
        self.widget_3.setObjectName("widget_3")
        self.searchButton = QtWidgets.QPushButton(self.widget_3)
        self.searchButton.setGeometry(QtCore.QRect(460, 20, 71, 41))
        self.searchButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: white;\n"
"    color:rgb(0, 170, 255);\n"
"    border-style: inset;\n"
"}")
        self.searchButton.setObjectName("searchButton")
        self.searchLineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.searchLineEdit.setGeometry(QtCore.QRect(30, 20, 421, 41))
        self.searchLineEdit.setStyleSheet("background-color: white;\n"
"border-width: 2px;\n"
"border-color: #3D74BB;\n"
"border-style: solid;")
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.searchDBTable = QtWidgets.QTableWidget(self.widget_3)
        self.searchDBTable.setGeometry(QtCore.QRect(30, 70, 821, 461))
        self.searchDBTable.setStyleSheet("/*\n"
"tabelwidget*/\n"
"QTableWidget{\n"
"border:1px solid #242424;\n"
"gridline-color:#242424;\n"
"\n"
"    background-color: white;\n"
"    border-width: 2px;\n"
"    border-color: #3D74BB;\n"
"    border-style: solid;\n"
"}\n"
"\n"
"/*选中item*/\n"
"QTableWidget::item:selected{\n"
"color:rgb(255, 255, 255);\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 rgb(0, 170, 255));\n"
"}\n"
"\n"
"/*悬浮item*/\n"
"QTableWidget::item:hover{\n"
"background:rgb(0, 170, 255);\n"
"}\n"
"/*表头*/\n"
"QHeaderView::section{\n"
"text-align:center;\n"
"font: 14px;\n"
"padding:3px;\n"
"margin:0px;\n"
"border:1px solid #242424;\n"
"border-left-width:0;\n"
"}\n"
"\n"
"")
        self.searchDBTable.setObjectName("searchDBTable")
        self.searchDBTable.setColumnCount(4)
        self.searchDBTable.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.searchDBTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.searchDBTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.searchDBTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.searchDBTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.searchDBTable.setHorizontalHeaderItem(3, item)
        self.searchDBTable.horizontalHeader().setCascadingSectionResizes(False)
        self.searchDBTable.horizontalHeader().setDefaultSectionSize(198)
        self.searchF1Button = QtWidgets.QPushButton(self.widget_3)
        self.searchF1Button.setGeometry(QtCore.QRect(780, 20, 71, 41))
        self.searchF1Button.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: white;\n"
"    color:rgb(0, 170, 255);\n"
"    border-style: inset;\n"
"}")
        self.searchF1Button.setObjectName("searchF1Button")
        self.searchClearButton = QtWidgets.QPushButton(self.widget_3)
        self.searchClearButton.setGeometry(QtCore.QRect(540, 20, 71, 41))
        self.searchClearButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: white;\n"
"    color:rgb(0, 170, 255);\n"
"    border-style: inset;\n"
"}")
        self.searchClearButton.setObjectName("searchClearButton")
        self.searchF1Result = QtWidgets.QLineEdit(self.widget_3)
        self.searchF1Result.setGeometry(QtCore.QRect(710, 20, 61, 41))
        self.searchF1Result.setStyleSheet("background-color: white;\n"
"border-width: 2px;\n"
"border-color: #3D74BB;\n"
"border-style: solid;")
        self.searchF1Result.setObjectName("searchF1Result")
        self.mainTabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.widget = QtWidgets.QWidget(self.tab_4)
        self.widget.setGeometry(QtCore.QRect(0, 10, 871, 561))
        self.widget.setObjectName("widget")
        self.wordCloudTabWidget = QtWidgets.QTabWidget(self.widget)
        self.wordCloudTabWidget.setGeometry(QtCore.QRect(320, 10, 531, 501))
        self.wordCloudTabWidget.setStyleSheet("QTabWidget::pane{\n"
"}\n"
"QTabWidget::tab-bar{\n"
"    alignment:left;\n"
"}\n"
"QTabBar::tab{\n"
"    min-width:80px;\n"
"    min-height:30px;\n"
"    font:13pt \'微软雅黑\';\n"
"    background: rgb(255, 170, 0);\n"
"    color: white;\n"
"}\n"
"QTabBar::tab:hover{\n"
"    color:rgb(255, 170, 0);\n"
"    background: white;\n"
"}\n"
"QTabBar::tab:selected{\n"
"    border-color: rgb(255, 170, 0);\n"
"    background: white;\n"
"    color: rgb(255, 170, 0);\n"
"}")
        self.wordCloudTabWidget.setObjectName("wordCloudTabWidget")
        self.WordCloudTab = QtWidgets.QWidget()
        self.WordCloudTab.setObjectName("WordCloudTab")
        self.WordCloudWidget = MatplotlibWidget(self.WordCloudTab)
        self.WordCloudWidget.setGeometry(QtCore.QRect(0, 0, 561, 491))
        self.WordCloudWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WordCloudWidget.setObjectName("WordCloudWidget")
        self.wordCloudTabWidget.addTab(self.WordCloudTab, "")
        self.WordCountTab = QtWidgets.QWidget()
        self.WordCountTab.setObjectName("WordCountTab")
        self.WordCountWidget = MatplotlibWidget(self.WordCountTab)
        self.WordCountWidget.setGeometry(QtCore.QRect(0, 0, 561, 491))
        self.WordCountWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.WordCountWidget.setObjectName("WordCountWidget")
        self.wordCloudTabWidget.addTab(self.WordCountTab, "")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 71, 41))
        self.label_3.setStyleSheet("QLabel{\n"
"    color:#3D74BB;\n"
"    border: 2px solid blue;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    font: 14px;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 71, 41))
        self.label_4.setStyleSheet("QLabel{\n"
"    color:#3D74BB;\n"
"    border: 2px solid blue;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    font: 14px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.wordCloudBox = QtWidgets.QComboBox(self.widget)
        self.wordCloudBox.setGeometry(QtCore.QRect(110, 50, 151, 31))
        self.wordCloudBox.setObjectName("wordCloudBox")
        self.wordCloudBox.addItem("")
        self.wordCloudBox.addItem("")
        self.wordCloudBox.addItem("")
        self.wordCloudBox.addItem("")
        self.wordCloudBox.addItem("")
        self.wordCloudBox.addItem("")
        self.wordCloudBox.addItem("")
        self.wordCloudBox.addItem("")
        self.wordCloudBox.addItem("")
        self.wordCloudBox.addItem("")
        self.wordCloudBox.addItem("")
        self.wordSizeBox = QtWidgets.QComboBox(self.widget)
        self.wordSizeBox.setGeometry(QtCore.QRect(110, 130, 151, 31))
        self.wordSizeBox.setObjectName("wordSizeBox")
        self.wordSizeBox.addItem("")
        self.wordSizeBox.addItem("")
        self.wordSizeBox.addItem("")
        self.wordSizeBox.addItem("")
        self.layoutWidget2 = QtWidgets.QWidget(self.widget)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 200, 231, 61))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.wordDrawButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.wordDrawButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: white;\n"
"    color:rgb(0, 170, 255);\n"
"    border-style: inset;\n"
"}")
        self.wordDrawButton.setObjectName("wordDrawButton")
        self.horizontalLayout_3.addWidget(self.wordDrawButton)
        self.wordSaveButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.wordSaveButton.setStyleSheet("QPushButton {\n"
"    color:white;\n"
"    background-color:rgb(0, 170, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: white;\n"
"    color:rgb(0, 170, 255);\n"
"    border-style: inset;\n"
"}")
        self.wordSaveButton.setObjectName("wordSaveButton")
        self.horizontalLayout_3.addWidget(self.wordSaveButton)
        self.mainTabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.widget_2 = QtWidgets.QWidget(self.tab_5)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 871, 491))
        self.widget_2.setObjectName("widget_2")
        self.introTextBrowser = QtWidgets.QTextBrowser(self.widget_2)
        self.introTextBrowser.setGeometry(QtCore.QRect(20, 30, 611, 161))
        self.introTextBrowser.setStyleSheet("background-color: white;\n"
"font: 25 16pt \"微软雅黑 Light\";\n"
"border-width: 2px;\n"
"border-color: #3D74BB;\n"
"border-style: solid;")
        self.introTextBrowser.setObjectName("introTextBrowser")
        self.introLogoLabel = QtWidgets.QLabel(self.widget_2)
        self.introLogoLabel.setGeometry(QtCore.QRect(670, 30, 161, 161))
        self.introLogoLabel.setStyleSheet("background-color: rgb(255, 170, 0)")
        self.introLogoLabel.setObjectName("introLogoLabel")
        self.mainTabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainTabWidget.setCurrentIndex(0)
        self.wordCloudTabWidget.setCurrentIndex(1)
        self.searchClearButton.clicked.connect(self.searchLineEdit.clear)
        self.searchClearButton.clicked.connect(self.searchF1Result.clear)
        self.clearButton.clicked.connect(self.singleNewsPaperEdit.clear)
        self.clearButton.clicked.connect(self.singleNewslineEdit.clear)
        self.clearButton.clicked.connect(self.singleResultBroswer.clear)
        self.exitButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Meows - 一个优雅的新闻文本【分类预测&数据分析&词云生成】软件"))
        self.singleFileButton.setText(_translate("MainWindow", "从文件导入"))
        self.predictButton2.setText(_translate("MainWindow", "->"))
        self.clearButton.setText(_translate("MainWindow", "清除全部内容"))
        self.predictButton.setText(_translate("MainWindow", "新闻文本预测"))
        self.exitButton.setText(_translate("MainWindow", "退出程序"))
        self.singleResultBroswer.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">请输入新闻</p></body></html>"))
        self.label.setText(_translate("MainWindow", "新闻标题"))
        self.label_2.setText(_translate("MainWindow", "新闻内容"))
        self.singleLogoLabel.setText(_translate("MainWindow", "LOGO"))
        self.label_5.setText(_translate("MainWindow", "预测结果"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab_1), _translate("MainWindow", "单条预测"))
        self.multiFileButton.setText(_translate("MainWindow", "导入文本"))
        self.multiPredictButton.setText(_translate("MainWindow", "批量预测"))
        self.multiSaveButton.setText(_translate("MainWindow", "导出结果"))
        item = self.multiNewsTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.multiNewsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "新闻标题"))
        item = self.multiNewsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "新闻内容"))
        __sortingEnabled = self.multiNewsTable.isSortingEnabled()
        self.multiNewsTable.setSortingEnabled(False)
        self.multiNewsTable.setSortingEnabled(__sortingEnabled)
        item = self.multiResultsTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.multiResultsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "预测分类"))
        item = self.multiResultsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "原分类"))
        __sortingEnabled = self.multiResultsTable.isSortingEnabled()
        self.multiResultsTable.setSortingEnabled(False)
        self.multiResultsTable.setSortingEnabled(__sortingEnabled)
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab_2), _translate("MainWindow", "多条预测"))
        self.searchButton.setText(_translate("MainWindow", "搜索"))
        item = self.searchDBTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.searchDBTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "预测分类"))
        item = self.searchDBTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "原分类"))
        item = self.searchDBTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "新闻标题"))
        item = self.searchDBTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "新闻内容"))
        self.searchF1Button.setText(_translate("MainWindow", "f1Score"))
        self.searchClearButton.setText(_translate("MainWindow", "清空"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab_3), _translate("MainWindow", "数据查看"))
        self.wordCloudTabWidget.setTabText(self.wordCloudTabWidget.indexOf(self.WordCloudTab), _translate("MainWindow", "词云"))
        self.wordCloudTabWidget.setTabText(self.wordCloudTabWidget.indexOf(self.WordCountTab), _translate("MainWindow", "统计"))
        self.label_3.setText(_translate("MainWindow", "选择词源"))
        self.label_4.setText(_translate("MainWindow", "选择形状"))
        self.wordCloudBox.setItemText(0, _translate("MainWindow", "所有"))
        self.wordCloudBox.setItemText(1, _translate("MainWindow", "财经"))
        self.wordCloudBox.setItemText(2, _translate("MainWindow", "房产"))
        self.wordCloudBox.setItemText(3, _translate("MainWindow", "教育"))
        self.wordCloudBox.setItemText(4, _translate("MainWindow", "科技"))
        self.wordCloudBox.setItemText(5, _translate("MainWindow", "军事"))
        self.wordCloudBox.setItemText(6, _translate("MainWindow", "汽车"))
        self.wordCloudBox.setItemText(7, _translate("MainWindow", "体育"))
        self.wordCloudBox.setItemText(8, _translate("MainWindow", "游戏"))
        self.wordCloudBox.setItemText(9, _translate("MainWindow", "娱乐"))
        self.wordCloudBox.setItemText(10, _translate("MainWindow", "其他"))
        self.wordSizeBox.setItemText(0, _translate("MainWindow", "皮卡丘"))
        self.wordSizeBox.setItemText(1, _translate("MainWindow", "猫"))
        self.wordSizeBox.setItemText(2, _translate("MainWindow", "可达鸭"))
        self.wordSizeBox.setItemText(3, _translate("MainWindow", "伊布"))
        self.wordDrawButton.setText(_translate("MainWindow", "绘制"))
        self.wordSaveButton.setText(_translate("MainWindow", "保存"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab_4), _translate("MainWindow", "数据分析"))
        self.introTextBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑 Light\'; font-size:16pt; font-weight:24; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">这里是Meows团队~</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">又是元气满满的一天呢！</p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Meow001</p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">greetings from 4 a.m.~</p></body></html>"))
        self.introLogoLabel.setText(_translate("MainWindow", "LOGO"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab_5), _translate("MainWindow", "关于我们"))
from utils.matplotlibwidget import MatplotlibWidget