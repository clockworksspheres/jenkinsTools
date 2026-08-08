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
        Dialog.resize(460, 363)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.privateKeyLabel = QLabel(Dialog)
        self.privateKeyLabel.setObjectName(u"privateKeyLabel")

        self.gridLayout.addWidget(self.privateKeyLabel, 7, 0, 1, 1)

        self.UsernameLabel = QLabel(Dialog)
        self.UsernameLabel.setObjectName(u"UsernameLabel")

        self.gridLayout.addWidget(self.UsernameLabel, 1, 0, 1, 1)

        self.credsIdLineEdit = QLineEdit(Dialog)
        self.credsIdLineEdit.setObjectName(u"credsIdLineEdit")

        self.gridLayout.addWidget(self.credsIdLineEdit, 4, 1, 1, 1)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)

        self.sshUserLabel = QLabel(Dialog)
        self.sshUserLabel.setObjectName(u"sshUserLabel")

        self.gridLayout.addWidget(self.sshUserLabel, 5, 0, 1, 1)

        self.descriptionLabel = QLabel(Dialog)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.gridLayout.addWidget(self.descriptionLabel, 6, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 9, 1, 1, 1)

        self.keyPassphraseLineEdit = QLineEdit(Dialog)
        self.keyPassphraseLineEdit.setObjectName(u"keyPassphraseLineEdit")

        self.gridLayout.addWidget(self.keyPassphraseLineEdit, 8, 1, 1, 1)

        self.UrlLineEdit = QLineEdit(Dialog)
        self.UrlLineEdit.setObjectName(u"UrlLineEdit")

        self.gridLayout.addWidget(self.UrlLineEdit, 0, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.tokenLabel = QLabel(Dialog)
        self.tokenLabel.setObjectName(u"tokenLabel")

        self.gridLayout.addWidget(self.tokenLabel, 2, 0, 1, 1)

        self.privateKeyLineEdit = QLineEdit(Dialog)
        self.privateKeyLineEdit.setObjectName(u"privateKeyLineEdit")
        self.privateKeyLineEdit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.gridLayout.addWidget(self.privateKeyLineEdit, 7, 1, 1, 1)

        self.keyPassphraseLabel = QLabel(Dialog)
        self.keyPassphraseLabel.setObjectName(u"keyPassphraseLabel")

        self.gridLayout.addWidget(self.keyPassphraseLabel, 8, 0, 1, 1)

        self.sshUserLineEdit = QLineEdit(Dialog)
        self.sshUserLineEdit.setObjectName(u"sshUserLineEdit")

        self.gridLayout.addWidget(self.sshUserLineEdit, 5, 1, 1, 1)

        self.UrlLabel = QLabel(Dialog)
        self.UrlLabel.setObjectName(u"UrlLabel")

        self.gridLayout.addWidget(self.UrlLabel, 0, 0, 1, 1)

        self.credsIdLabel = QLabel(Dialog)
        self.credsIdLabel.setObjectName(u"credsIdLabel")

        self.gridLayout.addWidget(self.credsIdLabel, 4, 0, 1, 1)

        self.descriptionLineEdit = QLineEdit(Dialog)
        self.descriptionLineEdit.setObjectName(u"descriptionLineEdit")

        self.gridLayout.addWidget(self.descriptionLineEdit, 6, 1, 1, 1)

        self.UsernameLineEdit = QLineEdit(Dialog)
        self.UsernameLineEdit.setObjectName(u"UsernameLineEdit")

        self.gridLayout.addWidget(self.UsernameLineEdit, 1, 1, 1, 1)

        self.tokenLineEdit = QLineEdit(Dialog)
        self.tokenLineEdit.setObjectName(u"tokenLineEdit")
        self.tokenLineEdit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.gridLayout.addWidget(self.tokenLineEdit, 2, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.privateKeyLabel.setText(QCoreApplication.translate("Dialog", u"private key", None))
        self.UsernameLabel.setText(QCoreApplication.translate("Dialog", u"Jenkins username", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Add SSH key as credential", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Add and encrypted SSH key as credential", None))

        self.sshUserLabel.setText(QCoreApplication.translate("Dialog", u"ssh user", None))
        self.descriptionLabel.setText(QCoreApplication.translate("Dialog", u"description", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Method", None))
        self.tokenLabel.setText(QCoreApplication.translate("Dialog", u"token/password", None))
        self.keyPassphraseLabel.setText(QCoreApplication.translate("Dialog", u"key passphrase", None))
        self.UrlLabel.setText(QCoreApplication.translate("Dialog", u"URL", None))
        self.credsIdLabel.setText(QCoreApplication.translate("Dialog", u"credentials ID", None))
    # retranslateUi

