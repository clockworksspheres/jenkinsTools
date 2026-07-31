# This Python file uses the following encoding: utf-8
import sys
import re

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_nodeForm import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
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
        self.ui.RunPushButton.clicked.connect(self.runCommand)

    def runCommand(self):
        print(f"Running command '{self.ui.ActionComboBox.currentText()}'")

    def handleActionComboBoxChange(self):

        selected_text = self.ui.ActionComboBox.currentText()

        print(f"selected text: '{selected_text}'")

        if selected_text == "Add":
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.DescriptionLabel.show()
            self.ui.DescriptionLineEdit.show()
            self.ui.MethodLabel.show()
            self.ui.MethodComboBox.show()
        elif selected_text == "Update":
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.DescriptionLabel.hide()
            self.ui.DescriptionLineEdit.hide()
            self.ui.MethodLabel.hide()
            self.ui.MethodComboBox.hide()
        elif selected_text == "Get Nodes":
            self.ui.stackedWidget.setCurrentIndex(2)
            self.ui.DescriptionLineEdit.hide()
            self.ui.MethodLabel.hide()
        elif selected_text.strip() == "Get Node Info":
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.DescriptionLineEdit.hide()
            self.ui.MethodLabel.hide()
        elif selected_text.strip() == "Get Node Config":
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.DescriptionLineEdit.hide()
            self.ui.MethodLabel.hide()
        elif selected_text.strip() == "Node Exists":
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.DescriptionLineEdit.hide()
            self.ui.MethodLabel.hide()
        elif selected_text.strip() == "New Item":
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.DescriptionLineEdit.hide()
            self.ui.MethodLabel.hide()
        elif selected_text.strip() == "Delete":
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.DescriptionLineEdit.hide()
            self.ui.MethodLabel.hide()
        elif selected_text.strip() == "Disable":
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.DescriptionLineEdit.hide()
            self.ui.MethodLabel.hide()
        elif selected_text.strip() == "Enable":
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.DescriptionLineEdit.hide()
            self.ui.MethodLabel.hide()
        else:
            print("Not a valid comboBox value")

    def handleMethodComboBoxChange(self):

        selected_text = self.ui.MethodComboBox.currentText()

        print(f"selected text: '{selected_text}'")

        if re.match("SSH", selected_text):
            self.ui.stackedWidget.setCurrentIndex(0)
        elif re.match("JNLP", selected_text):
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            print("not a valid comboBox value")

 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
