#!/usr/bin/env python3

import sys
import argparse

from PySide6.QtWidgets import QApplication


if __name__=="__main__":

    from JenkinsTools.AddSshKeyCredential import parseSshKeyWrangling

    parseSshKeyWrangling()

