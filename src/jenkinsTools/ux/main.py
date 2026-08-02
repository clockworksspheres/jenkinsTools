import sys

from pathlib import Path

parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))

from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtGui import QAction, QShortcut, QKeySequence
from PySide6.QtCore import Qt

from ux.nodeMain import nodeWidget
from ux.ui_main import Ui_MainWindow

class JenkinsToolsUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connect quit button
        self.ui.quitPushButton.clicked.connect(self.close)

        # connect ssh button
        self.ui.sshCredsPushButton.clicked.connect(self.openSshCredsWidget)

        # connect nodes button
        self.ui.nodesPushButton.clicked.connect(self.openNodesWidget)

        # connect pipelines button
        self.ui.pipelinesPushButton.clicked.connect(self.openPipelinesWidget)

    def openSshCredsWidget(self):
        print("stub for opening ssh creds window")

    def openNodesWidget(self):
        nodes = nodeWidget()
        nodes.show()
        if sys.platform.lower().startswith("darwin"):
            try:
                nodes._raise()
                nodes.activateWindow()
            except AttributeError:
                print("AttributeError detected, but not applicable here...")
                nodes._raise()
                nodes.activateWindow()
            print("\n ### NOTE: AttributeError not applicable here...")

    def openPipelinesWidget(self):
        print("stub for opening pipelines window")


if __name__=="__main__":
    app = QApplication(sys.argv)
    widget = JenkinsToolsUi()
    widget.show()
    sys.exit(app.exec())
    

