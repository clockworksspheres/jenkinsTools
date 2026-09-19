# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sshCreds.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(460, 368)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.credsIdLabel = QLabel(Dialog)
        self.credsIdLabel.setObjectName(u"credsIdLabel")

        self.gridLayout.addWidget(self.credsIdLabel, 5, 0, 1, 1)

        self.sshUserLineEdit = QLineEdit(Dialog)
        self.sshUserLineEdit.setObjectName(u"sshUserLineEdit")

        self.gridLayout.addWidget(self.sshUserLineEdit, 6, 1, 1, 1)

        self.descriptionLabel = QLabel(Dialog)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.gridLayout.addWidget(self.descriptionLabel, 7, 0, 1, 1)

        self.UsernameLabel = QLabel(Dialog)
        self.UsernameLabel.setObjectName(u"UsernameLabel")

        self.gridLayout.addWidget(self.UsernameLabel, 2, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.tokenLineEdit = QLineEdit(Dialog)
        self.tokenLineEdit.setObjectName(u"tokenLineEdit")
        self.tokenLineEdit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.gridLayout.addWidget(self.tokenLineEdit, 3, 1, 1, 1)

        self.keyPassphraseLabel = QLabel(Dialog)
        self.keyPassphraseLabel.setObjectName(u"keyPassphraseLabel")

        self.gridLayout.addWidget(self.keyPassphraseLabel, 9, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 10, 1, 1, 1)

        self.tokenLabel = QLabel(Dialog)
        self.tokenLabel.setObjectName(u"tokenLabel")

        self.gridLayout.addWidget(self.tokenLabel, 3, 0, 1, 1)

        self.UrlLabel = QLabel(Dialog)
        self.UrlLabel.setObjectName(u"UrlLabel")

        self.gridLayout.addWidget(self.UrlLabel, 1, 0, 1, 1)

        self.privateKeyLineEdit = QLineEdit(Dialog)
        self.privateKeyLineEdit.setObjectName(u"privateKeyLineEdit")
        self.privateKeyLineEdit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.gridLayout.addWidget(self.privateKeyLineEdit, 8, 1, 1, 1)

        self.descriptionLineEdit = QLineEdit(Dialog)
        self.descriptionLineEdit.setObjectName(u"descriptionLineEdit")

        self.gridLayout.addWidget(self.descriptionLineEdit, 7, 1, 1, 1)

        self.credsIdLineEdit = QLineEdit(Dialog)
        self.credsIdLineEdit.setObjectName(u"credsIdLineEdit")

        self.gridLayout.addWidget(self.credsIdLineEdit, 5, 1, 1, 1)

        self.privateKeyPushButton = QPushButton(Dialog)
        self.privateKeyPushButton.setObjectName(u"privateKeyPushButton")

        self.gridLayout.addWidget(self.privateKeyPushButton, 8, 0, 1, 1)

        self.UsernameLineEdit = QLineEdit(Dialog)
        self.UsernameLineEdit.setObjectName(u"UsernameLineEdit")

        self.gridLayout.addWidget(self.UsernameLineEdit, 2, 1, 1, 1)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)

        self.keyPassphraseLineEdit = QLineEdit(Dialog)
        self.keyPassphraseLineEdit.setObjectName(u"keyPassphraseLineEdit")

        self.gridLayout.addWidget(self.keyPassphraseLineEdit, 9, 1, 1, 1)

        self.sshUserLabel = QLabel(Dialog)
        self.sshUserLabel.setObjectName(u"sshUserLabel")

        self.gridLayout.addWidget(self.sshUserLabel, 6, 0, 1, 1)

        self.UrlLineEdit = QLineEdit(Dialog)
        self.UrlLineEdit.setObjectName(u"UrlLineEdit")

        self.gridLayout.addWidget(self.UrlLineEdit, 1, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.credsIdLabel.setText(QCoreApplication.translate("Dialog", u"credentials ID", None))
        self.descriptionLabel.setText(QCoreApplication.translate("Dialog", u"description", None))
        self.UsernameLabel.setText(QCoreApplication.translate("Dialog", u"Jenkins username", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Method", None))
        self.keyPassphraseLabel.setText(QCoreApplication.translate("Dialog", u"key passphrase", None))
        self.tokenLabel.setText(QCoreApplication.translate("Dialog", u"token/password", None))
        self.UrlLabel.setText(QCoreApplication.translate("Dialog", u"URL", None))
        self.privateKeyPushButton.setText(QCoreApplication.translate("Dialog", u"Private Key File", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Add SSH key as credential", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Add and encrypted SSH key as credential", None))

        self.sshUserLabel.setText(QCoreApplication.translate("Dialog", u"ssh user", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Jenkins Ssh Key Wrangling", None))
    # retranslateUi

