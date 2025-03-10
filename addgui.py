# -*- coding: utf-8 -*-

# from PyQt5 import QtCore, QtGui, QtWidgets
from aqt.qt import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("AddRule")
        Form.setFixedSize(540, 109)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 521, 91))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.originalLE = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.originalLE.setObjectName("originalLE")
        self.gridLayout_5.addWidget(self.originalLE, 0, 1, 1, 1)
        self.overwriteLE = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.overwriteLE.setObjectName("overwriteLE")
        self.gridLayout_5.addWidget(self.overwriteLE, 0, 3, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.horizontalLayout_4.addStretch(1)
        self.listCount = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.listCount.setObjectName("listCount")
        self.horizontalLayout_4.addWidget(self.listCount)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 1, 0, 1, 4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ncAddCB = QtWidgets.QCheckBox(self.gridLayoutWidget_4)
        self.ncAddCB.setObjectName("ncAddCB")
        self.horizontalLayout_6.addWidget(self.ncAddCB)
        self.lcAddCB = QtWidgets.QCheckBox(self.gridLayoutWidget_4)
        self.lcAddCB.setObjectName("lcAddCB")
        self.horizontalLayout_6.addWidget(self.lcAddCB)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 2, 0, 1, 3)
        self.addRuleButton = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.addRuleButton.setObjectName("addRuleButton")
        self.gridLayout_5.addWidget(self.addRuleButton, 2, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "New Parsing Overwrite Rule"))
        self.label_4.setText(_translate("Form", "Overwrite"))
        self.label.setText(_translate("Form", "Original"))
        self.label_11.setText(_translate("Form", "Apply Rule to current collection:"))
        self.ncAddCB.setText(_translate("Form", "New Cards"))
        self.lcAddCB.setText(_translate("Form", "Learned Cards"))
        self.addRuleButton.setText(_translate("Form", "Add"))

