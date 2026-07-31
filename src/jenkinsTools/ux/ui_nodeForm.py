# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nodeForm.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.layoutWidget = QWidget(Widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 50, 741, 451))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.UrlLabel = QLabel(self.layoutWidget)
        self.UrlLabel.setObjectName(u"UrlLabel")

        self.gridLayout.addWidget(self.UrlLabel, 0, 0, 1, 1)

        self.UrlLineEdit = QLineEdit(self.layoutWidget)
        self.UrlLineEdit.setObjectName(u"UrlLineEdit")

        self.gridLayout.addWidget(self.UrlLineEdit, 0, 1, 1, 1)

        self.UsernameLabel = QLabel(self.layoutWidget)
        self.UsernameLabel.setObjectName(u"UsernameLabel")

        self.gridLayout.addWidget(self.UsernameLabel, 1, 0, 1, 1)

        self.UsernameLineEdit = QLineEdit(self.layoutWidget)
        self.UsernameLineEdit.setObjectName(u"UsernameLineEdit")

        self.gridLayout.addWidget(self.UsernameLineEdit, 1, 1, 1, 1)

        self.tokenLabel = QLabel(self.layoutWidget)
        self.tokenLabel.setObjectName(u"tokenLabel")

        self.gridLayout.addWidget(self.tokenLabel, 2, 0, 1, 1)

        self.tokenLineEdit = QLineEdit(self.layoutWidget)
        self.tokenLineEdit.setObjectName(u"tokenLineEdit")

        self.gridLayout.addWidget(self.tokenLineEdit, 2, 1, 1, 1)

        self.ActionLabel = QLabel(self.layoutWidget)
        self.ActionLabel.setObjectName(u"ActionLabel")

        self.gridLayout.addWidget(self.ActionLabel, 3, 0, 1, 1)

        self.ActionComboBox = QComboBox(self.layoutWidget)
        self.ActionComboBox.addItem("")
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

        self.gridLayout.addWidget(self.ActionComboBox, 3, 1, 1, 1)

        self.MethodLabel = QLabel(self.layoutWidget)
        self.MethodLabel.setObjectName(u"MethodLabel")

        self.gridLayout.addWidget(self.MethodLabel, 3, 2, 1, 1)

        self.MethodComboBox = QComboBox(self.layoutWidget)
        self.MethodComboBox.addItem("")
        self.MethodComboBox.addItem("")
        self.MethodComboBox.setObjectName(u"MethodComboBox")

        self.gridLayout.addWidget(self.MethodComboBox, 3, 3, 1, 1)

        self.stackedWidget = QStackedWidget(self.layoutWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.VmNamelabel = QLabel(self.page)
        self.VmNamelabel.setObjectName(u"VmNamelabel")
        self.VmNamelabel.setGeometry(QRect(10, 60, 121, 16))
        self.RemoteFsLlabel = QLabel(self.page)
        self.RemoteFsLlabel.setObjectName(u"RemoteFsLlabel")
        self.RemoteFsLlabel.setGeometry(QRect(380, 150, 121, 16))
        self.HostnameIpLabel = QLabel(self.page)
        self.HostnameIpLabel.setObjectName(u"HostnameIpLabel")
        self.HostnameIpLabel.setGeometry(QRect(10, 90, 121, 16))
        self.JenkinsCredsLabel = QLabel(self.page)
        self.JenkinsCredsLabel.setObjectName(u"JenkinsCredsLabel")
        self.JenkinsCredsLabel.setGeometry(QRect(380, 60, 141, 16))
        self.LabelsLabel = QLabel(self.page)
        self.LabelsLabel.setObjectName(u"LabelsLabel")
        self.LabelsLabel.setGeometry(QRect(10, 120, 121, 16))
        self.ExecutorsLabel = QLabel(self.page)
        self.ExecutorsLabel.setObjectName(u"ExecutorsLabel")
        self.ExecutorsLabel.setGeometry(QRect(10, 150, 121, 16))
        self.PortLabel = QLabel(self.page)
        self.PortLabel.setObjectName(u"PortLabel")
        self.PortLabel.setGeometry(QRect(380, 90, 141, 16))
        self.DescriptionLabel = QLabel(self.page)
        self.DescriptionLabel.setObjectName(u"DescriptionLabel")
        self.DescriptionLabel.setGeometry(QRect(380, 120, 141, 16))
        self.VmNameLineEdit = QLineEdit(self.page)
        self.VmNameLineEdit.setObjectName(u"VmNameLineEdit")
        self.VmNameLineEdit.setGeometry(QRect(152, 60, 131, 20))
        self.HostnameOrIpLineEdit = QLineEdit(self.page)
        self.HostnameOrIpLineEdit.setObjectName(u"HostnameOrIpLineEdit")
        self.HostnameOrIpLineEdit.setGeometry(QRect(152, 90, 131, 20))
        self.LabelsLineEdit = QLineEdit(self.page)
        self.LabelsLineEdit.setObjectName(u"LabelsLineEdit")
        self.LabelsLineEdit.setGeometry(QRect(152, 120, 131, 20))
        self.ExecutorsLineEdit = QLineEdit(self.page)
        self.ExecutorsLineEdit.setObjectName(u"ExecutorsLineEdit")
        self.ExecutorsLineEdit.setGeometry(QRect(152, 150, 131, 20))
        self.JenkinsCredsIdLineEdit = QLineEdit(self.page)
        self.JenkinsCredsIdLineEdit.setObjectName(u"JenkinsCredsIdLineEdit")
        self.JenkinsCredsIdLineEdit.setGeometry(QRect(550, 60, 171, 16))
        self.PortLlineEdit = QLineEdit(self.page)
        self.PortLlineEdit.setObjectName(u"PortLlineEdit")
        self.PortLlineEdit.setGeometry(QRect(550, 90, 171, 16))
        self.DescriptionLineEdit = QLineEdit(self.page)
        self.DescriptionLineEdit.setObjectName(u"DescriptionLineEdit")
        self.DescriptionLineEdit.setGeometry(QRect(550, 120, 171, 16))
        self.RemoteFsLineEdit = QLineEdit(self.page)
        self.RemoteFsLineEdit.setObjectName(u"RemoteFsLineEdit")
        self.RemoteFsLineEdit.setGeometry(QRect(550, 150, 171, 16))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.JenkinsCredsIdLineEdit_2 = QLineEdit(self.page_2)
        self.JenkinsCredsIdLineEdit_2.setObjectName(u"JenkinsCredsIdLineEdit_2")
        self.JenkinsCredsIdLineEdit_2.setGeometry(QRect(490, 60, 231, 20))
        self.RemoteFsLlabel_2 = QLabel(self.page_2)
        self.RemoteFsLlabel_2.setObjectName(u"RemoteFsLlabel_2")
        self.RemoteFsLlabel_2.setGeometry(QRect(350, 150, 121, 16))
        self.VmNameLineEdit_2 = QLineEdit(self.page_2)
        self.VmNameLineEdit_2.setObjectName(u"VmNameLineEdit_2")
        self.VmNameLineEdit_2.setGeometry(QRect(152, 60, 171, 20))
        self.JenkinsCredsLabel_2 = QLabel(self.page_2)
        self.JenkinsCredsLabel_2.setObjectName(u"JenkinsCredsLabel_2")
        self.JenkinsCredsLabel_2.setGeometry(QRect(350, 60, 121, 16))
        self.HostnameIpLabel_2 = QLabel(self.page_2)
        self.HostnameIpLabel_2.setObjectName(u"HostnameIpLabel_2")
        self.HostnameIpLabel_2.setGeometry(QRect(10, 90, 91, 16))
        self.LabelsLineEdit_2 = QLineEdit(self.page_2)
        self.LabelsLineEdit_2.setObjectName(u"LabelsLineEdit_2")
        self.LabelsLineEdit_2.setGeometry(QRect(152, 120, 171, 20))
        self.HostnameOrIpLineEdit_2 = QLineEdit(self.page_2)
        self.HostnameOrIpLineEdit_2.setObjectName(u"HostnameOrIpLineEdit_2")
        self.HostnameOrIpLineEdit_2.setGeometry(QRect(152, 90, 171, 20))
        self.DescriptionLabel_2 = QLabel(self.page_2)
        self.DescriptionLabel_2.setObjectName(u"DescriptionLabel_2")
        self.DescriptionLabel_2.setGeometry(QRect(350, 120, 121, 16))
        self.VmNamelabel_2 = QLabel(self.page_2)
        self.VmNamelabel_2.setObjectName(u"VmNamelabel_2")
        self.VmNamelabel_2.setGeometry(QRect(10, 60, 91, 16))
        self.LabelsLabel_2 = QLabel(self.page_2)
        self.LabelsLabel_2.setObjectName(u"LabelsLabel_2")
        self.LabelsLabel_2.setGeometry(QRect(10, 120, 91, 16))
        self.ExecutorsLabel_2 = QLabel(self.page_2)
        self.ExecutorsLabel_2.setObjectName(u"ExecutorsLabel_2")
        self.ExecutorsLabel_2.setGeometry(QRect(10, 150, 91, 16))
        self.ExecutorsLineEdit_2 = QLineEdit(self.page_2)
        self.ExecutorsLineEdit_2.setObjectName(u"ExecutorsLineEdit_2")
        self.ExecutorsLineEdit_2.setGeometry(QRect(152, 150, 171, 20))
        self.RemoteFsLineEdit_2 = QLineEdit(self.page_2)
        self.RemoteFsLineEdit_2.setObjectName(u"RemoteFsLineEdit_2")
        self.RemoteFsLineEdit_2.setGeometry(QRect(490, 150, 231, 20))
        self.DescriptionLineEdit_2 = QLineEdit(self.page_2)
        self.DescriptionLineEdit_2.setObjectName(u"DescriptionLineEdit_2")
        self.DescriptionLineEdit_2.setGeometry(QRect(490, 120, 231, 20))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.GetNodesTextEdit = QTextEdit(self.page_3)
        self.GetNodesTextEdit.setObjectName(u"GetNodesTextEdit")
        self.GetNodesTextEdit.setGeometry(QRect(20, 10, 671, 241))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.VmNamelabel_3 = QLabel(self.page_4)
        self.VmNamelabel_3.setObjectName(u"VmNamelabel_3")
        self.VmNamelabel_3.setGeometry(QRect(10, 60, 121, 16))
        self.VmNameLineEdit_3 = QLineEdit(self.page_4)
        self.VmNameLineEdit_3.setObjectName(u"VmNameLineEdit_3")
        self.VmNameLineEdit_3.setGeometry(QRect(152, 60, 131, 20))
        self.GetNodeTextEdit = QTextEdit(self.page_4)
        self.GetNodeTextEdit.setObjectName(u"GetNodeTextEdit")
        self.GetNodeTextEdit.setGeometry(QRect(10, 100, 701, 151))
        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout.addWidget(self.stackedWidget, 4, 0, 1, 5)

        self.QuitPushButton = QPushButton(self.layoutWidget)
        self.QuitPushButton.setObjectName(u"QuitPushButton")

        self.gridLayout.addWidget(self.QuitPushButton, 5, 3, 1, 1)

        self.RunPushButton = QPushButton(self.layoutWidget)
        self.RunPushButton.setObjectName(u"RunPushButton")

        self.gridLayout.addWidget(self.RunPushButton, 5, 4, 1, 1)


        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.UrlLabel.setText(QCoreApplication.translate("Widget", u"URL", None))
        self.UsernameLabel.setText(QCoreApplication.translate("Widget", u"username", None))
        self.tokenLabel.setText(QCoreApplication.translate("Widget", u"token/password", None))
        self.ActionLabel.setText(QCoreApplication.translate("Widget", u"Action", None))
        self.ActionComboBox.setItemText(0, QCoreApplication.translate("Widget", u"Add", None))
        self.ActionComboBox.setItemText(1, QCoreApplication.translate("Widget", u"Update", None))
        self.ActionComboBox.setItemText(2, QCoreApplication.translate("Widget", u"Enable", None))
        self.ActionComboBox.setItemText(3, QCoreApplication.translate("Widget", u"Disable", None))
        self.ActionComboBox.setItemText(4, QCoreApplication.translate("Widget", u"Delete", None))
        self.ActionComboBox.setItemText(5, QCoreApplication.translate("Widget", u"Node Exists", None))
        self.ActionComboBox.setItemText(6, QCoreApplication.translate("Widget", u"Get Nodes", None))
        self.ActionComboBox.setItemText(7, QCoreApplication.translate("Widget", u"Get Node Info", None))
        self.ActionComboBox.setItemText(8, QCoreApplication.translate("Widget", u"Get Node Config", None))
        self.ActionComboBox.setItemText(9, QCoreApplication.translate("Widget", u"New Item", None))

        self.MethodLabel.setText(QCoreApplication.translate("Widget", u"Method", None))
        self.MethodComboBox.setItemText(0, QCoreApplication.translate("Widget", u"SSH", None))
        self.MethodComboBox.setItemText(1, QCoreApplication.translate("Widget", u"JNLP", None))

        self.VmNamelabel.setText(QCoreApplication.translate("Widget", u"VM Name", None))
        self.RemoteFsLlabel.setText(QCoreApplication.translate("Widget", u"Remote Filesystem", None))
        self.HostnameIpLabel.setText(QCoreApplication.translate("Widget", u"Hostname/IP", None))
        self.JenkinsCredsLabel.setText(QCoreApplication.translate("Widget", u"Jenkins Credentials ID", None))
        self.LabelsLabel.setText(QCoreApplication.translate("Widget", u"Labels", None))
        self.ExecutorsLabel.setText(QCoreApplication.translate("Widget", u"Executors", None))
        self.PortLabel.setText(QCoreApplication.translate("Widget", u"Port", None))
        self.DescriptionLabel.setText(QCoreApplication.translate("Widget", u"Description", None))
        self.PortLlineEdit.setText(QCoreApplication.translate("Widget", u"22", None))
        self.RemoteFsLlabel_2.setText(QCoreApplication.translate("Widget", u"Remote Filesystem", None))
        self.JenkinsCredsLabel_2.setText(QCoreApplication.translate("Widget", u"JVM Options", None))
        self.HostnameIpLabel_2.setText(QCoreApplication.translate("Widget", u"Hostname/IP", None))
        self.DescriptionLabel_2.setText(QCoreApplication.translate("Widget", u"Description", None))
        self.VmNamelabel_2.setText(QCoreApplication.translate("Widget", u"VM Name", None))
        self.LabelsLabel_2.setText(QCoreApplication.translate("Widget", u"Labels", None))
        self.ExecutorsLabel_2.setText(QCoreApplication.translate("Widget", u"Executors", None))
        self.VmNamelabel_3.setText(QCoreApplication.translate("Widget", u"VM Name", None))
        self.QuitPushButton.setText(QCoreApplication.translate("Widget", u"quit", None))
        self.RunPushButton.setText(QCoreApplication.translate("Widget", u"run command", None))
    # retranslateUi

