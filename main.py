# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 787)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(350, 150, 431, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.title.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.title.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("color: white\n"
"")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.backtest_ui_Btn = QtWidgets.QPushButton(self.centralwidget)
        self.backtest_ui_Btn.setGeometry(QtCore.QRect(440, 340, 261, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.backtest_ui_Btn.setFont(font)
        self.backtest_ui_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backtest_ui_Btn.setStyleSheet("QPushButton{\n"
"background:#6699CC;\n"
"color:#fff;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid #DEF748;\n"
"background:#66A6FF;\n"
"}")
        self.backtest_ui_Btn.setObjectName("backtest_ui_Btn")
        self.prediction_ui_btn = QtWidgets.QPushButton(self.centralwidget)
        self.prediction_ui_btn.setGeometry(QtCore.QRect(440, 420, 261, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.prediction_ui_btn.setFont(font)
        self.prediction_ui_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prediction_ui_btn.setStyleSheet("QPushButton{\n"
"background:#6699CC;\n"
"color:#fff;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid #DEF748;\n"
"background:#66A6FF;\n"
"}")
        self.prediction_ui_btn.setObjectName("prediction_ui_btn")
        self.descripe_ui_btn = QtWidgets.QPushButton(self.centralwidget)
        self.descripe_ui_btn.setGeometry(QtCore.QRect(440, 500, 261, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.descripe_ui_btn.setFont(font)
        self.descripe_ui_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.descripe_ui_btn.setStyleSheet("QPushButton{\n"
"background:#6699CC;\n"
"color:#fff;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid #DEF748;\n"
"background:#66A6FF;\n"
"}")
        self.descripe_ui_btn.setObjectName("descripe_ui_btn")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(350, 110, 441, 511))
        self.frame.setStyleSheet("background:rgba(0,0,0,0.7);\n"
"border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1121, 791))
        self.frame_2.setStyleSheet("border-image: url(\"homeimage.jpeg\");\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.raise_()
        self.frame.raise_()
        self.backtest_ui_Btn.raise_()
        self.prediction_ui_btn.raise_()
        self.descripe_ui_btn.raise_()
        self.title.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "股票系統"))
        self.backtest_ui_Btn.setText(_translate("MainWindow", "回測系統"))
        self.prediction_ui_btn.setText(_translate("MainWindow", "預測系統"))
        self.descripe_ui_btn.setText(_translate("MainWindow", "簡介"))

