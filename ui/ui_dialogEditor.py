# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dialogEditor(object):
    def setupUi(self, dialogEditor):
        if not dialogEditor.objectName():
            dialogEditor.setObjectName(u"dialogEditor")
        dialogEditor.setWindowModality(Qt.ApplicationModal)
        dialogEditor.resize(400, 300)
        dialogEditor.setAcceptDrops(False)
        self.verticalLayout = QVBoxLayout(dialogEditor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblKey = QLabel(dialogEditor)
        self.lblKey.setObjectName(u"lblKey")

        self.verticalLayout.addWidget(self.lblKey)

        self.keyEdit = QLineEdit(dialogEditor)
        self.keyEdit.setObjectName(u"keyEdit")

        self.verticalLayout.addWidget(self.keyEdit)

        self.lblValue = QLabel(dialogEditor)
        self.lblValue.setObjectName(u"lblValue")

        self.verticalLayout.addWidget(self.lblValue)

        self.valueEdit = QTextEdit(dialogEditor)
        self.valueEdit.setObjectName(u"valueEdit")

        self.verticalLayout.addWidget(self.valueEdit)

        self.buttonBox = QDialogButtonBox(dialogEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(dialogEditor)
        self.buttonBox.accepted.connect(dialogEditor.accept)
        self.buttonBox.rejected.connect(dialogEditor.reject)

        QMetaObject.connectSlotsByName(dialogEditor)
    # setupUi

    def retranslateUi(self, dialogEditor):
        dialogEditor.setWindowTitle(QCoreApplication.translate("dialogEditor", u"\u7f16\u8f91\u5b57\u6bb5", None))
        self.lblKey.setText(QCoreApplication.translate("dialogEditor", u"\u5b57\u6bb5\u540d", None))
        self.lblValue.setText(QCoreApplication.translate("dialogEditor", u"\u952e\u503c", None))
    # retranslateUi

