
import sys

from pathlib import Path

parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))

from PySide6.QtWidgets import (QDialog, QVBoxLayout,
                               QLabel, QDialogButtonBox)
from PySide6.QtCore import Qt


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


