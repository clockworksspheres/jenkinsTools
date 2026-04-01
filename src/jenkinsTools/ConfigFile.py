import os
import sys
import ConfigParser

from pathlib import Path



class ConfigFile():
    """
    Class to manage a config file for the project.
    """    


    def __init__(self):
        """
        Initialize class variables
        """
        self.jenkinsServer = ""
        self.jenkinsUser = ""
        self.jenkinsToken = ""
        self.filename = "config.py"
        self.getDefaultConfigPath()
        self.permissions = 0o600
        self.userHome = str(getUserHome())

    def saveConfig(self):
        """
        """
        with open(self.configFile "w") as f:
            f.write(f"JENKINS_SERVER={self.jenkinsServer}")
            f.write(f"JENKINS_USER={self.jenkinsUser}")
            f.write(f"JENKINS_TOKEN={self.jenkinsToken}")

    def loadConfig(self):
        """
        """
        pass
        

    def useConfig(self):
        """
        """
        pass

    def getUserHome(self):
        """
        """
        # Path.home is a cross platform way to get the user's home
        self.userHome = str(Path.home()).strip()

        return self.userHome

    def getDefaultConfigPath(self):
        """
        """
        userHome = self.getUserHome()

        if sys.platform.lower().startswith("win"):
            self.configFilePath = self.userHome + r'\\.local\\config\\jenkinsTools'
            self.configFile = self.configFilePath + r'\\' +  self.filename
        else:
            self.configFilePath = self.userHome + "/.local/config/jenkinsTools"
            self.configFile = self.configFilePath + "/" + self.filename

        print(str(self.configFile))

    def createConfig(self):
        """
        """
        Path(self.configFilePath).mkdir(parents=True, exist_ok=True)
        Path(self.configFile).touch() 
        configFile = Path(self.configFile)
        configFile.chmod(0o600)

    def getJenkinsServer(self):
        """
        """
        return self.jenkinsServer

    def setJenkinsServer(self, server=""):
        """
        """
        if server and isinstance(server, str):
            self.jenkinsServer = server

    def getJenkinsUser(self):
        """
        """
        return self.jenkinsUser

    def setJenkinsUser(self, user=""):
        """
        """
        if user and isinstance(user, str):
            self.jenkinsUser = user

    def getJenkinsToken(self):
        """
        """
        return ""

    def setJenkinsServer(self, token=""):
        """
        """
        if token and isinstance(token, str):
            self.jenkinsToken = token

    def commitCursor(self):
        """
        Write the project variables to the config file.
        """
        # import variable from the config file

        # overwrite variables with class variables that have been set

        # write the file



