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
   pip install pylint
   pip install astroid
   pip install python-jenkins
   pip install PyInstaller
   pip install requests
   pip install pytest
else
   source packenv/bin/activate
fi

cp BuildScripts/build.deb-based.NodeTool.spec jenkinsTools
cp BuildScripts/build.deb-based.PipelineTool.spec jenkinsTools
cp BuildScripts/build.deb-based.AddSshKeyTool.spec jenkinsTools

pushd jenkinsTools

pyinstaller --clean -y build.deb-based.NodeTool.spec
pyinstaller -y build.deb-based.NodeTool.spec

pyinstaller --clean -y build.deb-based.PipelineTool.spec
pyinstaller -y build.deb-based.PipelineTool.spec

cp JenkinsTools/AddSshKeyCredential.py .
pyinstaller --clean -y build.deb-based.AddSshKeyTool.spec
pyinstaller -y build.deb-based.AddSshKeyTool.spec

rm build.deb-based.NodeTool.spec
rm build.deb-based.PipelineTool.spec
rm build.macos.AddSshKeyTool.spec
rm AddSshKeyCredential.py

popd
popd


