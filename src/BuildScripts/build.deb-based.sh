#!/bin/bash

# highly modified version of:
# https://www.pythonguis.com/tutorials/packaging-pyside6-applications-pyinstaller-macos-dmg/
# amoung others... including
# https://pyinstaller.org/en/stable/

echo "----------===== ### =====----------"
echo " ### starting Debian based build ###"

pushd ..

#if doesn't the packenv directory doesn't exist...

directory="./projEnv"
actfile="$directory/bin/activate"
if [ ! -d "$directory" ]  || [ ! -f "$actfile" ] ; then

   sudo apt install python-is-python3

   python3 -m venv projEnv
   source $actfile

   pip install -r requirements.txt

else
   source $actfile
fi

cp BuildScripts/build.deb-based.NodeTool.spec jenkinsTools
cp BuildScripts/build.deb-based.PipelineTool.spec jenkinsTools
cp BuildScripts/build.deb-based.SshKeyWrangling.spec jenkinsTools
cp BuildScripts/build.deb-based.ToolsGui.spec jenkinsTools

pushd jenkinsTools

pyinstaller --clean -y build.deb-based.NodeTool.spec
pyinstaller -y build.deb-based.NodeTool.spec

pyinstaller --clean -y build.deb-based.PipelineTool.spec
pyinstaller -y build.deb-based.PipelineTool.spec

pyinstaller --clean -y build.deb-based.SshKeyWrangling.spec
pyinstaller -y build.deb-based.SshKeyWrangling.spec

pyinstaller --clean -y build.deb-based.ToolsGui.spec
pyinstaller -y build.deb-based.ToolsGui.spec


rm build.deb-based.NodeTool.spec
rm build.deb-based.PipelineTool.spec
rm build.deb-based.SshKeyWrangling.spec
rm build.deb-based.ToolsGui.spec

popd
popd


