#!/bin/bash

# highly modified version of:
# https://www.pythonguis.com/tutorials/packaging-pyside6-applications-pyinstaller-macos-dmg/
# amoung others... including
# https://pyinstaller.org/en/stable/

pushd ..

#if doesn't the packenv directory doesn't exist...
directory="./projEnv"
actfile="$directory/bin/activate"
if [ ! -d "$directory" ]  || [ ! -f "$actfile" ] ; then
   python3 -m venv $directory
   source $actfile

   pip install -r requirements.txt

else
   source $actfile
fi

cp BuildScripts/build.macos.ToolsGui.spec jenkinsTools
cp BuildScripts/build.macos.NodeTool.spec jenkinsTools
cp BuildScripts/build.macos.PipelineTool.spec jenkinsTools
cp BuildScripts/build.macos.SshKeyWrangling.spec jenkinsTools

pushd jenkinsTools

pyinstaller --clean -y build.macos.ToolsGui.spec
pyinstaller -y build.macos.ToolsGui.spec

pyinstaller --clean -y build.macos.NodeTool.spec
pyinstaller -y build.macos.NodeTool.spec

pyinstaller --clean -y build.macos.PipelineTool.spec
pyinstaller -y build.macos.PipelineTool.spec

pyinstaller --clean -y build.macos.SshKeyWrangling.spec
pyinstaller -y build.macos.SshKeyWrangling.spec

rm build.macos.ToolsGui.spec
rm build.macos.NodeTool.spec
rm build.macos.PipelineTool.spec
rm build.macos.SshKeyWrangling.spec
rm AddSshKeyCredential.py

popd
popd


