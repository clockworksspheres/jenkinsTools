import sys
import re

from pathlib import Path

parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))

from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QDialog, QVBoxLayout,
                               QLabel, QDialogButtonBox,
                               QSizePolicy, QSpacerItem,
                               QTextBrowser)
from PySide6.QtGui import QAction, QShortcut, QKeySequence, QFont
from PySide6.QtCore import Qt, QObject, Signal

from ux.nodesMain import nodesDialog
from ux.ui_main import Ui_MainWindow
from ux.sshCredsMain import SshCredsDialog
from ux.pipelinesMain import pipelinesDialog
from ux.consoleDialog import ConsoleStream, ConsoleDialog

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        """
        Not yet implemented error dialog
        """
        super().__init__(parent)
        self.setWindowTitle("Oops")

        self.button = QPushButton("Close")
        self.button.clicked.connect(self.accept)
        layout = QVBoxLayout()
        message = QLabel("Not Yet Implemented")
        layout.addWidget(message)
        layout.addWidget(self.button)
        self.setLayout(layout)


class CustomMessageDialog(QDialog):
    def __init__(self, parent=None, message=""):
        """
        Generic message dialog that shows the passed in message.
        """
        super().__init__(parent)

        # Set window title
        self.setWindowTitle("message")

        # Create layout
        layout = QVBoxLayout()

        # Add centered message label
        messageText = QLabel(f"{message}")
        messageText.setAlignment(Qt.AlignLeft)
        layout.addWidget(messageText)

        # Add single OK button
        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        layout.addWidget(button_box)

        # Connect the OK button to the accept slot
        button_box.accepted.connect(self.accept)
        '''
        self.button = QPushButton("Ok")
        self.button.setDefault(True)
        self.button.accepted.connect(self.accept)
        layout.addWidget(self.button)
        '''
        # Set the layout
        self.setLayout(layout)


class JenkinsToolsUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set the window title
        self.setWindowTitle("Jenkins Tools")

        # connect quit button and menu item
        self.ui.quitPushButton.clicked.connect(self.close)
        self.ui.actionQuit.triggered.connect(self.close)

        # connect ssh button & menu
        self.ui.sshCredsPushButton.clicked.connect(self.openSshCredsDialog)
        self.ui.actionSSH_creds_wrangling.triggered.connect(self.openSshCredsDialog)

        # connect nodes button & menu
        self.ui.nodesPushButton.clicked.connect(self.openNodesDialog)
        self.ui.actionWorking_with_Jenkins_Nodes.triggered.connect(self.openNodesDialog)

        # connect pipelines button & menu
        self.ui.pipelinesPushButton.clicked.connect(self.openPipelinesDialog)
        self.ui.actionWorking_with_Jenkins_Pipelines.triggered.connect(self.openPipelinesDialog)

        # set textEdit to read only
        self.ui.textBrowser.setReadOnly(True)
        # self.ui.textEdit.append("This line was added via code after setting it to read only...")

        # Hide the textEdit and remove the virticleSpacer by default
        self.ui.textBrowser.hide()
        existing_item = self.ui.gridLayout.itemAtPosition(4,1)
        if existing_item:
            self.ui.gridLayout.removeItem(existing_item)
        self.adjustSize()

        # Connect the radio button signal to slot
        self.ui.radioButton.clicked.connect(self.onRadioButtonClicked)

        # self.ui.textBrowser.append("application started")

        self.console_dialogs = []

        # Shared stream that all open dialogs listen to
        self.stream = ConsoleStream()

        # Redirect stdout & stderr to our stream
        sys.stdout = self.stream
        sys.stderr = self.stream

    def openSshCredsDialog(self):
        # show message box with mounted data
        msg = "stub for opening SSH creds window"
        dlg = SshCredsDialog(self)
        dlg.show()
  
    def openNodesDialog(self):

        # 1.  Create a standard QDialog
        nodes = nodesDialog(self)
        nodes.setWindowTitle("Work with Jenkins Nodes")

        # 2. show non-modally - Don't block until closed
        nodes.show()
        """
        # 2. Show modally (Blocks until closed)
        result = nodes.exec()

        if result == QDialog.Accepted:
            print("User Accepted")
        """

    def openPipelinesDialog(self):
        # show message box with mounted data
        msg = "stub for opening pipelines window"
        dlg = pipelinesDialog(self)
        dlg.show()
        """
        retval = dlg.exec()
        if retval:
            print("User clicked OK, dialog accepted")
        else:
            print("Dialog Rejected")
        """
    def onRadioButtonClicked(self, checked):
        dialog = ConsoleDialog(self, title=f"Console #{len(self.console_dialogs) + 1}")

        # Connect this dialog to the shared stream
        self.stream.text_emitted.connect(dialog.append_html)

        # Disconnect when the dialog is closed (prevents errors later)
        def on_finished():
            try:
                self.stream.text_emitted.disconnect(dialog.append_html)
            except TypeError:
                pass  # already disconnected
            if dialog in self.console_dialogs:
                self.console_dialogs.remove(dialog)

        dialog.finished.connect(on_finished)

        self.console_dialogs.append(dialog)
        dialog.show()


if __name__=="__main__":
    app = QApplication(sys.argv)
    widget = JenkinsToolsUi()
    widget.show()
    sys.exit(app.exec())
    

