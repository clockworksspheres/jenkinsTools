#!/usr/bin/env python3

import sys
import argparse

from PySide6.QtWidgets import QApplication


if __name__=="__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-g", "--gui", action='store_true', help="Start the main GUI")
    parser.add_argument("-s", "--ssh-creds", action='store_true', help="Start the SSH creds wrangling GUI")

    args = parser.parse_args()

    if len(sys.argv) == 1 or args.gui or args.ssh_creds:
            
        from ux.sshCredsMain import SshCredsDialog
        app = QApplication(sys.argv)
        dlg = SshCredsDialog()
        dlg.show()
        sys.exit(app.exec())
    else:
        parser.print_help()
        sys.exit()

