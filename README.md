# jenkinsTools

Command line tools for interfacing with Jenkins

Relies on the python-jenkins library to interface with a Jenkins server.

Command line tools to:
 * manage nodes
 * work with a simple pipeline
 * add previously created ssh credential to Jenkins.

Command line tools:

JenkinsNodeTool.py
Node actions: add, update, delete, enable, disable, get-nodes, get-node-info, get-node-config 

JenkinsPipelineTool.py
Pipeline actions:  Create, run, check, get-config, set-config

jenkinsSshKeyWrangling.py
Add an existing SSH private key as a Jenkins credential on a Jenkins server

Command line tools used with the -g or -gui switch will run a graphical version of the tool.

The jenkinsToolsGUI.py is a small meta wrapper around all the GUI's.

-----

A [clockworksspheres](https://clockworksspheres.github.io/) project.

Can work in hand with the [clockworksspheres/mvm](https://clockworksspheres/mvm.git) project to manage test VM's for testing the cross platform nature of the tools

