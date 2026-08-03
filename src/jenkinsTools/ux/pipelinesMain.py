# This Python file uses the following encoding: utf-8
import sys
import re
import json
from argparse import Namespace

from pathlib import Path

parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))

from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtCore import Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
from ux.ui_pipelinesDialog import Ui_Dialog

class pipelinesDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Set current (default) page in the stacked widget
        self.ui.stackedWidget.setCurrentIndex(0)

        # Set current(default) page of combo boxes
        self.ui.ActionComboBox.setCurrentIndex(0)
        self.ui.MethodComboBox.setCurrentIndex(0)

        # combo box actions
        self.ui.ActionComboBox.currentIndexChanged.connect(self.handleActionComboBoxChange)
        self.ui.MethodComboBox.currentIndexChanged.connect(self.handleMethodComboBoxChange)

        # Button actions
        self.ui.QuitPushButton.clicked.connect(self.close)
        self.ui.RunPushButton.clicked.connect(self.runAction)

    def runAction(self):
        print(f"Running command '{self.ui.ActionComboBox.currentText()}'")

    def handleActionComboBoxChange(self):

        selected_text = self.ui.ActionComboBox.currentText()

        print(f"selected text: '{selected_text}'")

    def handleMethodComboBoxChange(self):

        selected_text = self.ui.MethodComboBox.currentText()

        print(f"selected text: '{selected_text}'")






