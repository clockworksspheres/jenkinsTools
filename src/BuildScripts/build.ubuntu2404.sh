#!/bin/bash

# highly modified version of:
# https://www.pythonguis.com/tutorials/packaging-pyside6-applications-pyinstaller-macos-dmg/
# amoung others... including
# https://pyinstaller.org/en/stable/

pushd ..

#if doesn't the packenv directory doesn't exist...
directory="./packenv"
actfile="./packenv/bin/activate"
if [ ! -d "$directory" ]  || [ ! -f "$actfile" ] ; then
   python3 -m venv packenv
   source packenv/bin/activate

   pip install --upgrade pip
   pip install python-jenkins
   pip install PyInstaller
   pip install requests
   pip install pytest
else
   source packenv/bin/activate
fi

cp BuildScripts/build.ubuntu2404.NodeTool.spec jenkinsTools
cp BuildScripts/build.ubuntu2404.PipelineTool.spec jenkinsTools
cp BuildScripts/build.ubuntu2404.AddSshKeyTool.spec jenkinsTools

pushd jenkinsTools

pyinstaller --clean -y build.ubuntu2404.NodeTool.spec
pyinstaller -y build.ubuntu2404.NodeTool.spec

pyinstaller --clean -y build.ubuntu2404.PipelineTool.spec
pyinstaller -y build.ubuntu2404.PipelineTool.spec

cp JenkinsTools/AddSshKeyCredential.py .
pyinstaller --clean -y build.ubuntu2404.AddSshKeyTool.spec
pyinstaller -y build.ubuntu2404.AddSshKeyTool.spec

rm build.ubuntu2404.NodeTool.spec
rm build.ubuntu2404.PipelineTool.spec
rm build.macos.AddSshKeyTool.spec
rm AddSshKeyCredential.py

popd
popd


