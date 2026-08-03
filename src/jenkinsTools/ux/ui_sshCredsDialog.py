# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sshCreds.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(471, 402)
        self.titleLabel = QLabel(Dialog)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(150, 30, 121, 16))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 70, 426, 311))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.UrlLabel = QLabel(self.widget)
        self.UrlLabel.setObjectName(u"UrlLabel")

        self.gridLayout.addWidget(self.UrlLabel, 0, 0, 1, 1)

        self.UrlLineEdit = QLineEdit(self.widget)
        self.UrlLineEdit.setObjectName(u"UrlLineEdit")

        self.gridLayout.addWidget(self.UrlLineEdit, 0, 1, 1, 1)

        self.UsernameLabel = QLabel(self.widget)
        self.UsernameLabel.setObjectName(u"UsernameLabel")

        self.gridLayout.addWidget(self.UsernameLabel, 1, 0, 1, 1)

        self.UsernameLineEdit = QLineEdit(self.widget)
        self.UsernameLineEdit.setObjectName(u"UsernameLineEdit")

        self.gridLayout.addWidget(self.UsernameLineEdit, 1, 1, 1, 1)

        self.tokenLabel = QLabel(self.widget)
        self.tokenLabel.setObjectName(u"tokenLabel")

        self.gridLayout.addWidget(self.tokenLabel, 2, 0, 1, 1)

        self.tokenLineEdit = QLineEdit(self.widget)
        self.tokenLineEdit.setObjectName(u"tokenLineEdit")
        self.tokenLineEdit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.gridLayout.addWidget(self.tokenLineEdit, 2, 1, 1, 1)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)

        self.credsIdLabel = QLabel(self.widget)
        self.credsIdLabel.setObjectName(u"credsIdLabel")

        self.gridLayout.addWidget(self.credsIdLabel, 4, 0, 1, 1)

        self.credsIdLineEdit = QLineEdit(self.widget)
        self.credsIdLineEdit.setObjectName(u"credsIdLineEdit")

        self.gridLayout.addWidget(self.credsIdLineEdit, 4, 1, 1, 1)

        self.sshUserLabel = QLabel(self.widget)
        self.sshUserLabel.setObjectName(u"sshUserLabel")

        self.gridLayout.addWidget(self.sshUserLabel, 5, 0, 1, 1)

        self.sshUserLineEdit = QLineEdit(self.widget)
        self.sshUserLineEdit.setObjectName(u"sshUserLineEdit")

        self.gridLayout.addWidget(self.sshUserLineEdit, 5, 1, 1, 1)

        self.privateKeyLabel = QLabel(self.widget)
        self.privateKeyLabel.setObjectName(u"privateKeyLabel")

        self.gridLayout.addWidget(self.privateKeyLabel, 6, 0, 1, 1)

        self.privateKeyLineEdit = QLineEdit(self.widget)
        self.privateKeyLineEdit.setObjectName(u"privateKeyLineEdit")

        self.gridLayout.addWidget(self.privateKeyLineEdit, 6, 1, 1, 1)

        self.keyPassphraseLabel = QLabel(self.widget)
        self.keyPassphraseLabel.setObjectName(u"keyPassphraseLabel")

        self.gridLayout.addWidget(self.keyPassphraseLabel, 7, 0, 1, 1)

        self.keyPassphraseLineEdit = QLineEdit(self.widget)
        self.keyPassphraseLineEdit.setObjectName(u"keyPassphraseLineEdit")
        self.keyPassphraseLineEdit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.gridLayout.addWidget(self.keyPassphraseLineEdit, 7, 1, 1, 1)

        self.descriptionLabel = QLabel(self.widget)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.gridLayout.addWidget(self.descriptionLabel, 8, 0, 1, 1)

        self.descriptionLineEdit = QLineEdit(self.widget)
        self.descriptionLineEdit.setObjectName(u"descriptionLineEdit")

        self.gridLayout.addWidget(self.descriptionLineEdit, 8, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(self.widget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 9, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"SSH key wrangling", None))
        self.UrlLabel.setText(QCoreApplication.translate("Dialog", u"URL", None))
        self.UsernameLabel.setText(QCoreApplication.translate("Dialog", u"Jenkins username", None))
        self.tokenLabel.setText(QCoreApplication.translate("Dialog", u"token/password", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Add SSH key as credential", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Add and encrypted SSH key as credential", None))

        self.credsIdLabel.setText(QCoreApplication.translate("Dialog", u"credentials ID", None))
        self.sshUserLabel.setText(QCoreApplication.translate("Dialog", u"ssh user", None))
        self.privateKeyLabel.setText(QCoreApplication.translate("Dialog", u"private key", None))
        self.keyPassphraseLabel.setText(QCoreApplication.translate("Dialog", u"key passphrase", None))
        self.descriptionLabel.setText(QCoreApplication.translate("Dialog", u"description", None))
    # retranslateUi

