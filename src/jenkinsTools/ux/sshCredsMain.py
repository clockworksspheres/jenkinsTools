import sys
import traceback
from argparse import Namespace

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

        # Set the window title
        self.setWindowTitle("SSH creds wrangling")

        # rename the ok button to "Run"
        buttonBox = self.ui.buttonBox.button(QDialogButtonBox.Ok)
        buttonBox.setText("Run")

        # rename the cancel button to close
        buttonbox = self.ui.buttonBox.button(QDialogButtonBox.Cancel)
        buttonbox.setText("Close")

        # Connect buttonbox signals to slots
        self.ui.buttonBox.accepted.connect(self.onRunButtonClicked)
        self.ui.buttonBox.rejected.connect(self.reject)

        # connect comboBox actions to slots
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox.currentIndexChanged.connect(self.comboBoxActivate)

        # hide fields based on default comboBox selection
        self.ui.keyPassphraseLabel.hide()
        self.ui.keyPassphraseLineEdit.hide()

        # Set the tab order between fields, buttons and comboBox
        self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
        self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
        self.setTabOrder(self.ui.tokenLineEdit, self.ui.comboBox)
        self.setTabOrder(self.ui.comboBox, self.ui.credsIdLineEdit)
        self.setTabOrder(self.ui.credsIdLineEdit, self.ui.sshUserLineEdit)
        self.setTabOrder(self.ui.sshUserLineEdit, self.ui.descriptionLineEdit)
        self.setTabOrder(self.ui.descriptionLineEdit, self.ui.privateKeyLineEdit)
        self.setTabOrder(self.ui.privateKeyLineEdit, self.ui.keyPassphraseLineEdit)
        self.setTabOrder(self.ui.keyPassphraseLineEdit, self.ui.buttonBox)
        self.setTabOrder(self.ui.buttonBox, self.ui.UrlLineEdit)

    def onRunButtonClicked(self):
        print("Run button clicked")

        action = {}

        action["url"] = self.ui.UrlLineEdit.text()
        action["jenkins_user"] = self.ui.UsernameLineEdit.text()
        action["jenkins_token"] = self.ui.tokenLineEdit.text()

        if action["url"] and \
           action["jenkins_user"] and \
           action["jenkins_token"]:
            print ("first three fields aquired")
        else:
            raise ValueError("url, user and token fields required.")

        if self.ui.credsIdLineEdit.text():
            action["credential_id"] = self.ui.credsIdLineEdit.text()
        if self.ui.sshUserLineEdit.text():
            action["ssh_user"] = self.ui.sshUserLineEdit.text()
        if self.ui.descriptionLineEdit.text():
            action["description"] = self.ui.descriptionLineEdit.text()
        if self.ui.privateKeyLineEdit.text():
            action["private_key"] = self.ui.privateKeyLineEdit.text()

        text = self.ui.comboBox.currentText()

        if text == "Add SSH key as credential":
            print("non-encrypted key")
            
        elif text == "Add and encrypted SSH key as credential":
            print("encrypted key")
            if self.ui.keyPassphraseLineEdit.text():
                action["key_passphrase"] = self.ui.keyPassphraseLineEdit.text()
            else:
                raise ValueError("Need a key passphrase")
        else:
            raise ValueError("Not a valid comboBox value")

        print(str(action))

        args = Namespace(**action)
        print(f"Adding {args.url} for node <{args.ssh_user}>...")

        from JenkinsTools.AddSshKeyCredential import SshKeyWrangling

        keyWrangling = SshKeyWrangling()

        try:
            private_key = keyWrangling.load_private_key(args.private_key)
            keyWrangling.add_ssh_private_key_credential(
                jenkins_url=args.url,
                jenkins_user=args.jenkins_user,
                jenkins_token=args.jenkins_token,
                credential_id=args.credential_id,
                ssh_username=args.ssh_user,
                private_key=args.private_key,
                passphrase=args.key_passphrase,
                description=args.description,
            )
        except Exception:
            print(traceback.format_exc())
        else:
            print(f"Credential '{args.credential_id}' added to Jenkins successfully")

    def comboBoxActivate(self):
        print("Combo Box Activated")
        text = self.ui.comboBox.currentText()

        if text == "Add SSH key as credential":
            print("comboBox 'Add SSH key as credential' selected")
            self.ui.keyPassphraseLabel.hide()
            self.ui.keyPassphraseLineEdit.hide()

        elif text == "Add and encrypted SSH key as credential":
            print("comboBox 'Add and encrypted SSH key as credential' selected")
            self.ui.keyPassphraseLabel.show()
            self.ui.keyPassphraseLineEdit.show()

        else:
            raise ValueError("ComboBox selection out of bounds...")

    def closeEvent(self, event):
        '''
        Catch when the red x (exit) window button is clicked
        '''
        print("Dialog close event triggered.")
        event.accept()  # Allow the dialog to close
        # DO NOT call app.quit() or sys.exit() here


if __name__ == "__main__":
    __package__ = "jenkinsTools.ux"
    app = QApplication(sys.argv)
    dialog = SshCredsDialog()
    dialog.show()
    sys.exit(app.exec())

