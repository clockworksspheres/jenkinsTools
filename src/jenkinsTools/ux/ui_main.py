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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionSSH_creds_wrangling = QAction(MainWindow)
        self.actionSSH_creds_wrangling.setObjectName(u"actionSSH_creds_wrangling")
        self.actionWorking_with_Jenkins_Nodes = QAction(MainWindow)
        self.actionWorking_with_Jenkins_Nodes.setObjectName(u"actionWorking_with_Jenkins_Nodes")
        self.actionWorking_with_Jenkins_Pipelines = QAction(MainWindow)
        self.actionWorking_with_Jenkins_Pipelines.setObjectName(u"actionWorking_with_Jenkins_Pipelines")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.quitPushButton = QPushButton(self.centralwidget)
        self.quitPushButton.setObjectName(u"quitPushButton")

        self.gridLayout.addWidget(self.quitPushButton, 5, 1, 1, 1)

        self.pipelinesPushButton = QPushButton(self.centralwidget)
        self.pipelinesPushButton.setObjectName(u"pipelinesPushButton")

        self.gridLayout.addWidget(self.pipelinesPushButton, 3, 1, 1, 1)

        self.nodesPushButton = QPushButton(self.centralwidget)
        self.nodesPushButton.setObjectName(u"nodesPushButton")

        self.gridLayout.addWidget(self.nodesPushButton, 2, 1, 1, 1)

        self.sshCredsPushButton = QPushButton(self.centralwidget)
        self.sshCredsPushButton.setObjectName(u"sshCredsPushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sshCredsPushButton.sizePolicy().hasHeightForWidth())
        self.sshCredsPushButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.sshCredsPushButton, 1, 1, 1, 1)

        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout.addWidget(self.textBrowser, 0, 0, 6, 1)

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
        self.menuAction.addAction(self.actionSSH_creds_wrangling)
        self.menuAction.addAction(self.actionWorking_with_Jenkins_Nodes)
        self.menuAction.addAction(self.actionWorking_with_Jenkins_Pipelines)
        self.menuAction.addSeparator()
        self.menuAction.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSSH_creds_wrangling.setText(QCoreApplication.translate("MainWindow", u"Add SSH creds", None))
        self.actionWorking_with_Jenkins_Nodes.setText(QCoreApplication.translate("MainWindow", u"Working with Jenkins Nodes", None))
        self.actionWorking_with_Jenkins_Pipelines.setText(QCoreApplication.translate("MainWindow", u"Working with Jenkins Pipelines", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.quitPushButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.pipelinesPushButton.setText(QCoreApplication.translate("MainWindow", u"Working with Jenkins Pipelines", None))
        self.nodesPushButton.setText(QCoreApplication.translate("MainWindow", u"Working with Jenkins Nodes", None))
        self.sshCredsPushButton.setText(QCoreApplication.translate("MainWindow", u"Add SSH creds", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Show debug messages", None))
        self.menuAction.setTitle(QCoreApplication.translate("MainWindow", u"Action", None))
    # retranslateUi

