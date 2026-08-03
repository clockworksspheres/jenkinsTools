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
from ux.ui_nodesDialog import Ui_Dialog

class pipelinesDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)




