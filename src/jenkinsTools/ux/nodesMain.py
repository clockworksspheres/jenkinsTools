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

class nodesDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Set the Window Title name
        self.setWindowTitle("Jenkins Node Tool")

        # Set current (default) page in the stacked widget
        self.ui.stackedWidget.setCurrentIndex(0)

        # Set current(default) page of combo boxes
        self.ui.ActionComboBox.setCurrentIndex(0)
        self.ui.MethodComboBox.setCurrentIndex(0)

        # combo box actions
        self.ui.ActionComboBox.currentIndexChanged.connect(self.handleActionComboBoxChange)
        self.ui.MethodComboBox.currentIndexChanged.connect(self.handleMethodComboBoxChange)

        # Button actions
        self.ui.QuitPushButton.clicked.connect(self.close)
        self.ui.RunPushButton.clicked.connect(self.runAction)

        # Set focus on the URL LineEdit
        self.ui.UrlLineEdit.setFocus()

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

        if selected_text == "Add":
            action["method"] = self.ui.MethodComboBox.currentText()

            if action["method"] == "SSH":
                action['name'] = self.ui.VmNameLineEdit.text()

                if action["name"]:
                    print ("name field acquired")
                else:
                    raise ValueError("name field required for this action.")
            
                action["credentials_id"] = self.ui.JenkinsCredsIdLineEdit.text()
                action["port"] = self.ui.PortLlineEdit.text()
                action["host"] = self.ui.HostnameOrIpLineEdit.text()
                action["labels"] = self.ui.LabelsLineEdit.text()
                action["executors"] = self.ui.ExecutorsLineEdit.text()
                action["description"] = self.ui.DescriptionLineEdit.text()
                action["remote_fs"] = self.ui.RemoteFsLineEdit.text()

            elif action["method"] == "JNLP":
                action['name'] = self.ui.VmNameLineEdit_2.text()

                if action["name"]:
                    print ("name field acquired")
                else:
                    raise ValueError("name field required for this action.")
                
                action['jvm_options'] = self.ui.JVMOptionsLineEdit.text()
                action["host"] = self.ui.HostnameOrIpLineEdit_2.text()
                action["labels"] = self.ui.LabelsLineEdit_2.text()
                action["executors"] = self.ui.ExecutorsLineEdit_2.text()
                action["description"] = self.ui.DescriptionLineEdit_2.text()
                action["remote_fs"] = self.ui.RemoteFsLineEdit_2.text()

            print(str(action))

            args = Namespace(**action)
            print(f"Adding {args.url} for node <{args.name}>...")

            from JenkinsTools.AddJenkinsNode import AddJenkinsNode

            addNode = AddJenkinsNode(args)
            addNode.add_jenkins_node()

        elif selected_text == "Update":
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.DescriptionLabel.hide()
            self.ui.DescriptionLineEdit.hide()
            self.ui.MethodLabel.hide()
            self.ui.MethodComboBox.hide()

            action['name'] = self.ui.VmNameLineEdit.text()

            if action["name"]:
                print ("action acquired")
            else:
                raise ValueError("name field required for this action.")
           
            action["method"] = self.ui.MethodComboBox.currentText()

            if action["method"] == "SSH":
                action["credentials_id"] = self.ui.JenkinsCredsIdLineEdit.text()
                action["port"] = self.ui.PortLlineEdit.text()
            elif action["method"] == "JNLP":
                action[''] = self.ui.jvmOptionsLineEdit.text()

            action["host"] = self.ui.HostnameOrIpLineEdit.text()
            action["labels"] = self.ui.LabelsLineEdit.text()
            action["executors"] = self.ui.ExecutorsLineEdit.text()
            action["description"] = self.ui.DescriptionLineEdit.text()
            action["remote_fs"] = self.ui.RemoteFsLineEdit.text()

            print(str(action))

            args = Namespace(**action)
            print(f"Adding {args.url} for node <{args.name}>...")

            from JenkinsTools.update_node import cmd_update_node

            # THIS IS CORRECT - it's just a function call, unlike the other actions.
            cmd_update_node(args)

        elif selected_text == "Get Nodes":
            self.ui.stackedWidget.setCurrentIndex(2)
            self.ui.DescriptionLineEdit.hide()
            self.ui.MethodLabel.hide()

            print(str(action))

            args = Namespace(**action)
            print(f"Adding {args.url} for node <{args.name}>...")

            from JenkinsTools.NodeStatus import NodeStatus
            ns = NodeStatus(args)
            print(ns.get_nodes())            

        elif selected_text.strip() == "Get Node Info":
            self.ui.stackedWidget.setCurrentIndex(3)

            action['name'] = self.ui.VmNameLineEdit_3.text()

            if action["name"]:
                print ("action acquired")
            else:
                raise ValueError("name field required for this action.")
            
            print(str(action))

            args = Namespace(**action)
            print(f"Adding {args.url} for node <{args.name}>...")

            from JenkinsTools.NodeStatus import NodeStatus
            ns = NodeStatus(args)
            print(json.dumps(ns.get_node_info(), indent=4))

        elif selected_text.strip() == "Get Node Config":
            self.ui.stackedWidget.setCurrentIndex(3)

            action['name'] = self.ui.VmNameLineEdit_3.text()

            if action["name"]:
                print ("action acquired")
            else:
                raise ValueError("name field required for this action.")
            
            print(str(action))

            args = Namespace(**action)
            print(f"Adding {args.url} for node <{args.name}>...")

            from JenkinsTools.NodeStatus import NodeStatus
            ns = NodeStatus(args)
            print(ns.get_node_config())

        elif selected_text.strip() == "Node Exists":
            self.ui.stackedWidget.setCurrentIndex(3)

            action['name'] = self.ui.VmNameLineEdit_3.text()

            if action["name"]:
                print ("action acquired")
            else:
                raise ValueError("name field required for this action.")
            
            print(str(action))

            args = Namespace(**action)
            print(f"Adding {args.url} for node <{args.name}>...")

            from JenkinsTools.NodeStatus import NodeStatus
            ns = NodeStatus(args)
            print(ns.node_exists())

        elif selected_text.strip() == "New Item":
            self.ui.stackedWidget.setCurrentIndex(3)

            action['name'] = self.ui.VmNameLineEdit_3.text()

            if action["name"]:
                print ("action acquired")
            else:
                raise ValueError("name field required for this action.")
            
            print(str(action))

            args = Namespace(**action)
            print(f"Adding {args.url} for node <{args.name}>...")

            raise Exception("Not yet implemented in the GUI...")

        elif selected_text.strip() == "Delete":
            self.ui.stackedWidget.setCurrentIndex(3)

            action['name'] = self.ui.VmNameLineEdit_3.text()

            if action["name"]:
                print ("action acquired")
            else:
                raise ValueError("name field required for this action.")
            
            print(str(action))

            args = Namespace(**action)
            print(f"Adding {args.url} for node <{args.name}>...")

            from JenkinsTools.NodeManage import NodeManage
            nm = NodeManage(args)
            print(nm.delete_node())

        elif selected_text.strip() == "Disable":
            self.ui.stackedWidget.setCurrentIndex(3)

            action['name'] = self.ui.VmNameLineEdit_3.text()

            if action["name"]:
                print ("action acquired")
            else:
                raise ValueError("name field required for this action.")
            
            print(str(action))

            args = Namespace(**action)
            print(f"Adding {args.url} for node <{args.name}>...")

            from JenkinsTools.NodeManage import NodeManage
            nm = NodeManage(args)
            print(nm.disable_node())

        elif selected_text.strip() == "Enable":
            self.ui.stackedWidget.setCurrentIndex(3)

            action['name'] = self.ui.VmNameLineEdit_3.text()

            if action["name"]:
                print ("action acquired")
            else:
                raise ValueError("name field required for this action.")
            
            print(str(action))

            args = Namespace(**action)
            print(f"Adding {args.url} for node <{args.name}>...")

            from JenkinsTools.NodeManage import NodeManage
            nm = NodeManage(args)
            print(nm.enable_node())

        else:
            print("not a valid combobox value")

    def handleActionComboBoxChange(self):

        selected_text = self.ui.ActionComboBox.currentText()

        print(f"selected text: '{selected_text}'")

        if selected_text == "Add":
            # Set focus on the URL LineEdit
            self.ui.UrlLineEdit.setFocus()

            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.DescriptionLabel.show()
            self.ui.DescriptionLineEdit.show()
            self.ui.MethodLabel.show()
            self.ui.MethodComboBox.show()

            if self.ui.MethodComboBox.currentText() == "SSH":
                self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
                self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
                self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
                self.setTabOrder(self.ui.ActionComboBox, self.ui.MethodComboBox)
                self.setTabOrder(self.ui.MethodComboBox, self.ui.VmNameLineEdit)
                self.setTabOrder(self.ui.VmNameLineEdit, self.ui.HostnameOrIpLineEdit)
                self.setTabOrder(self.ui.HostnameOrIpLineEdit, self.ui.LabelsLineEdit)
                self.setTabOrder(self.ui.LabelsLineEdit, self.ui.ExecutorsLineEdit)
                self.setTabOrder(self.ui.ExecutorsLineEdit, self.ui.JenkinsCredsIdLineEdit)
                self.setTabOrder(self.ui.JenkinsCredsIdLineEdit, self.ui.PortLlineEdit)
                self.setTabOrder(self.ui.PortLlineEdit, self.ui.DescriptionLineEdit)
                self.setTabOrder(self.ui.DescriptionLineEdit, self.ui.RemoteFsLineEdit)
                self.setTabOrder(self.ui.RemoteFsLineEdit, self.ui.RunPushButton)
                self.setTabOrder(self.ui.RunPushButton, self.ui.QuitPushButton)
                self.setTabOrder(self.ui.QuitPushButton, self.ui.UrlLineEdit)

            if self.ui.MethodComboBox.currentText() == "JNLP":
                self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
                self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
                self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
                self.setTabOrder(self.ui.ActionComboBox, self.ui.MethodComboBox)
                self.setTabOrder(self.ui.MethodComboBox, self.ui.VmNameLineEdit_2)
                self.setTabOrder(self.ui.VmNameLineEdit_2, self.ui.HostnameOrIpLineEdit_2)
                self.setTabOrder(self.ui.HostnameOrIpLineEdit_2, self.ui.LabelsLineEdit_2)
                self.setTabOrder(self.ui.LabelsLineEdit_2, self.ui.ExecutorsLineEdit_2)
                self.setTabOrder(self.ui.ExecutorsLineEdit_2, self.ui.JVMOptionsLineEdit)
                self.setTabOrder(self.ui.JVMOptionsLineEdit, self.ui.DescriptionLineEdit_2)
                self.setTabOrder(self.ui.DescriptionLineEdit_2, self.ui.RemoteFsLineEdit_2)
                self.setTabOrder(self.ui.RemoteFsLineEdit_2, self.ui.RunPushButton)
                self.setTabOrder(self.ui.RunPushButton, self.ui.QuitPushButton)
                self.setTabOrder(self.ui.QuitPushButton, self.ui.UrlLineEdit)

        elif selected_text == "Update":
           # Set focus on the URL LineEdit
            self.ui.UrlLineEdit.setFocus()

            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.DescriptionLabel.hide()
            self.ui.DescriptionLineEdit.hide()
            self.ui.MethodLabel.hide()
            self.ui.MethodComboBox.hide()

            self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
            self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
            self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
            self.setTabOrder(self.ui.ActionComboBox, self.ui.MethodComboBox)
            self.setTabOrder(self.ui.MethodComboBox, self.ui.VmNameLineEdit)
            self.setTabOrder(self.ui.VmNameLineEdit, self.ui.HostnameOrIpLineEdit)
            self.setTabOrder(self.ui.HostnameOrIpLineEdit, self.ui.LabelsLineEdit)
            self.setTabOrder(self.ui.LabelsLineEdit, self.ui.ExecutorsLineEdit)
            self.setTabOrder(self.ui.ExecutorsLineEdit, self.ui.JenkinsCredsIdLineEdit)
            self.setTabOrder(self.ui.JenkinsCredsIdLineEdit, self.ui.PortLlineEdit)
            self.setTabOrder(self.ui.PortLlineEdit, self.ui.DescriptionLineEdit)
            self.setTabOrder(self.ui.DescriptionLineEdit, self.ui.RemoteFsLineEdit)
            self.setTabOrder(self.ui.RemoteFsLineEdit, self.ui.RunPushButton)
            self.setTabOrder(self.ui.RunPushButton, self.ui.QuitPushButton)
            self.setTabOrder(self.ui.QuitPushButton, self.ui.UrlLineEdit)

        elif selected_text == "Get Nodes":
           # Set focus on the URL LineEdit
            self.ui.UrlLineEdit.setFocus()
            self.ui.GetNodesTextEdit.setFocusPolicy(Qt.NoFocus)

            self.ui.stackedWidget.setCurrentIndex(2)
            self.ui.DescriptionLineEdit.hide()

            self.ui.MethodLabel.hide()
            self.ui.MethodComboBox.hide()

            self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
            self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
            self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
            self.setTabOrder(self.ui.ActionComboBox, self.ui.MethodComboBox)
            self.setTabOrder(self.ui.MethodComboBox, self.ui.VmNameLineEdit_2)
            self.setTabOrder(self.ui.VmNameLineEdit_2, self.ui.HostnameOrIpLineEdit_2)
            self.setTabOrder(self.ui.HostnameOrIpLineEdit_2, self.ui.LabelsLineEdit_2)
            self.setTabOrder(self.ui.LabelsLineEdit_2, self.ui.ExecutorsLineEdit_2)
            self.setTabOrder(self.ui.ExecutorsLineEdit_2, self.ui.JVMOptionsLineEdit)
            self.setTabOrder(self.ui.JVMOptionsLineEdit, self.ui.DescriptionLineEdit_2)
            self.setTabOrder(self.ui.DescriptionLineEdit_2, self.ui.RemoteFsLineEdit_2)
            self.setTabOrder(self.ui.RemoteFsLineEdit_2, self.ui.RunPushButton)
            self.setTabOrder(self.ui.RunPushButton, self.ui.QuitPushButton)
            self.setTabOrder(self.ui.QuitPushButton, self.ui.UrlLineEdit)

        elif selected_text.strip() == "Get Node Info":
           # Set focus on the URL LineEdit
            self.ui.UrlLineEdit.setFocus()
            self.ui.GetNodeTextEdit.setFocusPolicy(Qt.NoFocus)

            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.DescriptionLineEdit.hide()

            self.ui.MethodLabel.hide()
            self.ui.MethodComboBox.hide()

            self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
            self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
            self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
            self.setTabOrder(self.ui.ActionComboBox, self.ui.MethodComboBox)
            self.setTabOrder(self.ui.MethodComboBox, self.ui.VmNameLineEdit_3)
            self.setTabOrder(self.ui.VmNameLineEdit_3, self.ui.RunPushButton)
            self.setTabOrder(self.ui.RunPushButton, self.ui.QuitPushButton)
            self.setTabOrder(self.ui.QuitPushButton, self.ui.UrlLineEdit)

        elif selected_text.strip() == "Get Node Config":
           # Set focus on the URL LineEdit
            self.ui.UrlLineEdit.setFocus()
            self.ui.GetNodeTextEdit.setFocusPolicy(Qt.NoFocus)

            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.DescriptionLineEdit.hide()

            self.ui.MethodLabel.hide()
            self.ui.MethodComboBox.hide()

            self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
            self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
            self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
            self.setTabOrder(self.ui.ActionComboBox, self.ui.MethodComboBox)
            self.setTabOrder(self.ui.MethodComboBox, self.ui.VmNameLineEdit_3)
            self.setTabOrder(self.ui.VmNameLineEdit_3, self.ui.RunPushButton)
            self.setTabOrder(self.ui.RunPushButton, self.ui.QuitPushButton)
            self.setTabOrder(self.ui.QuitPushButton, self.ui.UrlLineEdit)

        elif selected_text.strip() == "Node Exists":
           # Set focus on the URL LineEdit
            self.ui.UrlLineEdit.setFocus()
            self.ui.GetNodeTextEdit.setFocusPolicy(Qt.NoFocus)

            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.DescriptionLineEdit.hide()

            self.ui.MethodLabel.hide()
            self.ui.MethodComboBox.hide()

            self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
            self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
            self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
            self.setTabOrder(self.ui.ActionComboBox, self.ui.MethodComboBox)
            self.setTabOrder(self.ui.MethodComboBox, self.ui.VmNameLineEdit_3)
            self.setTabOrder(self.ui.VmNameLineEdit_3, self.ui.RunPushButton)
            self.setTabOrder(self.ui.RunPushButton, self.ui.QuitPushButton)
            self.setTabOrder(self.ui.QuitPushButton, self.ui.UrlLineEdit)

        elif selected_text.strip() == "New Item":
           # Set focus on the URL LineEdit
            self.ui.UrlLineEdit.setFocus()
            self.ui.GetNodeTextEdit.setFocusPolicy(Qt.NoFocus)

            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.DescriptionLineEdit.hide()

            self.ui.MethodLabel.hide()
            self.ui.MethodComboBox.hide()

            self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
            self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
            self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
            self.setTabOrder(self.ui.ActionComboBox, self.ui.MethodComboBox)
            self.setTabOrder(self.ui.MethodComboBox, self.ui.VmNameLineEdit_3)
            self.setTabOrder(self.ui.VmNameLineEdit_3, self.ui.RunPushButton)
            self.setTabOrder(self.ui.RunPushButton, self.ui.QuitPushButton)
            self.setTabOrder(self.ui.QuitPushButton, self.ui.UrlLineEdit)

        elif selected_text.strip() == "Delete":
           # Set focus on the URL LineEdit
            self.ui.UrlLineEdit.setFocus()
            self.ui.GetNodeTextEdit.setFocusPolicy(Qt.NoFocus)

            self.ui.stackedWidget.setCurrentIndex(3)

            self.ui.MethodLabel.hide()
            self.ui.MethodComboBox.hide()

            self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
            self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
            self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
            self.setTabOrder(self.ui.ActionComboBox, self.ui.MethodComboBox)
            self.setTabOrder(self.ui.MethodComboBox, self.ui.VmNameLineEdit_3)
            self.setTabOrder(self.ui.VmNameLineEdit_3, self.ui.RunPushButton)
            self.setTabOrder(self.ui.RunPushButton, self.ui.QuitPushButton)
            self.setTabOrder(self.ui.QuitPushButton, self.ui.UrlLineEdit)

        elif selected_text.strip() == "Disable":
           # Set focus on the URL LineEdit
            self.ui.UrlLineEdit.setFocus()
            self.ui.GetNodeTextEdit.setFocusPolicy(Qt.NoFocus)

            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.DescriptionLineEdit.hide()

            self.ui.MethodLabel.hide()
            self.ui.MethodComboBox.hide()

            self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
            self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
            self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
            self.setTabOrder(self.ui.ActionComboBox, self.ui.MethodComboBox)
            self.setTabOrder(self.ui.MethodComboBox, self.ui.VmNameLineEdit_3)
            self.setTabOrder(self.ui.VmNameLineEdit_3, self.ui.RunPushButton)
            self.setTabOrder(self.ui.RunPushButton, self.ui.QuitPushButton)
            self.setTabOrder(self.ui.QuitPushButton, self.ui.UrlLineEdit)

        elif selected_text.strip() == "Enable":
           # Set focus on the URL LineEdit
            self.ui.UrlLineEdit.setFocus()
            self.ui.GetNodeTextEdit.setFocusPolicy(Qt.NoFocus)

            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.DescriptionLineEdit.hide()

            self.ui.MethodLabel.hide()
            self.ui.MethodComboBox.hide()

            self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
            self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
            self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
            self.setTabOrder(self.ui.ActionComboBox, self.ui.MethodComboBox)
            self.setTabOrder(self.ui.MethodComboBox, self.ui.VmNameLineEdit_3)
            self.setTabOrder(self.ui.VmNameLineEdit_3, self.ui.RunPushButton)
            self.setTabOrder(self.ui.RunPushButton, self.ui.QuitPushButton)
            self.setTabOrder(self.ui.QuitPushButton, self.ui.UrlLineEdit)

        else:
            print("Not a valid comboBox value")

    def handleMethodComboBoxChange(self):

        selected_text = self.ui.MethodComboBox.currentText()

        print(f"selected text: '{selected_text}'")

        if re.match("SSH", selected_text):
           # Set focus on the URL LineEdit
            self.ui.UrlLineEdit.setFocus()

            self.ui.stackedWidget.setCurrentIndex(0)

            self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
            self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
            self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
            self.setTabOrder(self.ui.ActionComboBox, self.ui.MethodComboBox)
            self.setTabOrder(self.ui.MethodComboBox, self.ui.VmNameLineEdit)
            self.setTabOrder(self.ui.VmNameLineEdit, self.ui.HostnameOrIpLineEdit)
            self.setTabOrder(self.ui.HostnameOrIpLineEdit, self.ui.LabelsLineEdit)
            self.setTabOrder(self.ui.LabelsLineEdit, self.ui.ExecutorsLineEdit)
            self.setTabOrder(self.ui.ExecutorsLineEdit, self.ui.JenkinsCredsIdLineEdit)
            self.setTabOrder(self.ui.JenkinsCredsIdLineEdit, self.ui.PortLlineEdit)
            self.setTabOrder(self.ui.PortLlineEdit, self.ui.DescriptionLineEdit)
            self.setTabOrder(self.ui.DescriptionLineEdit, self.ui.RemoteFsLineEdit)
            self.setTabOrder(self.ui.RemoteFsLineEdit, self.ui.RunPushButton)
            self.setTabOrder(self.ui.RunPushButton, self.ui.QuitPushButton)
            self.setTabOrder(self.ui.QuitPushButton, self.ui.UrlLineEdit)

        elif re.match("JNLP", selected_text):
           # Set focus on the URL LineEdit
            self.ui.UrlLineEdit.setFocus()

            self.ui.stackedWidget.setCurrentIndex(1)

            self.setTabOrder(self.ui.UrlLineEdit, self.ui.UsernameLineEdit)
            self.setTabOrder(self.ui.UsernameLineEdit, self.ui.tokenLineEdit)
            self.setTabOrder(self.ui.tokenLineEdit, self.ui.ActionComboBox)
            self.setTabOrder(self.ui.ActionComboBox, self.ui.MethodComboBox)
            self.setTabOrder(self.ui.MethodComboBox, self.ui.VmNameLineEdit_2)
            self.setTabOrder(self.ui.VmNameLineEdit_2, self.ui.HostnameOrIpLineEdit_2)
            self.setTabOrder(self.ui.HostnameOrIpLineEdit_2, self.ui.LabelsLineEdit_2)
            self.setTabOrder(self.ui.LabelsLineEdit_2, self.ui.ExecutorsLineEdit_2)
            self.setTabOrder(self.ui.ExecutorsLineEdit_2, self.ui.JVMOptionsLineEdit)
            self.setTabOrder(self.ui.JVMOptionsLineEdit, self.ui.DescriptionLineEdit_2)
            self.setTabOrder(self.ui.DescriptionLineEdit_2, self.ui.RemoteFsLineEdit_2)
            self.setTabOrder(self.ui.RemoteFsLineEdit_2, self.ui.RunPushButton)
            self.setTabOrder(self.ui.RunPushButton, self.ui.QuitPushButton)
            self.setTabOrder(self.ui.QuitPushButton, self.ui.UrlLineEdit)


        else:
            print("not a valid comboBox value")


if __name__ == "__main__":
    __package__ = "jenkinsTools.ux"
    app = QApplication(sys.argv)
    dialog = nodesDialog()
    dialog.show()
    sys.exit(app.exec())

