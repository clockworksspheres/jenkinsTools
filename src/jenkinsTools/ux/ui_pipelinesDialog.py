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
    QSpacerItem, QStackedWidget, QTextBrowser, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(834, 559)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.UrlLabel = QLabel(Dialog)
        self.UrlLabel.setObjectName(u"UrlLabel")

        self.gridLayout.addWidget(self.UrlLabel, 1, 0, 1, 1)

        self.UrlLineEdit = QLineEdit(Dialog)
        self.UrlLineEdit.setObjectName(u"UrlLineEdit")

        self.gridLayout.addWidget(self.UrlLineEdit, 1, 1, 1, 1)

        self.UsernameLabel = QLabel(Dialog)
        self.UsernameLabel.setObjectName(u"UsernameLabel")

        self.gridLayout.addWidget(self.UsernameLabel, 2, 0, 1, 1)

        self.UsernameLineEdit = QLineEdit(Dialog)
        self.UsernameLineEdit.setObjectName(u"UsernameLineEdit")

        self.gridLayout.addWidget(self.UsernameLineEdit, 2, 1, 1, 1)

        self.tokenLabel = QLabel(Dialog)
        self.tokenLabel.setObjectName(u"tokenLabel")

        self.gridLayout.addWidget(self.tokenLabel, 3, 0, 1, 1)

        self.tokenLineEdit = QLineEdit(Dialog)
        self.tokenLineEdit.setObjectName(u"tokenLineEdit")

        self.gridLayout.addWidget(self.tokenLineEdit, 3, 1, 1, 1)

        self.ActionLabel = QLabel(Dialog)
        self.ActionLabel.setObjectName(u"ActionLabel")

        self.gridLayout.addWidget(self.ActionLabel, 4, 0, 1, 1)

        self.ActionComboBox = QComboBox(Dialog)
        self.ActionComboBox.addItem("")
        self.ActionComboBox.addItem("")
        self.ActionComboBox.addItem("")
        self.ActionComboBox.addItem("")
        self.ActionComboBox.addItem("")
        self.ActionComboBox.setObjectName(u"ActionComboBox")

        self.gridLayout.addWidget(self.ActionComboBox, 4, 1, 1, 1)

        self.MethodLabel = QLabel(Dialog)
        self.MethodLabel.setObjectName(u"MethodLabel")

        self.gridLayout.addWidget(self.MethodLabel, 4, 2, 1, 1)

        self.MethodComboBox = QComboBox(Dialog)
        self.MethodComboBox.addItem("")
        self.MethodComboBox.addItem("")
        self.MethodComboBox.setObjectName(u"MethodComboBox")

        self.gridLayout.addWidget(self.MethodComboBox, 4, 3, 1, 1)

        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scriptLabel = QLabel(self.page)
        self.scriptLabel.setObjectName(u"scriptLabel")

        self.gridLayout_2.addWidget(self.scriptLabel, 2, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.jenkinsfileLabel = QLabel(self.page)
        self.jenkinsfileLabel.setObjectName(u"jenkinsfileLabel")

        self.gridLayout_2.addWidget(self.jenkinsfileLabel, 3, 0, 1, 1)

        self.jenkinsfileLineEdit = QLineEdit(self.page)
        self.jenkinsfileLineEdit.setObjectName(u"jenkinsfileLineEdit")

        self.gridLayout_2.addWidget(self.jenkinsfileLineEdit, 3, 1, 1, 1)

        self.descriptionLineEdit = QLineEdit(self.page)
        self.descriptionLineEdit.setObjectName(u"descriptionLineEdit")

        self.gridLayout_2.addWidget(self.descriptionLineEdit, 1, 3, 1, 1)

        self.credsIdLineEdit = QLineEdit(self.page)
        self.credsIdLineEdit.setObjectName(u"credsIdLineEdit")

        self.gridLayout_2.addWidget(self.credsIdLineEdit, 0, 3, 1, 1)

        self.repoLineEdit = QLineEdit(self.page)
        self.repoLineEdit.setObjectName(u"repoLineEdit")

        self.gridLayout_2.addWidget(self.repoLineEdit, 1, 1, 1, 1)

        self.jobNameLineEdit = QLineEdit(self.page)
        self.jobNameLineEdit.setObjectName(u"jobNameLineEdit")

        self.gridLayout_2.addWidget(self.jobNameLineEdit, 0, 1, 1, 1)

        self.repoLabel = QLabel(self.page)
        self.repoLabel.setObjectName(u"repoLabel")

        self.gridLayout_2.addWidget(self.repoLabel, 1, 0, 1, 1)

        self.descriptionLabel = QLabel(self.page)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.gridLayout_2.addWidget(self.descriptionLabel, 1, 2, 1, 1)

        self.scriptPathLineEdit = QLineEdit(self.page)
        self.scriptPathLineEdit.setObjectName(u"scriptPathLineEdit")

        self.gridLayout_2.addWidget(self.scriptPathLineEdit, 3, 3, 1, 1)

        self.credsIdLabel = QLabel(self.page)
        self.credsIdLabel.setObjectName(u"credsIdLabel")

        self.gridLayout_2.addWidget(self.credsIdLabel, 0, 2, 1, 1)

        self.scriptLineEdit = QLineEdit(self.page)
        self.scriptLineEdit.setObjectName(u"scriptLineEdit")

        self.gridLayout_2.addWidget(self.scriptLineEdit, 2, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.branchLineEdit = QLineEdit(self.page)
        self.branchLineEdit.setObjectName(u"branchLineEdit")

        self.gridLayout_2.addWidget(self.branchLineEdit, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 4, 3, 1, 1)

        self.branchLabel = QLabel(self.page)
        self.branchLabel.setObjectName(u"branchLabel")

        self.gridLayout_2.addWidget(self.branchLabel, 2, 0, 1, 1)

        self.jobNamelabel = QLabel(self.page)
        self.jobNamelabel.setObjectName(u"jobNamelabel")

        self.gridLayout_2.addWidget(self.jobNamelabel, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 4, 2, 1, 1)

        self.scriptPathPushButton = QPushButton(self.page)
        self.scriptPathPushButton.setObjectName(u"scriptPathPushButton")

        self.gridLayout_2.addWidget(self.scriptPathPushButton, 3, 2, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.gridLayout_3 = QGridLayout(self.page1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.followLabel = QLabel(self.page1)
        self.followLabel.setObjectName(u"followLabel")

        self.gridLayout_3.addWidget(self.followLabel, 1, 0, 1, 1)

        self.JobNameLabel_2 = QLabel(self.page1)
        self.JobNameLabel_2.setObjectName(u"JobNameLabel_2")

        self.gridLayout_3.addWidget(self.JobNameLabel_2, 0, 0, 1, 1)

        self.followComboBox = QComboBox(self.page1)
        self.followComboBox.addItem("")
        self.followComboBox.addItem("")
        self.followComboBox.setObjectName(u"followComboBox")

        self.gridLayout_3.addWidget(self.followComboBox, 1, 1, 1, 1)

        self.tokenBuildLabel_2 = QLabel(self.page1)
        self.tokenBuildLabel_2.setObjectName(u"tokenBuildLabel_2")

        self.gridLayout_3.addWidget(self.tokenBuildLabel_2, 3, 0, 1, 1)

        self.parametersLabel_2 = QLabel(self.page1)
        self.parametersLabel_2.setObjectName(u"parametersLabel_2")

        self.gridLayout_3.addWidget(self.parametersLabel_2, 2, 0, 1, 1)

        self.tokenBuildLineEdit_2 = QLineEdit(self.page1)
        self.tokenBuildLineEdit_2.setObjectName(u"tokenBuildLineEdit_2")

        self.gridLayout_3.addWidget(self.tokenBuildLineEdit_2, 3, 1, 1, 1)

        self.parametersLineEdit_2 = QLineEdit(self.page1)
        self.parametersLineEdit_2.setObjectName(u"parametersLineEdit_2")

        self.gridLayout_3.addWidget(self.parametersLineEdit_2, 2, 1, 1, 1)

        self.JobNameLineEdit_2 = QLineEdit(self.page1)
        self.JobNameLineEdit_2.setObjectName(u"JobNameLineEdit_2")

        self.gridLayout_3.addWidget(self.JobNameLineEdit_2, 0, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 4, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 4, 1, 1, 1)

        self.stackedWidget.addWidget(self.page1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.getPipelineTextBrowser = QTextBrowser(self.page_2)
        self.getPipelineTextBrowser.setObjectName(u"getPipelineTextBrowser")

        self.gridLayout_4.addWidget(self.getPipelineTextBrowser, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_5 = QGridLayout(self.page_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.jobNameLabel_3 = QLabel(self.page_3)
        self.jobNameLabel_3.setObjectName(u"jobNameLabel_3")

        self.gridLayout_5.addWidget(self.jobNameLabel_3, 0, 0, 1, 1)

        self.xmlFilePushButton = QPushButton(self.page_3)
        self.xmlFilePushButton.setObjectName(u"xmlFilePushButton")

        self.gridLayout_5.addWidget(self.xmlFilePushButton, 0, 2, 1, 1)

        self.xmlFileLineEdit = QLineEdit(self.page_3)
        self.xmlFileLineEdit.setObjectName(u"xmlFileLineEdit")

        self.gridLayout_5.addWidget(self.xmlFileLineEdit, 0, 3, 1, 1)

        self.jobNameLineEdit_3 = QLineEdit(self.page_3)
        self.jobNameLineEdit_3.setObjectName(u"jobNameLineEdit_3")

        self.gridLayout_5.addWidget(self.jobNameLineEdit_3, 0, 1, 1, 1)

        self.jobTextBrowser = QTextBrowser(self.page_3)
        self.jobTextBrowser.setObjectName(u"jobTextBrowser")

        self.gridLayout_5.addWidget(self.jobTextBrowser, 1, 0, 1, 4)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout.addWidget(self.stackedWidget, 5, 0, 1, 5)

        self.closePushButton = QPushButton(Dialog)
        self.closePushButton.setObjectName(u"closePushButton")

        self.gridLayout.addWidget(self.closePushButton, 6, 3, 1, 1)

        self.RunPushButton = QPushButton(Dialog)
        self.RunPushButton.setObjectName(u"RunPushButton")

        self.gridLayout.addWidget(self.RunPushButton, 6, 4, 1, 1)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"jenkins Pipeline Tool", None))
        self.UrlLabel.setText(QCoreApplication.translate("Dialog", u"URL", None))
        self.UsernameLabel.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.tokenLabel.setText(QCoreApplication.translate("Dialog", u"Token/Password", None))
        self.ActionLabel.setText(QCoreApplication.translate("Dialog", u"Action", None))
        self.ActionComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"create", None))
        self.ActionComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"run", None))
        self.ActionComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"check", None))
        self.ActionComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"get-config", None))
        self.ActionComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"set-config", None))

        self.MethodLabel.setText(QCoreApplication.translate("Dialog", u"Type", None))
        self.MethodComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"scm", None))
        self.MethodComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"inline", None))

        self.scriptLabel.setText(QCoreApplication.translate("Dialog", u"Script", None))
        self.jenkinsfileLabel.setText(QCoreApplication.translate("Dialog", u"Jenkinsfile", None))
        self.descriptionLineEdit.setText("")
        self.repoLabel.setText(QCoreApplication.translate("Dialog", u"Repo", None))
        self.descriptionLabel.setText(QCoreApplication.translate("Dialog", u"Description", None))
        self.credsIdLabel.setText(QCoreApplication.translate("Dialog", u"Credentials ID", None))
        self.branchLabel.setText(QCoreApplication.translate("Dialog", u"Branch", None))
        self.jobNamelabel.setText(QCoreApplication.translate("Dialog", u"Job Name", None))
        self.scriptPathPushButton.setText(QCoreApplication.translate("Dialog", u"Script Path", None))
        self.followLabel.setText(QCoreApplication.translate("Dialog", u"Follow console output", None))
        self.JobNameLabel_2.setText(QCoreApplication.translate("Dialog", u"Job Name", None))
        self.followComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"no", None))
        self.followComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"yes", None))

        self.tokenBuildLabel_2.setText(QCoreApplication.translate("Dialog", u"Token Build", None))
        self.parametersLabel_2.setText(QCoreApplication.translate("Dialog", u"Parameters", None))
        self.jobNameLabel_3.setText(QCoreApplication.translate("Dialog", u"Job Name", None))
        self.xmlFilePushButton.setText(QCoreApplication.translate("Dialog", u"xml file to upload", None))
        self.closePushButton.setText(QCoreApplication.translate("Dialog", u"close", None))
        self.RunPushButton.setText(QCoreApplication.translate("Dialog", u"run command", None))
    # retranslateUi

