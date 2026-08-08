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
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTextEdit, QWidget)

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
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 80, 751, 441))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.sshCredsPushButton = QPushButton(self.layoutWidget)
        self.sshCredsPushButton.setObjectName(u"sshCredsPushButton")

        self.gridLayout.addWidget(self.sshCredsPushButton, 1, 1, 1, 1)

        self.textEdit = QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 0, 6, 1)

        self.quitPushButton = QPushButton(self.layoutWidget)
        self.quitPushButton.setObjectName(u"quitPushButton")

        self.gridLayout.addWidget(self.quitPushButton, 5, 1, 1, 1)

        self.nodesPushButton = QPushButton(self.layoutWidget)
        self.nodesPushButton.setObjectName(u"nodesPushButton")

        self.gridLayout.addWidget(self.nodesPushButton, 2, 1, 1, 1)

        self.pipelinesPushButton = QPushButton(self.layoutWidget)
        self.pipelinesPushButton.setObjectName(u"pipelinesPushButton")

        self.gridLayout.addWidget(self.pipelinesPushButton, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

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
        self.sshCredsPushButton.setText(QCoreApplication.translate("MainWindow", u"Add SSH creds", None))
        self.quitPushButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.nodesPushButton.setText(QCoreApplication.translate("MainWindow", u"Working with Jenkins Nodes", None))
        self.pipelinesPushButton.setText(QCoreApplication.translate("MainWindow", u"Working with Jenkins Pipelines", None))
        self.menuAction.setTitle(QCoreApplication.translate("MainWindow", u"Action", None))
    # retranslateUi

