# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'postman.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 1200)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widgetReq = QWidget(self.centralwidget)
        self.widgetReq.setObjectName(u"widgetReq")
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        font.setPointSize(10)
        self.widgetReq.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.widgetReq)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.comboMethod = QComboBox(self.widgetReq)
        self.comboMethod.addItem("")
        self.comboMethod.addItem("")
        self.comboMethod.setObjectName(u"comboMethod")
        self.comboMethod.setFont(font)

        self.horizontalLayout.addWidget(self.comboMethod)

        self.textURL = QLineEdit(self.widgetReq)
        self.textURL.setObjectName(u"textURL")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textURL.sizePolicy().hasHeightForWidth())
        self.textURL.setSizePolicy(sizePolicy)
        self.textURL.setFont(font)

        self.horizontalLayout.addWidget(self.textURL)

        self.btnSend = QPushButton(self.widgetReq)
        self.btnSend.setObjectName(u"btnSend")
        self.btnSend.setFont(font)

        self.horizontalLayout.addWidget(self.btnSend)


        self.verticalLayout.addWidget(self.widgetReq)

        self.widgetPayload = QWidget(self.centralwidget)
        self.widgetPayload.setObjectName(u"widgetPayload")
        self.widgetPayload.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.widgetPayload)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widgetHeader = QWidget(self.widgetPayload)
        self.widgetHeader.setObjectName(u"widgetHeader")
        self.widgetHeader.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.widgetHeader)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Toolbar = QHBoxLayout()
        self.Toolbar.setObjectName(u"Toolbar")
        self.lblHeader = QLabel(self.widgetHeader)
        self.lblHeader.setObjectName(u"lblHeader")
        self.lblHeader.setFont(font)

        self.Toolbar.addWidget(self.lblHeader)

        self.btnAdd = QPushButton(self.widgetHeader)
        self.btnAdd.setObjectName(u"btnAdd")
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.btnAdd.setFont(font1)

        self.Toolbar.addWidget(self.btnAdd)

        self.btnRemove = QPushButton(self.widgetHeader)
        self.btnRemove.setObjectName(u"btnRemove")
        self.btnRemove.setFont(font1)

        self.Toolbar.addWidget(self.btnRemove)


        self.verticalLayout_3.addLayout(self.Toolbar)

        self.table = QTableView(self.widgetHeader)
        self.table.setObjectName(u"table")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy1)
        self.table.setFont(font)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setTextElideMode(Qt.ElideLeft)
        self.table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_3.addWidget(self.table)


        self.horizontalLayout_2.addWidget(self.widgetHeader)

        self.line_2 = QFrame(self.widgetPayload)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.widgetBody = QWidget(self.widgetPayload)
        self.widgetBody.setObjectName(u"widgetBody")
        self.widgetBody.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.widgetBody)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lblBody = QLabel(self.widgetBody)
        self.lblBody.setObjectName(u"lblBody")
        self.lblBody.setFont(font)

        self.verticalLayout_2.addWidget(self.lblBody)

        self.textBody = QTextEdit(self.widgetBody)
        self.textBody.setObjectName(u"textBody")
        sizePolicy1.setHeightForWidth(self.textBody.sizePolicy().hasHeightForWidth())
        self.textBody.setSizePolicy(sizePolicy1)
        self.textBody.setFont(font)

        self.verticalLayout_2.addWidget(self.textBody)


        self.horizontalLayout_2.addWidget(self.widgetBody)


        self.verticalLayout.addWidget(self.widgetPayload)

        self.line_1 = QFrame(self.centralwidget)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setFont(font)
        self.line_1.setFrameShape(QFrame.HLine)
        self.line_1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_1)

        self.widgetRes = QWidget(self.centralwidget)
        self.widgetRes.setObjectName(u"widgetRes")
        self.widgetRes.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.widgetRes)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.textResp = QTextEdit(self.widgetRes)
        self.textResp.setObjectName(u"textResp")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textResp.sizePolicy().hasHeightForWidth())
        self.textResp.setSizePolicy(sizePolicy2)
        self.textResp.setFont(font)

        self.verticalLayout_4.addWidget(self.textResp)

        self.btnClear = QPushButton(self.widgetRes)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnClear.sizePolicy().hasHeightForWidth())
        self.btnClear.setSizePolicy(sizePolicy3)
        self.btnClear.setFont(font)

        self.verticalLayout_4.addWidget(self.btnClear, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.widgetRes)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.comboMethod.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.comboMethod.setItemText(0, QCoreApplication.translate("MainWindow", u"GET", None))
        self.comboMethod.setItemText(1, QCoreApplication.translate("MainWindow", u"POST", None))

        self.comboMethod.setCurrentText(QCoreApplication.translate("MainWindow", u"GET", None))
        self.btnSend.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.lblHeader.setText(QCoreApplication.translate("MainWindow", u"\u6d88\u606f\u5934", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btnRemove.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lblBody.setText(QCoreApplication.translate("MainWindow", u"\u6d88\u606f\u4f53", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
    # retranslateUi

