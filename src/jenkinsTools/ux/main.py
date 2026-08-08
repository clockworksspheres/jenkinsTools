import sys

from pathlib import Path

parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))

from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QDialog, QVBoxLayout,
                               QLabel, QDialogButtonBox)
from PySide6.QtGui import QAction, QShortcut, QKeySequence
from PySide6.QtCore import Qt

from ux.nodesMain import nodesDialog
from ux.ui_main import Ui_MainWindow
from ux.sshCredsMain import SshCredsDialog
from ux.pipelinesMain import pipelinesDialog

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
        self.ui.textEdit.setReadOnly(True)
        # self.ui.textEdit.append("This line was added via code after setting it to read only...")

    def openSshCredsDialog(self):
        # show message box with mounted data
        msg = "stub for opening SSH creds window"
        dlg = SshCredsDialog(self)
        retval = dlg.exec()
        if retval:
            print("User clicked OK, dialog accepted")
        else:
            print("Dialog Rejected")
  
    def openNodesDialog(self):

        # 1.  Create a standard QDialog
        nodes = nodesDialog(self)
        nodes.setWindowTitle("Work with Jenkins Nodes")

        # 2. Show modally (Blocks until closed)
        result = nodes.exec()

        if result == QDialog.Accepted:
            print("User Accepted")

        '''
        #nodes.show()
        retval = nodes.exec()
        
        if sys.platform.lower().startswith("darwin"):
            nodes.raise_()
            nodes.activateWindow()
            print("\n ### NOTE: AttributeError not applicable here...")
        '''

    def openPipelinesDialog(self):
        # show message box with mounted data
        msg = "stub for opening pipelines window"
        dlg = pipelinesDialog(self)
        retval = dlg.exec()
        if retval:
            print("User clicked OK, dialog accepted")
        else:
            print("Dialog Rejected")
  

if __name__=="__main__":
    app = QApplication(sys.argv)
    widget = JenkinsToolsUi()
    widget.show()
    sys.exit(app.exec())
    

