import sys

from pathlib import Path

parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))

from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QDialog, QVBoxLayout,
                               QLabel, QDialogButtonBox)
from PySide6.QtCore import Qt

from ux.nodesMain import nodesDialog
from ux.ui_main import Ui_MainWindow
from ux.sshCredsMain import SshCredsDialog
from ux.pipelinesMain import pipelinesDialog
from ux.consoleDialog import ConsoleStream, ConsoleDialog


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

        # Hide the textEdit and remove the virticleSpacer by default
        existing_item = self.ui.gridLayout.itemAtPosition(4,1)
        if existing_item:
            self.ui.gridLayout.removeItem(existing_item)
        self.adjustSize()
        
        # Connect the debug button signal to slot
        self.ui.debugPushButton.clicked.connect(self.onDebugPushButtonClicked)

        self.console_dialogs = []

        # Shared stream that all open dialogs listen to
        self.stream = ConsoleStream()

        # Redirect stdout & stderr to our stream
        sys.stdout = self.stream
        sys.stderr = self.stream

        if sys.platform.lower().startswith("win32"):
            # non-modal on Windows11 only works if None is passed in rather than self.
            # problem is, all windows have to be closed separately...
            # fixed - check out closeEvent method - QApplication.closeAllWindows()
            self.conDialog = ConsoleDialog(None, title=f"Console #{len(self.console_dialogs) + 1}")
        else:
            self.conDialog = ConsoleDialog(self, title=f"Console #{len(self.console_dialogs) + 1}")

    def openSshCredsDialog(self):
        # show message box with mounted data
        msg = "stub for opening SSH creds window"
        dlg = SshCredsDialog(self)
        dlg.show()
        self.raise_()
  
    def openNodesDialog(self):

        # 1.  Create a standard QDialog
        nodes = nodesDialog(self)
        nodes.setWindowTitle("Work with Jenkins Nodes")

        # 2. show non-modally - Don't block until closed
        nodes.show()
        self.raise_()
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
        self.raise_()
        """
        retval = dlg.exec()
        if retval:
            print("User clicked OK, dialog accepted")
        else:
            print("Dialog Rejected")
        """

    def onDebugPushButtonClicked(self, checked):

        # Connect this dialog to the shared stream
        self.stream.text_emitted.connect(self.conDialog.append_html)

        self.ui.debugPushButton.hide()

        # Disconnect when the dialog is closed (prevents errors later)
        def on_finished():
            try:
                self.stream.text_emitted.disconnect(self.conDialog.append_html)
                self.ui.debugPushButton.show()
            except TypeError:
                pass  # already disconnected
            if self.conDialog in self.console_dialogs:
                self.console_dialogs.remove(self.conDialog)

        self.conDialog.finished.connect(on_finished)

        self.console_dialogs.append(self.conDialog)
        self.conDialog.show()
        self.raise_()

    def closeEvent(self, event):
        if sys.platform.lower().startswith("win32"):
            # Required for the way the self.conDialog is instanciated on Windows
            QApplication.closeAllWindows()
        event.accept()  # Let the window close

if __name__=="__main__":
    app = QApplication(sys.argv)

    # Ensure the app doesn't quit when the last window (dialog) is closed
    # app.setQuitOnLastWindowClosed(False)

    widget = JenkinsToolsUi()
    widget.show()
    sys.exit(app.exec())
    

