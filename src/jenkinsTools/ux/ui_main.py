# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionAdd_SSH_creds = QAction(MainWindow)
        self.actionAdd_SSH_creds.setObjectName(u"actionAdd_SSH_creds")
        self.actionWorking_with_Jenkins_Nodes = QAction(MainWindow)
        self.actionWorking_with_Jenkins_Nodes.setObjectName(u"actionWorking_with_Jenkins_Nodes")
        self.actionWorking_with_Jenkins_Pipelines = QAction(MainWindow)
        self.actionWorking_with_Jenkins_Pipelines.setObjectName(u"actionWorking_with_Jenkins_Pipelines")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sshCredsPushButton = QPushButton(self.centralwidget)
        self.sshCredsPushButton.setObjectName(u"sshCredsPushButton")
        self.sshCredsPushButton.setGeometry(QRect(560, 130, 221, 32))
        self.nodesPushButton = QPushButton(self.centralwidget)
        self.nodesPushButton.setObjectName(u"nodesPushButton")
        self.nodesPushButton.setGeometry(QRect(560, 180, 221, 32))
        self.pipelinesPushButton = QPushButton(self.centralwidget)
        self.pipelinesPushButton.setObjectName(u"pipelinesPushButton")
        self.pipelinesPushButton.setGeometry(QRect(560, 230, 221, 32))
        self.quitPushButton = QPushButton(self.centralwidget)
        self.quitPushButton.setObjectName(u"quitPushButton")
        self.quitPushButton.setGeometry(QRect(680, 290, 100, 32))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 40, 511, 441))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.menuAction = QMenu(self.menubar)
        self.menuAction.setObjectName(u"menuAction")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAction.menuAction())
        self.menuAction.addAction(self.actionAdd_SSH_creds)
        self.menuAction.addAction(self.actionWorking_with_Jenkins_Nodes)
        self.menuAction.addAction(self.actionWorking_with_Jenkins_Pipelines)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd_SSH_creds.setText(QCoreApplication.translate("MainWindow", u"Add SSH creds", None))
        self.actionWorking_with_Jenkins_Nodes.setText(QCoreApplication.translate("MainWindow", u"Working with Jenkins Nodes", None))
        self.actionWorking_with_Jenkins_Pipelines.setText(QCoreApplication.translate("MainWindow", u"Working with Jenkins Pipelines", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.sshCredsPushButton.setText(QCoreApplication.translate("MainWindow", u"Add SSH creds", None))
        self.nodesPushButton.setText(QCoreApplication.translate("MainWindow", u"Working with Jenkins Nodes", None))
        self.pipelinesPushButton.setText(QCoreApplication.translate("MainWindow", u"Working with Jenkins Pipelines", None))
        self.quitPushButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.menuAction.setTitle(QCoreApplication.translate("MainWindow", u"Action", None))
    # retranslateUi

