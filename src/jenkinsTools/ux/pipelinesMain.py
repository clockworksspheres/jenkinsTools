# This Python file uses the following encoding: utf-8
import sys
import re
import json
from argparse import Namespace

from pathlib import Path

parent_dir = Path(__file__).parent.parent
sys.path.append(str(parent_dir))

from PySide6.QtWidgets import QApplication, QDialog, QFileDialog
from PySide6.QtCore import Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic pipelinesDialog.ui -o ui_pipelinesDialog.py
from ux.ui_pipelinesDialog import Ui_Dialog

class pipelinesDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Set current (default) page in the stacked widget
        self.ui.stackedWidget.setCurrentIndex(0)

        # Set current(default) page of combo boxes
        self.ui.ActionComboBox.setCurrentIndex(0)
        self.ui.MethodComboBox.setCurrentIndex(0)

        # combo box actions
        self.ui.ActionComboBox.currentIndexChanged.connect(self.handleActionComboBoxChange)
        self.ui.MethodComboBox.currentIndexChanged.connect(self.handleMethodComboBoxChange)
        self.ui.followComboBox.currentIndexChanged.connect(self.handleFollowComboBoxChange)

        # Button actions
        self.ui.closePushButton.clicked.connect(self.close)
        self.ui.RunPushButton.clicked.connect(self.runAction)
        self.ui.xmlFilePushButton.clicked.connect(self.getXmlFileLocation)

        # Hiding functionality that doesn't yet do the right thing
        self.ui.MethodLabel.hide()
        self.ui.MethodComboBox.hide()
        self.ui.scriptLabel.hide()
        self.ui.scriptLineEdit.hide()
        self.ui.scriptPathLabel.hide()
        self.ui.scriptPathLineEdit.hide()

        # Setting tab focus on first stacked widget
        self.ui.UrlLineEdit.setFocus()

        self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
        self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
        self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
        self.setTabOrder(self.ui.ActionComboBox, self.ui.MethodComboBox)
        self.setTabOrder(self.ui.MethodComboBox, self.ui.jobNameLineEdit)
        self.setTabOrder(self.ui.jobNameLineEdit, self.ui.repoLineEdit)
        self.setTabOrder(self.ui.repoLineEdit, self.ui.branchLineEdit)
        self.setTabOrder(self.ui.branchLineEdit, self.ui.jenkinsfileLineEdit)
        self.setTabOrder(self.ui.jenkinsfileLineEdit, self.ui.credsIdLineEdit)
        self.setTabOrder(self.ui.credsIdLineEdit, self.ui.scriptLineEdit)
        self.setTabOrder(self.ui.scriptLineEdit, self.ui.scriptPathLineEdit)
        self.setTabOrder(self.ui.scriptPathLineEdit, self.ui.descriptionLineEdit)
        self.setTabOrder(self.ui.descriptionLineEdit, self.ui.RunPushButton)
        self.setTabOrder(self.ui.RunPushButton, self.ui.closePushButton)
        self.setTabOrder(self.ui.closePushButton, self.ui.UrlLineEdit)

    def runAction(self):
        print(f"Running command '{self.ui.ActionComboBox.currentText()}'")

        selected_text = self.ui.ActionComboBox.currentText()

        print(f"selected text: '{selected_text}'")

        action = {}

        action["url"] = self.ui.UrlLineEdit.text()
        action["user"] = self.ui.UsernameLineEdit.text()
        action["token"] = self.ui.tokenLineEdit.text()

        if action["url"] and \
           action["user"] and \
           action["token"]:
            print ("action acquired")
        else:
            raise ValueError("url, user and token fields required.")

        if selected_text == "create":
            self.ui.MethodLabel.hide()
            self.ui.MethodComboBox.hide()

            action["method"] = self.ui.MethodComboBox.currentText()
            # if action["method"] == "scm":

            # if validateJobNameLineEdit(self.ui.jobNameLineEdit.text()):
            if self.ui.jobNameLineEdit.text():
                action['job'] = self.ui.jobNameLineEdit.text()
            if self.ui.repoLineEdit.text():
                action['repo'] = self.ui.repoLineEdit.text()
            if self.ui.branchLineEdit.text():
                action['branch'] = self.ui.branchLineEdit.text()
            if self.ui.jenkinsfileLineEdit.text():
                action['jenkinsfile'] = self.ui.jenkinsfileLineEdit.text()
            if self.ui.credsIdLineEdit.text():
                action['credentials_id'] = self.ui.credsIdLineEdit.text()
            if self.ui.descriptionLineEdit.text():
                action['description'] = self.ui.descriptionLineEdit.text()

            print(str(action))

            args = Namespace(**action)
            print(f"Adding {args.url} for node <{args.job}>...")

            from JenkinsTools.CreateJenkinsPipeline import CreateJenkinsPipeline as createPipeline

            cjp = createPipeline()
            cjp.create_jenkins_pipeline(args)

        elif selected_text == "run":

            if self.ui.jobNameLineEdit_2.text():
                action['job'] = self.ui.jobNameLineEdit_2.text()
            else:
                raise ValueError("job field required.")

            action['follow'] = self.ui.followComboBox.currentText()

            if self.ui.followComboBox.currentText() == "Yes":
                action['follow'] = True
            elif self.ui.followComboBox.currentText() == "No":
                action['follow'] = False
            else:
                raise ValueError("follow variable out of bounds.")

            if self.ui.parametersLineEdit_2.text():
                action['param'] = self.ui.parametersLineEdit_2.text()

            if self.ui.tokenBuildLineEdit_2.text():
                action["token_build"] = self.ui.tokenBuildLineEdit_2.text()
        
            print(str(action))

            args = Namespace(**action)
            print(f"Adding {args.url} for node <{args.job}>...")

            from JenkinsTools.RunJenkinsPipeline import RunJenkinsPipeline as runPipeline

            rpipeline = runPipeline()
            rpipeline.controller(args)

        elif selected_text == "check":

            if self.ui.jobNameLineEdit_3.text():
                action['job'] = self.ui.jobNameLineEdit_3.text()
            else:
                raise ValueError("job field required.")

            if self.ui.followComboBox.currentText() == "Yes":
                action['follow'] = True
            elif self.ui.followComboBox.currentText() == "No":
                action['follow'] = False
            else:
                raise ValueError("follow variable out of bounds.")

            print(str(action))

            args = Namespace(**action)
            print(f"Adding {args.url} for node <{args.job}>...")
            from JenkinsTools.CheckJenkinsPipelineRun import CheckJenkinsPipelineRun as checkPipeline

            ckpipeline = checkPipeline()
            ckpipeline.get_full_run(args)

            '''
            if args.get_full_run:
                ckpipeline.get_full_run(args)
            else:
                ckpipeline.check_run(args)
            '''

        elif selected_text == "get-config":

            if self.ui.jobNameLineEdit_2.text():
                action['job'] = self.ui.jobNameLineEdit_3.text()
            else:
                raise ValueError("job field required.")

            print(str(action))

            args = Namespace(**action)
            print(f"Adding {args.url} for node <{args.job}>...")
            from JenkinsTools.ConfigJob import ConfigJob

            config_job = ConfigJob(args)
            config_job.cmd_get_config()

        elif selected_text == "set-config":

            if self.ui.jobNameLineEdit_2.text():
                action['job'] = self.ui.jobNameLineEdit_3.text()
            else:
                raise ValueError("job field required.")

            print(str(action))

            args = Namespace(**action)
            print(f"Adding {args.url} for node <{args.job}>...")
            from JenkinsTools.ConfigJob import ConfigJob

            config_job = ConfigJob(args)
            config_job.cmd_set_config()

        else:
           print("not a valid combobox value")

    def handleActionComboBoxChange(self):

        selected_text = self.ui.ActionComboBox.currentText()

        print(f"selected text: '{selected_text}'")

        if selected_text == "create":
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.MethodLabel.hide()
            self.ui.MethodComboBox.hide()
            self.ui.scriptLabel.hide()
            self.ui.scriptLineEdit.hide()
            self.ui.scriptPathLabel.hide()
            self.ui.scriptPathLineEdit.hide()

            # Setting tab focus on first stacked widget
            self.ui.UrlLineEdit.setFocus()

            self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
            self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
            self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
            self.setTabOrder(self.ui.ActionComboBox, self.ui.MethodComboBox)
            self.setTabOrder(self.ui.MethodComboBox, self.ui.jobNameLineEdit)
            self.setTabOrder(self.ui.jobNameLineEdit, self.ui.repoLineEdit)
            self.setTabOrder(self.ui.repoLineEdit, self.ui.branchLineEdit)
            self.setTabOrder(self.ui.branchLineEdit, self.ui.jenkinsfileLineEdit)
            self.setTabOrder(self.ui.jenkinsfileLineEdit, self.ui.credsIdLineEdit)
            self.setTabOrder(self.ui.credsIdLineEdit, self.ui.scriptLineEdit)
            self.setTabOrder(self.ui.scriptLineEdit, self.ui.scriptPathLineEdit)
            self.setTabOrder(self.ui.scriptPathLineEdit, self.ui.descriptionLineEdit)
            self.setTabOrder(self.ui.descriptionLineEdit, self.ui.RunPushButton)
            self.setTabOrder(self.ui.RunPushButton, self.ui.closePushButton)
            self.setTabOrder(self.ui.closePushButton, self.ui.UrlLineEdit)

        elif selected_text == "run":
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.MethodLabel.hide()
            self.ui.MethodComboBox.hide()
            self.ui.followLabel.hide()
            self.ui.followComboBox.hide()
            
            # Setting tab focus on first stacked widget
            self.ui.UrlLineEdit.setFocus()

            self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
            self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
            self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
            self.setTabOrder(self.ui.ActionComboBox, self.ui.JobNameLineEdit_2)
            self.setTabOrder(self.ui.JobNameLineEdit_2, self.ui.followComboBox)
            self.setTabOrder(self.ui.followComboBox, self.ui.parametersLineEdit_2)
            self.setTabOrder(self.ui.parametersLineEdit_2, self.ui.tokenBuildLineEdit_2)
            self.setTabOrder(self.ui.tokenBuildLineEdit_2, self.ui.RunPushButton)
            self.setTabOrder(self.ui.RunPushButton, self.ui.closePushButton)
            self.setTabOrder(self.ui.closePushButton, self.ui.UrlLineEdit)

        elif selected_text == "check":
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.MethodLabel.hide()
            self.ui.MethodComboBox.hide()
            self.ui.xmlFilePushButton.hide()
            self.ui.xmlFileLineEdit.hide()

            # Setting tab focus on first stacked widget
            self.ui.UrlLineEdit.setFocus()
            self.ui.GetNodeTextEdit.setFocusPolicy(Qt.NoFocus)

            self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
            self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
            self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
            self.setTabOrder(self.ui.ActionComboBox, self.ui.jobNameLineEdit_3)
            self.setTabOrder(self.ui.jobNameLineEdit_3, self.ui.RunPushButton)
            self.setTabOrder(self.ui.RunPushButton, self.ui.closePushButton)
            self.setTabOrder(self.ui.closePushButton, self.ui.UrlLineEdit)


        elif selected_text == "get-config":
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.MethodLabel.hide()
            self.ui.MethodComboBox.hide()
            self.ui.xmlFilePushButton.hide()
            self.ui.xmlFileLineEdit.hide()

            # Setting tab focus on first stacked widget
            self.ui.UrlLineEdit.setFocus()
            self.ui.GetNodeTextEdit.setFocusPolicy(Qt.NoFocus)

            self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
            self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
            self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
            self.setTabOrder(self.ui.ActionComboBox, self.ui.jobNameLineEdit_3)
            self.setTabOrder(self.ui.jobNameLineEdit_3, self.ui.RunPushButton)
            self.setTabOrder(self.ui.RunPushButton, self.ui.closePushButton)
            self.setTabOrder(self.ui.closePushButton, self.ui.UrlLineEdit)

        elif selected_text == "set-config":
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.MethodLabel.hide()
            self.ui.MethodComboBox.hide()
            self.ui.xmlFilePushButton.show()
            self.ui.xmlFileLineEdit.show()

            # Setting tab focus on first stacked widget
            self.ui.UrlLineEdit.setFocus()
            self.ui.GetNodeTextEdit.setFocusPolicy(Qt.NoFocus)

            self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
            self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
            self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
            self.setTabOrder(self.ui.ActionComboBox, self.ui.jobNameLineEdit_3)
            self.setTabOrder(self.ui.jobNameLineEdit_3, self.ui.xmlFileLineEdit)
            self.setTabOrder(self.ui.xmlFileLineEdit, self.ui.RunPushButton)
            self.setTabOrder(self.ui.RunPushButton, self.ui.closePushButton)
            self.setTabOrder(self.ui.closePushButton, self.ui.UrlLineEdit)

        else:
            raise ValueError("Not a valid comboBox value")

    def handleMethodComboBoxChange(self):

        selected_text = self.ui.MethodComboBox.currentText()

        print(f"selected text: '{selected_text}'")

    def handleFollowComboBoxChange(self):

        selected_text = self.ui.followComboBox.currentText()

        print(f"selected text: '{selected_text}'")

    def getXmlFileLocation(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "",
            "All Files (*);;Text Files (*.txt)"
        )

        if filePath:
            self.ui.xmlFileLineEdit.setText(filePath)

    def closeEvent(self, event):
        '''
        Catch when the red x (exit) window button is clicked
        '''
        print("Dialog close event triggered.")
        event.accept()  # Allow the dialog to close
        # DO NOT call app.quit() or sys.exit() here


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = pipelinesDialog()
    dialog.show()
    sys.exit(app.exec())




