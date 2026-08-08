import sys
import argparse

from PySide6.QtWidgets import QApplication


if __name__=="__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-g", "--gui", action='store_true', help="User's token to access the Jenkins server")
    parser.add_argument("-s", "--ssh-creds", action='store_true', help="User's token to access the Jenkins server")
    parser.add_argument("-n", "--nodes", action='store_true', help="User's token to access the Jenkins server")
    parser.add_argument("-p", "--pipelines", action='store_true', help="User's token to access the Jenkins server")

    args = parser.parse_args()

    if len(sys.argv) == 1 or args.gui:
            
        from ux.main import JenkinsToolsUi

        app = QApplication(sys.argv)
        widget = JenkinsToolsUi()
        widget.show()
        sys.exit(app.exec())

    elif args.ssh_creds:
        from ux.sshCredsMain import SshCredsDialog
        app = QApplication(sys.argv)
        dlg = SshCredsDialog()
        dlg.show()
        sys.exit(app.exec()) 

    elif args.nodes:
        from ux.nodesMain import nodesDialog
        app = QApplication(sys.argv)
        dlg = nodesDialog()
        dlg.show()
        sys.exit(app.exec()) 

    elif args.pipelines:
        from ux.pipelinesMain import pipelinesDialog
        app = QApplication(sys.argv)
        dlg = pipelinesDialog()
        dlg.show()
        sys.exit(app.exec()) 


