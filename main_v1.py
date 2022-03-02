# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_v1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngine
from PyQt5.QtWebEngineWidgets import *
import utils


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 734)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: #15202B;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1100, 40))
        self.frame.setStyleSheet("#frame{\n"
"    border-bottom: 2px solid #38444D;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    display: flex;\n"
"    align-items: center;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(470, 10, 160, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 40, 1100, 30))
        self.frame_3.setStyleSheet("#frame_3{\n"
"    border-bottom: 1px solid #38444D;\n"
"    border-left: 1px solid #38444D;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.token_submit = QtWidgets.QPushButton(self.frame_3)
        self.token_submit.setGeometry(QtCore.QRect(990, 0, 111, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.token_submit.setFont(font)
        self.token_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.token_submit.setStyleSheet("border: None;\n"
"background-color: #1D9BF0;\n"
"color: white;")
        self.token_submit.setObjectName("token_submit")
        self.token_input = QtWidgets.QLineEdit(self.frame_3)
        self.token_input.setGeometry(QtCore.QRect(2, 1, 981, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.token_input.setFont(font)
        self.token_input.setStyleSheet("border:none;\n"
"color:white;")
        self.token_input.setObjectName("token_input")
        self.tweet = QtWidgets.QFrame(self.centralwidget)
        self.tweet.setGeometry(QtCore.QRect(0, 70, 590, 600))
        self.tweet.setStyleSheet("#tweet{\n"
"    border: 1px solid #38444D;\n"
"}")
        self.tweet.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tweet.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tweet.setObjectName("tweet")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(600, 70, 500, 30))
        self.frame_4.setStyleSheet("#frame_4\n"
"{\n"
"    border-bottom: 1px solid #38444D;\n"
"    border-left: 1px solid #38444D;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.get_tweet = QtWidgets.QPushButton(self.frame_4)
        self.get_tweet.setGeometry(QtCore.QRect(390, 0, 111, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.get_tweet.setFont(font)
        self.get_tweet.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.get_tweet.setStyleSheet("border: None;\n"
"background-color: #1D9BF0;\n"
"color: white;")
        self.get_tweet.setObjectName("get_tweet")
        self.token_input_2 = QtWidgets.QLineEdit(self.frame_4)
        self.token_input_2.setGeometry(QtCore.QRect(2, 1, 381, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.token_input_2.setFont(font)
        self.token_input_2.setStyleSheet("border:none;\n"
"color:white;")
        self.token_input_2.setObjectName("token_input_2")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(600, 100, 500, 160))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.frame_5.setFont(font)
        self.frame_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_5.setStyleSheet("#frame_5{\n"
"    border-left: 1px solid #38444D;\n"
"    border-bottom: 1px solid #38444D;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 90, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 90, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 90, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 90, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white;\n"
"")
        self.label_5.setObjectName("label_5")
        self.fo_check = QtWidgets.QCheckBox(self.frame_5)
        self.fo_check.setGeometry(QtCore.QRect(120, 10, 121, 21))
        self.fo_check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fo_check.setStyleSheet("#checkbox{\n"
"QCheckBox::indicator{ width: 100px; height: 100px;}\n"
"}")
        self.fo_check.setText("")
        self.fo_check.setObjectName("fo_check")
        self.like_check = QtWidgets.QCheckBox(self.frame_5)
        self.like_check.setGeometry(QtCore.QRect(120, 40, 121, 21))
        self.like_check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.like_check.setStyleSheet("#checkbox{\n"
"QCheckBox::indicator{ width: 100px; height: 100px;}\n"
"}")
        self.like_check.setText("")
        self.like_check.setObjectName("like_check")
        self.re_check = QtWidgets.QCheckBox(self.frame_5)
        self.re_check.setGeometry(QtCore.QRect(120, 100, 121, 21))
        self.re_check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.re_check.setStyleSheet("#checkbox{\n"
"QCheckBox::indicator{ width: 100px; height: 100px;}\n"
"}")
        self.re_check.setText("")
        self.re_check.setObjectName("re_check")
        self.co_check = QtWidgets.QCheckBox(self.frame_5)
        self.co_check.setGeometry(QtCore.QRect(120, 70, 121, 21))
        self.co_check.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.co_check.setStyleSheet("#checkbox{\n"
"QCheckBox::indicator{ width: 100px; height: 100px;}\n"
"}")
        self.co_check.setText("")
        self.co_check.setObjectName("co_check")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setGeometry(QtCore.QRect(180, 10, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: white;\n"
"")
        self.label_6.setObjectName("label_6")
        self.num_win = QtWidgets.QSpinBox(self.frame_5)
        self.num_win.setGeometry(QtCore.QRect(370, 10, 71, 22))
        self.num_win.setStyleSheet("color: white;\n"
"")
        self.num_win.setObjectName("num_win")
        self.pick = QtWidgets.QPushButton(self.frame_5)
        self.pick.setGeometry(QtCore.QRect(220, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pick.setFont(font)
        self.pick.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pick.setStyleSheet("border: None;\n"
"background-color: #1D9BF0;\n"
"color: white;\n"
"border-radius: 20px;")
        self.pick.setObjectName("pick")
        self.warn = QtWidgets.QLabel(self.frame_5)
        self.warn.setGeometry(QtCore.QRect(10, 140, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.warn.setFont(font)
        self.warn.setText("")
        self.warn.setObjectName("warn")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(600, 260, 500, 411))
        self.frame_6.setStyleSheet("#frame_6{\n"
"border-left: 1px solid #38444D;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.win_list = QtWidgets.QListView(self.frame_6)
        self.win_list.setGeometry(QtCore.QRect(0, 60, 495, 341))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.win_list.setFont(font)
        self.win_list.setStyleSheet("color: white;")
        self.win_list.setObjectName("win_list")
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: white;\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(470, 680, 160, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #38444D;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QWebEngineProfile.defaultProfile().setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)
        QtWebEngine.QtWebEngine.initialize()
        self.web = QWebEngineView(self.tweet)
        self.web.setGeometry(QtCore.QRect(0, 0, 590, 600))
        self.web.setStyleSheet("background-color: #38444D;")
        self.web.setObjectName('web')
        self.token_submit.clicked.connect(lambda: utils.set_token(self.token_input.text(), self))
        self.get_tweet.clicked.connect(lambda: utils.read_tweet(self.token_input_2.text(), self))
        self.pick.clicked.connect(lambda: utils.pick_winner(self))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Twitter LuckyPicker"))
        self.token_submit.setText(_translate("MainWindow", "Set Token"))
        self.get_tweet.setText(_translate("MainWindow", "Get Tweet"))
        self.label_2.setText(_translate("MainWindow", "Followers"))
        self.label_3.setText(_translate("MainWindow", "Like"))
        self.label_4.setText(_translate("MainWindow", "Comment"))
        self.label_5.setText(_translate("MainWindow", "Retweet"))
        self.label_6.setText(_translate("MainWindow", "Number of Winners:"))
        self.pick.setText(_translate("MainWindow", "Pick Winners"))
        self.label_7.setText(_translate("MainWindow", "Winners:"))
        self.label_8.setText(_translate("MainWindow", "Twitter: @zixi39"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedSize(1100, 734)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
