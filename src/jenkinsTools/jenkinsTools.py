import sys



from PySide6.QtWidgets import QApplication

if __name__=="__main__":

    from ux.main import JenkinsToolsUi

    app = QApplication(sys.argv)
    widget = JenkinsToolsUi()
    widget.show()
    sys.exit(app.exec())
    
