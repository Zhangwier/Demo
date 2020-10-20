# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '1jxSPqb.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(851, 766)
        self.Time_2 = QAction(MainWindow)
        self.Time_2.setObjectName(u"Time_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Main_group = QGroupBox(self.centralwidget)
        self.Main_group.setObjectName(u"Main_group")
        self.Main_group.setGeometry(QRect(0, 0, 841, 591))
        self.Library_screen_goto = QPushButton(self.Main_group)
        self.Library_screen_goto.setObjectName(u"Library_screen_goto")
        self.Library_screen_goto.setGeometry(QRect(50, 350, 171, 61))
        self.Setting_screen_goto = QPushButton(self.Main_group)
        self.Setting_screen_goto.setObjectName(u"Setting_screen_goto")
        self.Setting_screen_goto.setGeometry(QRect(50, 440, 171, 61))
        self.Time_show = QLCDNumber(self.Main_group)
        self.Time_show.setObjectName(u"Time_show")
        self.Time_show.setGeometry(QRect(580, 480, 231, 81))
        self.Time_show.setStyleSheet(u"font: 9pt \"Constantia\";")
        self.logs_screen_goto = QPushButton(self.Main_group)
        self.logs_screen_goto.setObjectName(u"logs_screen_goto")
        self.logs_screen_goto.setGeometry(QRect(50, 260, 171, 61))
        self.schedule_screen_goto = QPushButton(self.Main_group)
        self.schedule_screen_goto.setObjectName(u"schedule_screen_goto")
        self.schedule_screen_goto.setGeometry(QRect(50, 170, 171, 61))
        self.Libr_screen = QScrollArea(self.Main_group)
        self.Libr_screen.setObjectName(u"Libr_screen")
        self.Libr_screen.setGeometry(QRect(0, 0, 851, 591))
        self.Libr_screen.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 849, 589))
        self.open_lib = QPushButton(self.scrollAreaWidgetContents_2)
        self.open_lib.setObjectName(u"open_lib")
        self.open_lib.setGeometry(QRect(30, 230, 181, 61))
        self.save_library = QPushButton(self.scrollAreaWidgetContents_2)
        self.save_library.setObjectName(u"save_library")
        self.save_library.setGeometry(QRect(30, 330, 181, 61))
        self.reload_library = QPushButton(self.scrollAreaWidgetContents_2)
        self.reload_library.setObjectName(u"reload_library")
        self.reload_library.setGeometry(QRect(30, 430, 181, 61))
        self.lib_show = QTextEdit(self.scrollAreaWidgetContents_2)
        self.lib_show.setObjectName(u"lib_show")
        self.lib_show.setGeometry(QRect(300, 90, 481, 431))
        self.find_txt_lib = QPushButton(self.scrollAreaWidgetContents_2)
        self.find_txt_lib.setObjectName(u"find_txt_lib")
        self.find_txt_lib.setGeometry(QRect(300, 60, 91, 31))
        self.find_txt_lib_input = QLineEdit(self.scrollAreaWidgetContents_2)
        self.find_txt_lib_input.setObjectName(u"find_txt_lib_input")
        self.find_txt_lib_input.setGeometry(QRect(390, 60, 141, 31))
        self.seeting_screen = QTabWidget(self.scrollAreaWidgetContents_2)
        self.seeting_screen.setObjectName(u"seeting_screen")
        self.seeting_screen.setGeometry(QRect(0, 0, 851, 591))
        self.seeting_screenPage1 = QWidget()
        self.seeting_screenPage1.setObjectName(u"seeting_screenPage1")
        self.seeting_screen.addTab(self.seeting_screenPage1, "")
        self.seeting_screenPage2 = QWidget()
        self.seeting_screenPage2.setObjectName(u"seeting_screenPage2")
        self.Save_adr = QPushButton(self.seeting_screenPage2)
        self.Save_adr.setObjectName(u"Save_adr")
        self.Save_adr.setGeometry(QRect(310, 430, 141, 51))
        self.adr = QLineEdit(self.seeting_screenPage2)
        self.adr.setObjectName(u"adr")
        self.adr.setGeometry(QRect(280, 60, 281, 41))
        self.schedule_adr_2 = QLineEdit(self.seeting_screenPage2)
        self.schedule_adr_2.setObjectName(u"schedule_adr_2")
        self.schedule_adr_2.setGeometry(QRect(280, 140, 281, 41))
        self.library_adr = QLineEdit(self.seeting_screenPage2)
        self.library_adr.setObjectName(u"library_adr")
        self.library_adr.setGeometry(QRect(280, 210, 281, 41))
        self.learn_adr_2 = QLineEdit(self.seeting_screenPage2)
        self.learn_adr_2.setObjectName(u"learn_adr_2")
        self.learn_adr_2.setGeometry(QRect(280, 280, 281, 41))
        self.label_2 = QLabel(self.seeting_screenPage2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 60, 121, 31))
        self.schedule_adr = QLabel(self.seeting_screenPage2)
        self.schedule_adr.setObjectName(u"schedule_adr")
        self.schedule_adr.setGeometry(QRect(131, 144, 121, 31))
        self.Library_adr = QLabel(self.seeting_screenPage2)
        self.Library_adr.setObjectName(u"Library_adr")
        self.Library_adr.setGeometry(QRect(131, 214, 121, 31))
        self.learn_adr = QLabel(self.seeting_screenPage2)
        self.learn_adr.setObjectName(u"learn_adr")
        self.learn_adr.setGeometry(QRect(130, 280, 121, 31))
        self.seeting_screen.addTab(self.seeting_screenPage2, "")
        self.seeting_screenPage3 = QWidget()
        self.seeting_screenPage3.setObjectName(u"seeting_screenPage3")
        self.label = QLabel(self.seeting_screenPage3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 30, 111, 51))
        self.textBrowser = QTextBrowser(self.seeting_screenPage3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(50, 90, 741, 321))
        self.Email = QPushButton(self.seeting_screenPage3)
        self.Email.setObjectName(u"Email")
        self.Email.setGeometry(QRect(50, 440, 281, 41))
        self.Other = QPushButton(self.seeting_screenPage3)
        self.Other.setObjectName(u"Other")
        self.Other.setGeometry(QRect(480, 440, 311, 41))
        self.seeting_screen.addTab(self.seeting_screenPage3, "")
        self.Libr_screen.setWidget(self.scrollAreaWidgetContents_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 851, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.seeting_screen.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Time_2.setText(QCoreApplication.translate("MainWindow", u"GetTime", None))
        self.Main_group.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.Library_screen_goto.setText(QCoreApplication.translate("MainWindow", u"Library dir", None))
        self.Setting_screen_goto.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.logs_screen_goto.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.schedule_screen_goto.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.open_lib.setText(QCoreApplication.translate("MainWindow", u"Open library", None))
        self.save_library.setText(QCoreApplication.translate("MainWindow", u"Save library", None))
        self.reload_library.setText(QCoreApplication.translate("MainWindow", u"Reload library", None))
        self.find_txt_lib.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.seeting_screen.setTabText(self.seeting_screen.indexOf(self.seeting_screenPage1), "")
        self.Save_adr.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.adr.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"adr", None))
        self.schedule_adr.setText(QCoreApplication.translate("MainWindow", u"Schedule_adr", None))
        self.Library_adr.setText(QCoreApplication.translate("MainWindow", u"Library_adr", None))
        self.learn_adr.setText(QCoreApplication.translate("MainWindow", u"Learn_adr", None))
        self.seeting_screen.setTabText(self.seeting_screen.indexOf(self.seeting_screenPage2), "")
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.Email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.Other.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.seeting_screen.setTabText(self.seeting_screen.indexOf(self.seeting_screenPage3), "")
    # retranslateUi


"""                                                     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    label = QLabel("Hello World")
    label.show()
    sys.exit(app.exec_())


"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
#"""