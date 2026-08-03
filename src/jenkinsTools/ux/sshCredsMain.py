import sys

from pathlib import Path

parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))

from PySide6.QtWidgets import QApplication, QDialog, QDialogButtonBox
from PySide6.QtCore import Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py
from ux.ui_sshCredsDialog import Ui_Dialog


class SshCredsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # rename the ok button to "Run"
        buttonBox = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        buttonBox.setText("Run")

        # Connect buttonbox signals to slots
        self.ui.buttonBox.accepted.connect(self.onRunButtonClicked)
        self.ui.buttonBox.rejected.connect(self.reject)

        # connect comboBox actions to slots
        self.ui.comboBox.connect(self.comboBoxActivate)

    def onRunButtonClicked(self):
        print("Run button clicked")

    def comboBoxActivate(self):
        print("Combo Box Activated")
        text = self.ui.comboBox.currentText()

        if text == "Add SSH key as credential":
            print("comboBox 'Add SSH key as credential' selected")

        elif text == "Add and encrypted SSH key as credential":
            print("comboBox 'Add and encrypted SSH key as credential' selected")

        else:
            raise ValueError("ComboBox selection out of bounds...")

if __name__ == "__main__":
    __package__ = "jenkinsTools.ux"
    app = QApplication(sys.argv)
    dialog = SshCredsDialog()
    dialog.show()
    sys.exit(app.exec())

