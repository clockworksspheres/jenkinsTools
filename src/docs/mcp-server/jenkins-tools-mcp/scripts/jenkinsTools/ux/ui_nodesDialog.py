# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nodesDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
        Dialog.resize(785, 522)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.UsernameLabel = QLabel(Dialog)
        self.UsernameLabel.setObjectName(u"UsernameLabel")

        self.gridLayout.addWidget(self.UsernameLabel, 2, 0, 1, 1)

        self.ActionComboBox = QComboBox(Dialog)
        self.ActionComboBox.addItem("")
        self.ActionComboBox.addItem("")
        self.ActionComboBox.addItem("")
        self.ActionComboBox.addItem("")
        self.ActionComboBox.addItem("")
        self.ActionComboBox.addItem("")
        self.ActionComboBox.addItem("")
        self.ActionComboBox.addItem("")
        self.ActionComboBox.addItem("")
        self.ActionComboBox.setObjectName(u"ActionComboBox")

        self.gridLayout.addWidget(self.ActionComboBox, 4, 1, 1, 1)

        self.tokenLineEdit = QLineEdit(Dialog)
        self.tokenLineEdit.setObjectName(u"tokenLineEdit")
        self.tokenLineEdit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.gridLayout.addWidget(self.tokenLineEdit, 3, 1, 1, 1)

        self.closePushButton = QPushButton(Dialog)
        self.closePushButton.setObjectName(u"closePushButton")

        self.gridLayout.addWidget(self.closePushButton, 6, 3, 1, 1)

        self.UrlLabel = QLabel(Dialog)
        self.UrlLabel.setObjectName(u"UrlLabel")

        self.gridLayout.addWidget(self.UrlLabel, 1, 0, 1, 1)

        self.RunPushButton = QPushButton(Dialog)
        self.RunPushButton.setObjectName(u"RunPushButton")

        self.gridLayout.addWidget(self.RunPushButton, 6, 4, 1, 1)

        self.tokenLabel = QLabel(Dialog)
        self.tokenLabel.setObjectName(u"tokenLabel")

        self.gridLayout.addWidget(self.tokenLabel, 3, 0, 1, 1)

        self.MethodLabel = QLabel(Dialog)
        self.MethodLabel.setObjectName(u"MethodLabel")

        self.gridLayout.addWidget(self.MethodLabel, 4, 2, 1, 1)

        self.ActionLabel = QLabel(Dialog)
        self.ActionLabel.setObjectName(u"ActionLabel")

        self.gridLayout.addWidget(self.ActionLabel, 4, 0, 1, 1)

        self.MethodComboBox = QComboBox(Dialog)
        self.MethodComboBox.addItem("")
        self.MethodComboBox.addItem("")
        self.MethodComboBox.setObjectName(u"MethodComboBox")

        self.gridLayout.addWidget(self.MethodComboBox, 4, 3, 1, 1)

        self.UrlLineEdit = QLineEdit(Dialog)
        self.UrlLineEdit.setObjectName(u"UrlLineEdit")

        self.gridLayout.addWidget(self.UrlLineEdit, 1, 1, 1, 1)

        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.JenkinsCredsLabel = QLabel(self.page)
        self.JenkinsCredsLabel.setObjectName(u"JenkinsCredsLabel")

        self.gridLayout_2.addWidget(self.JenkinsCredsLabel, 0, 2, 1, 1)

        self.ExecutorsLabel = QLabel(self.page)
        self.ExecutorsLabel.setObjectName(u"ExecutorsLabel")

        self.gridLayout_2.addWidget(self.ExecutorsLabel, 3, 0, 1, 1)

        self.RemoteFsLineEdit = QLineEdit(self.page)
        self.RemoteFsLineEdit.setObjectName(u"RemoteFsLineEdit")

        self.gridLayout_2.addWidget(self.RemoteFsLineEdit, 3, 3, 1, 1)

        self.RemoteFsLlabel = QLabel(self.page)
        self.RemoteFsLlabel.setObjectName(u"RemoteFsLlabel")

        self.gridLayout_2.addWidget(self.RemoteFsLlabel, 3, 2, 1, 1)

        self.HostnameOrIpLineEdit = QLineEdit(self.page)
        self.HostnameOrIpLineEdit.setObjectName(u"HostnameOrIpLineEdit")

        self.gridLayout_2.addWidget(self.HostnameOrIpLineEdit, 1, 1, 1, 1)

        self.PortLlineEdit = QLineEdit(self.page)
        self.PortLlineEdit.setObjectName(u"PortLlineEdit")

        self.gridLayout_2.addWidget(self.PortLlineEdit, 1, 3, 1, 1)

        self.LabelsLineEdit = QLineEdit(self.page)
        self.LabelsLineEdit.setObjectName(u"LabelsLineEdit")

        self.gridLayout_2.addWidget(self.LabelsLineEdit, 2, 1, 1, 1)

        self.VmNameLineEdit = QLineEdit(self.page)
        self.VmNameLineEdit.setObjectName(u"VmNameLineEdit")

        self.gridLayout_2.addWidget(self.VmNameLineEdit, 0, 1, 1, 1)

        self.HostnameIpLabel = QLabel(self.page)
        self.HostnameIpLabel.setObjectName(u"HostnameIpLabel")

        self.gridLayout_2.addWidget(self.HostnameIpLabel, 1, 0, 1, 1)

        self.JenkinsCredsIdLineEdit = QLineEdit(self.page)
        self.JenkinsCredsIdLineEdit.setObjectName(u"JenkinsCredsIdLineEdit")

        self.gridLayout_2.addWidget(self.JenkinsCredsIdLineEdit, 0, 3, 1, 1)

        self.VmNamelabel = QLabel(self.page)
        self.VmNamelabel.setObjectName(u"VmNamelabel")

        self.gridLayout_2.addWidget(self.VmNamelabel, 0, 0, 1, 1)

        self.LabelsLabel = QLabel(self.page)
        self.LabelsLabel.setObjectName(u"LabelsLabel")

        self.gridLayout_2.addWidget(self.LabelsLabel, 2, 0, 1, 1)

        self.PortLabel = QLabel(self.page)
        self.PortLabel.setObjectName(u"PortLabel")

        self.gridLayout_2.addWidget(self.PortLabel, 1, 2, 1, 1)

        self.DescriptionLineEdit = QLineEdit(self.page)
        self.DescriptionLineEdit.setObjectName(u"DescriptionLineEdit")

        self.gridLayout_2.addWidget(self.DescriptionLineEdit, 2, 3, 1, 1)

        self.DescriptionLabel = QLabel(self.page)
        self.DescriptionLabel.setObjectName(u"DescriptionLabel")

        self.gridLayout_2.addWidget(self.DescriptionLabel, 2, 2, 1, 1)

        self.ExecutorsLineEdit = QLineEdit(self.page)
        self.ExecutorsLineEdit.setObjectName(u"ExecutorsLineEdit")

        self.gridLayout_2.addWidget(self.ExecutorsLineEdit, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 4, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 4, 3, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.LabelsLineEdit_2 = QLineEdit(self.page_2)
        self.LabelsLineEdit_2.setObjectName(u"LabelsLineEdit_2")

        self.gridLayout_3.addWidget(self.LabelsLineEdit_2, 2, 1, 1, 1)

        self.VmNamelabel_2 = QLabel(self.page_2)
        self.VmNamelabel_2.setObjectName(u"VmNamelabel_2")

        self.gridLayout_3.addWidget(self.VmNamelabel_2, 0, 0, 1, 1)

        self.JVMOptionsLineEdit = QLineEdit(self.page_2)
        self.JVMOptionsLineEdit.setObjectName(u"JVMOptionsLineEdit")

        self.gridLayout_3.addWidget(self.JVMOptionsLineEdit, 0, 3, 1, 1)

        self.HostnameIpLabel_2 = QLabel(self.page_2)
        self.HostnameIpLabel_2.setObjectName(u"HostnameIpLabel_2")

        self.gridLayout_3.addWidget(self.HostnameIpLabel_2, 1, 0, 1, 1)

        self.HostnameOrIpLineEdit_2 = QLineEdit(self.page_2)
        self.HostnameOrIpLineEdit_2.setObjectName(u"HostnameOrIpLineEdit_2")

        self.gridLayout_3.addWidget(self.HostnameOrIpLineEdit_2, 1, 1, 1, 1)

        self.DescriptionLineEdit_2 = QLineEdit(self.page_2)
        self.DescriptionLineEdit_2.setObjectName(u"DescriptionLineEdit_2")

        self.gridLayout_3.addWidget(self.DescriptionLineEdit_2, 2, 3, 1, 1)

        self.ExecutorsLineEdit_2 = QLineEdit(self.page_2)
        self.ExecutorsLineEdit_2.setObjectName(u"ExecutorsLineEdit_2")

        self.gridLayout_3.addWidget(self.ExecutorsLineEdit_2, 3, 1, 1, 1)

        self.LabelsLabel_2 = QLabel(self.page_2)
        self.LabelsLabel_2.setObjectName(u"LabelsLabel_2")

        self.gridLayout_3.addWidget(self.LabelsLabel_2, 2, 0, 1, 1)

        self.JenkinsCredsLabel_2 = QLabel(self.page_2)
        self.JenkinsCredsLabel_2.setObjectName(u"JenkinsCredsLabel_2")

        self.gridLayout_3.addWidget(self.JenkinsCredsLabel_2, 0, 2, 1, 1)

        self.VmNameLineEdit_2 = QLineEdit(self.page_2)
        self.VmNameLineEdit_2.setObjectName(u"VmNameLineEdit_2")

        self.gridLayout_3.addWidget(self.VmNameLineEdit_2, 0, 1, 1, 1)

        self.RemoteFsLineEdit_2 = QLineEdit(self.page_2)
        self.RemoteFsLineEdit_2.setObjectName(u"RemoteFsLineEdit_2")

        self.gridLayout_3.addWidget(self.RemoteFsLineEdit_2, 3, 3, 1, 1)

        self.ExecutorsLabel_2 = QLabel(self.page_2)
        self.ExecutorsLabel_2.setObjectName(u"ExecutorsLabel_2")

        self.gridLayout_3.addWidget(self.ExecutorsLabel_2, 3, 0, 1, 1)

        self.DescriptionLabel_2 = QLabel(self.page_2)
        self.DescriptionLabel_2.setObjectName(u"DescriptionLabel_2")

        self.gridLayout_3.addWidget(self.DescriptionLabel_2, 2, 2, 1, 1)

        self.RemoteFsLlabel_2 = QLabel(self.page_2)
        self.RemoteFsLlabel_2.setObjectName(u"RemoteFsLlabel_2")

        self.gridLayout_3.addWidget(self.RemoteFsLlabel_2, 3, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 4, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 4, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 4, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_8, 4, 3, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_4 = QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.GetNodesTextBrowser = QTextBrowser(self.page_3)
        self.GetNodesTextBrowser.setObjectName(u"GetNodesTextBrowser")

        self.gridLayout_4.addWidget(self.GetNodesTextBrowser, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_5 = QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.VmNameLineEdit_3 = QLineEdit(self.page_4)
        self.VmNameLineEdit_3.setObjectName(u"VmNameLineEdit_3")

        self.gridLayout_5.addWidget(self.VmNameLineEdit_3, 0, 1, 1, 1)

        self.VmNamelabel_3 = QLabel(self.page_4)
        self.VmNamelabel_3.setObjectName(u"VmNamelabel_3")

        self.gridLayout_5.addWidget(self.VmNamelabel_3, 0, 0, 1, 1)

        self.getNodeTextBrowser = QTextBrowser(self.page_4)
        self.getNodeTextBrowser.setObjectName(u"getNodeTextBrowser")

        self.gridLayout_5.addWidget(self.getNodeTextBrowser, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout.addWidget(self.stackedWidget, 5, 0, 1, 5)

        self.UsernameLineEdit = QLineEdit(Dialog)
        self.UsernameLineEdit.setObjectName(u"UsernameLineEdit")

        self.gridLayout.addWidget(self.UsernameLineEdit, 2, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)


        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.UsernameLabel.setText(QCoreApplication.translate("Dialog", u"username", None))
        self.ActionComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Add", None))
        self.ActionComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Update", None))
        self.ActionComboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Enable", None))
        self.ActionComboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Disable", None))
        self.ActionComboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Delete", None))
        self.ActionComboBox.setItemText(5, QCoreApplication.translate("Dialog", u"Node Exists", None))
        self.ActionComboBox.setItemText(6, QCoreApplication.translate("Dialog", u"Get Nodes", None))
        self.ActionComboBox.setItemText(7, QCoreApplication.translate("Dialog", u"Get Node Info", None))
        self.ActionComboBox.setItemText(8, QCoreApplication.translate("Dialog", u"Get Node Config", None))

        self.closePushButton.setText(QCoreApplication.translate("Dialog", u"close", None))
        self.UrlLabel.setText(QCoreApplication.translate("Dialog", u"URL", None))
        self.RunPushButton.setText(QCoreApplication.translate("Dialog", u"run command", None))
        self.tokenLabel.setText(QCoreApplication.translate("Dialog", u"token/password", None))
        self.MethodLabel.setText(QCoreApplication.translate("Dialog", u"Method", None))
        self.ActionLabel.setText(QCoreApplication.translate("Dialog", u"Action", None))
        self.MethodComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"ssh", None))
        self.MethodComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"jnlp", None))

        self.JenkinsCredsLabel.setText(QCoreApplication.translate("Dialog", u"Jenkins Credentials ID", None))
        self.ExecutorsLabel.setText(QCoreApplication.translate("Dialog", u"Executors", None))
        self.RemoteFsLlabel.setText(QCoreApplication.translate("Dialog", u"Remote Filesystem", None))
        self.PortLlineEdit.setText(QCoreApplication.translate("Dialog", u"22", None))
        self.HostnameIpLabel.setText(QCoreApplication.translate("Dialog", u"Hostname/IP", None))
        self.VmNamelabel.setText(QCoreApplication.translate("Dialog", u"VM Name", None))
        self.LabelsLabel.setText(QCoreApplication.translate("Dialog", u"Labels", None))
        self.PortLabel.setText(QCoreApplication.translate("Dialog", u"Port", None))
        self.DescriptionLabel.setText(QCoreApplication.translate("Dialog", u"Description", None))
        self.VmNamelabel_2.setText(QCoreApplication.translate("Dialog", u"VM Name", None))
        self.HostnameIpLabel_2.setText(QCoreApplication.translate("Dialog", u"Hostname/IP", None))
        self.LabelsLabel_2.setText(QCoreApplication.translate("Dialog", u"Labels", None))
        self.JenkinsCredsLabel_2.setText(QCoreApplication.translate("Dialog", u"JVM Options", None))
        self.ExecutorsLabel_2.setText(QCoreApplication.translate("Dialog", u"Executors", None))
        self.DescriptionLabel_2.setText(QCoreApplication.translate("Dialog", u"Description", None))
        self.RemoteFsLlabel_2.setText(QCoreApplication.translate("Dialog", u"Remote Filesystem", None))
        self.VmNamelabel_3.setText(QCoreApplication.translate("Dialog", u"VM Name", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Jenkins Node Tool", None))
    # retranslateUi

