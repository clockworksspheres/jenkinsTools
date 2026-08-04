# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pipelinesDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QStackedWidget, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(782, 529)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 60, 741, 451))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.UsernameLabel = QLabel(self.layoutWidget)
        self.UsernameLabel.setObjectName(u"UsernameLabel")

        self.gridLayout.addWidget(self.UsernameLabel, 1, 0, 1, 1)

        self.tokenLineEdit = QLineEdit(self.layoutWidget)
        self.tokenLineEdit.setObjectName(u"tokenLineEdit")

        self.gridLayout.addWidget(self.tokenLineEdit, 2, 1, 1, 1)

        self.tokenLabel = QLabel(self.layoutWidget)
        self.tokenLabel.setObjectName(u"tokenLabel")

        self.gridLayout.addWidget(self.tokenLabel, 2, 0, 1, 1)

        self.ActionLabel = QLabel(self.layoutWidget)
        self.ActionLabel.setObjectName(u"ActionLabel")

        self.gridLayout.addWidget(self.ActionLabel, 3, 0, 1, 1)

        self.ActionComboBox = QComboBox(self.layoutWidget)
        self.ActionComboBox.addItem("")
        self.ActionComboBox.addItem("")
        self.ActionComboBox.addItem("")
        self.ActionComboBox.addItem("")
        self.ActionComboBox.addItem("")
        self.ActionComboBox.setObjectName(u"ActionComboBox")

        self.gridLayout.addWidget(self.ActionComboBox, 3, 1, 1, 1)

        self.MethodComboBox = QComboBox(self.layoutWidget)
        self.MethodComboBox.addItem("")
        self.MethodComboBox.addItem("")
        self.MethodComboBox.setObjectName(u"MethodComboBox")

        self.gridLayout.addWidget(self.MethodComboBox, 3, 3, 1, 1)

        self.QuitPushButton = QPushButton(self.layoutWidget)
        self.QuitPushButton.setObjectName(u"QuitPushButton")

        self.gridLayout.addWidget(self.QuitPushButton, 5, 3, 1, 1)

        self.UsernameLineEdit = QLineEdit(self.layoutWidget)
        self.UsernameLineEdit.setObjectName(u"UsernameLineEdit")

        self.gridLayout.addWidget(self.UsernameLineEdit, 1, 1, 1, 1)

        self.RunPushButton = QPushButton(self.layoutWidget)
        self.RunPushButton.setObjectName(u"RunPushButton")

        self.gridLayout.addWidget(self.RunPushButton, 5, 4, 1, 1)

        self.UrlLineEdit = QLineEdit(self.layoutWidget)
        self.UrlLineEdit.setObjectName(u"UrlLineEdit")

        self.gridLayout.addWidget(self.UrlLineEdit, 0, 1, 1, 1)

        self.UrlLabel = QLabel(self.layoutWidget)
        self.UrlLabel.setObjectName(u"UrlLabel")

        self.gridLayout.addWidget(self.UrlLabel, 0, 0, 1, 1)

        self.MethodLabel = QLabel(self.layoutWidget)
        self.MethodLabel.setObjectName(u"MethodLabel")

        self.gridLayout.addWidget(self.MethodLabel, 3, 2, 1, 1)

        self.stackedWidget = QStackedWidget(self.layoutWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.jobNamelabel = QLabel(self.page)
        self.jobNamelabel.setObjectName(u"jobNamelabel")
        self.jobNamelabel.setGeometry(QRect(10, 60, 121, 16))
        self.descriptionLabel = QLabel(self.page)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setGeometry(QRect(380, 90, 91, 16))
        self.repoLabel = QLabel(self.page)
        self.repoLabel.setObjectName(u"repoLabel")
        self.repoLabel.setGeometry(QRect(10, 90, 121, 16))
        self.credsIdLabel = QLabel(self.page)
        self.credsIdLabel.setObjectName(u"credsIdLabel")
        self.credsIdLabel.setGeometry(QRect(380, 60, 91, 16))
        self.branchLabel = QLabel(self.page)
        self.branchLabel.setObjectName(u"branchLabel")
        self.branchLabel.setGeometry(QRect(10, 120, 121, 16))
        self.jenkinsfileLabel = QLabel(self.page)
        self.jenkinsfileLabel.setObjectName(u"jenkinsfileLabel")
        self.jenkinsfileLabel.setGeometry(QRect(10, 150, 121, 16))
        self.scriptLabel = QLabel(self.page)
        self.scriptLabel.setObjectName(u"scriptLabel")
        self.scriptLabel.setGeometry(QRect(380, 120, 91, 16))
        self.scriptPathLabel = QLabel(self.page)
        self.scriptPathLabel.setObjectName(u"scriptPathLabel")
        self.scriptPathLabel.setGeometry(QRect(380, 150, 91, 16))
        self.jobNameLineEdit = QLineEdit(self.page)
        self.jobNameLineEdit.setObjectName(u"jobNameLineEdit")
        self.jobNameLineEdit.setGeometry(QRect(152, 60, 191, 20))
        self.repoLineEdit = QLineEdit(self.page)
        self.repoLineEdit.setObjectName(u"repoLineEdit")
        self.repoLineEdit.setGeometry(QRect(152, 90, 191, 20))
        self.branchLineEdit = QLineEdit(self.page)
        self.branchLineEdit.setObjectName(u"branchLineEdit")
        self.branchLineEdit.setGeometry(QRect(152, 120, 191, 20))
        self.jenkinsfileLineEdit = QLineEdit(self.page)
        self.jenkinsfileLineEdit.setObjectName(u"jenkinsfileLineEdit")
        self.jenkinsfileLineEdit.setGeometry(QRect(152, 150, 191, 20))
        self.credsIdLineEdit = QLineEdit(self.page)
        self.credsIdLineEdit.setObjectName(u"credsIdLineEdit")
        self.credsIdLineEdit.setGeometry(QRect(490, 60, 231, 20))
        self.descriptionLineEdit = QLineEdit(self.page)
        self.descriptionLineEdit.setObjectName(u"descriptionLineEdit")
        self.descriptionLineEdit.setGeometry(QRect(490, 90, 231, 20))
        self.scriptLineEdit = QLineEdit(self.page)
        self.scriptLineEdit.setObjectName(u"scriptLineEdit")
        self.scriptLineEdit.setGeometry(QRect(490, 120, 231, 20))
        self.scriptPathLineEdit = QLineEdit(self.page)
        self.scriptPathLineEdit.setObjectName(u"scriptPathLineEdit")
        self.scriptPathLineEdit.setGeometry(QRect(490, 150, 231, 20))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.JobNameLineEdit_2 = QLineEdit(self.page_2)
        self.JobNameLineEdit_2.setObjectName(u"JobNameLineEdit_2")
        self.JobNameLineEdit_2.setGeometry(QRect(160, 50, 351, 20))
        self.followLabel = QLabel(self.page_2)
        self.followLabel.setObjectName(u"followLabel")
        self.followLabel.setGeometry(QRect(10, 90, 141, 16))
        self.parametersLineEdit_2 = QLineEdit(self.page_2)
        self.parametersLineEdit_2.setObjectName(u"parametersLineEdit_2")
        self.parametersLineEdit_2.setGeometry(QRect(160, 120, 351, 20))
        self.JobNameLabel_2 = QLabel(self.page_2)
        self.JobNameLabel_2.setObjectName(u"JobNameLabel_2")
        self.JobNameLabel_2.setGeometry(QRect(10, 50, 91, 16))
        self.parametersLabel_2 = QLabel(self.page_2)
        self.parametersLabel_2.setObjectName(u"parametersLabel_2")
        self.parametersLabel_2.setGeometry(QRect(10, 120, 91, 16))
        self.tokenBuildLabel_2 = QLabel(self.page_2)
        self.tokenBuildLabel_2.setObjectName(u"tokenBuildLabel_2")
        self.tokenBuildLabel_2.setGeometry(QRect(10, 150, 91, 16))
        self.tokenBuildLineEdit_2 = QLineEdit(self.page_2)
        self.tokenBuildLineEdit_2.setObjectName(u"tokenBuildLineEdit_2")
        self.tokenBuildLineEdit_2.setGeometry(QRect(160, 150, 351, 20))
        self.followComboBox = QComboBox(self.page_2)
        self.followComboBox.addItem("")
        self.followComboBox.addItem("")
        self.followComboBox.setObjectName(u"followComboBox")
        self.followComboBox.setGeometry(QRect(160, 80, 103, 32))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.GetNodesTextEdit = QTextEdit(self.page_3)
        self.GetNodesTextEdit.setObjectName(u"GetNodesTextEdit")
        self.GetNodesTextEdit.setGeometry(QRect(20, 10, 671, 241))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.jobNameLabel_3 = QLabel(self.page_4)
        self.jobNameLabel_3.setObjectName(u"jobNameLabel_3")
        self.jobNameLabel_3.setGeometry(QRect(10, 60, 71, 16))
        self.jobNameLineEdit_3 = QLineEdit(self.page_4)
        self.jobNameLineEdit_3.setObjectName(u"jobNameLineEdit_3")
        self.jobNameLineEdit_3.setGeometry(QRect(100, 60, 181, 20))
        self.GetNodeTextEdit = QTextEdit(self.page_4)
        self.GetNodeTextEdit.setObjectName(u"GetNodeTextEdit")
        self.GetNodeTextEdit.setGeometry(QRect(10, 100, 701, 151))
        self.xmlFileLineEdit = QLineEdit(self.page_4)
        self.xmlFileLineEdit.setObjectName(u"xmlFileLineEdit")
        self.xmlFileLineEdit.setGeometry(QRect(452, 60, 261, 21))
        self.xmlFileLabel = QLabel(self.page_4)
        self.xmlFileLabel.setObjectName(u"xmlFileLabel")
        self.xmlFileLabel.setGeometry(QRect(330, 60, 111, 16))
        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout.addWidget(self.stackedWidget, 4, 0, 1, 5)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 20, 171, 31))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.UsernameLabel.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.tokenLabel.setText(QCoreApplication.translate("Dialog", u"Token/Password", None))
        self.ActionLabel.setText(QCoreApplication.translate("Dialog", u"Action", None))
        self.ActionComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"create", None))
        self.ActionComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"run", None))
        self.ActionComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"check", None))
        self.ActionComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"get-config", None))
        self.ActionComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"set-config", None))

        self.MethodComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"scm", None))
        self.MethodComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"inline", None))

        self.QuitPushButton.setText(QCoreApplication.translate("Dialog", u"quit", None))
        self.RunPushButton.setText(QCoreApplication.translate("Dialog", u"run command", None))
        self.UrlLabel.setText(QCoreApplication.translate("Dialog", u"URL", None))
        self.MethodLabel.setText(QCoreApplication.translate("Dialog", u"Type", None))
        self.jobNamelabel.setText(QCoreApplication.translate("Dialog", u"Job Name", None))
        self.descriptionLabel.setText(QCoreApplication.translate("Dialog", u"Description", None))
        self.repoLabel.setText(QCoreApplication.translate("Dialog", u"Repo", None))
        self.credsIdLabel.setText(QCoreApplication.translate("Dialog", u"Credentials ID", None))
        self.branchLabel.setText(QCoreApplication.translate("Dialog", u"Branch", None))
        self.jenkinsfileLabel.setText(QCoreApplication.translate("Dialog", u"Jenkinsfile", None))
        self.scriptLabel.setText(QCoreApplication.translate("Dialog", u"Script", None))
        self.scriptPathLabel.setText(QCoreApplication.translate("Dialog", u"Script Path", None))
        self.descriptionLineEdit.setText("")
        self.followLabel.setText(QCoreApplication.translate("Dialog", u"Follow console output", None))
        self.JobNameLabel_2.setText(QCoreApplication.translate("Dialog", u"Job Name", None))
        self.parametersLabel_2.setText(QCoreApplication.translate("Dialog", u"Parameters", None))
        self.tokenBuildLabel_2.setText(QCoreApplication.translate("Dialog", u"Token Build", None))
        self.followComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"no", None))
        self.followComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"yes", None))

        self.jobNameLabel_3.setText(QCoreApplication.translate("Dialog", u"Job Name", None))
        self.xmlFileLabel.setText(QCoreApplication.translate("Dialog", u"xml file to upload", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"jenkins Pipeline Tool", None))
    # retranslateUi

