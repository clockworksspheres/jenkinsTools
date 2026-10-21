#!/usr/bin/env python3

import sys
import argparse

from PySide6.QtWidgets import QApplication


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-g", "--gui", action='store_true', help="Start the main GUI")
    parser.add_argument("-s", "--ssh-creds", action='store_true', help="Start the SSH creds wrangling GUI")
    parser.add_argument("-n", "--nodes", action='store_true', help="Start the jenkins nodes GUI")
    parser.add_argument("-p", "--pipelines", action='store_true', help="start the jenkins pippelines GUI")

    args = parser.parse_args()

    if len(sys.argv) == 1 or args.gui:

        from jenkinsTools.ux.main import JenkinsToolsUi

        app = QApplication(sys.argv)
        widget = JenkinsToolsUi()
        widget.show()
        sys.exit(app.exec())

    elif args.ssh_creds:
        from jenkinsTools.ux.sshCredsMain import SshCredsDialog
        app = QApplication(sys.argv)
        dlg = SshCredsDialog()
        dlg.show()
        sys.exit(app.exec()) 

    elif args.nodes:
        from jenkinsTools.ux.nodesMain import nodesDialog
        app = QApplication(sys.argv)
        dlg = nodesDialog()
        dlg.show()
        sys.exit(app.exec()) 

    elif args.pipelines:
        from jenkinsTools.ux.pipelinesMain import pipelinesDialog
        app = QApplication(sys.argv)
        dlg = pipelinesDialog()
        dlg.show()
        sys.exit(app.exec()) 


if __name__=="__main__":
    main()
