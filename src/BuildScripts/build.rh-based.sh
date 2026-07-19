#!/bin/bash

# highly modified version of:
# https://www.pythonguis.com/tutorials/packaging-pyside6-applications-pyinstaller-macos-dmg/
# amoung others... including
# https://pyinstaller.org/en/stable/

echo "----------===== ### =====----------"
echo " ### starting RHEL based build ###"

pushd ..

#if doesn't the packenv directory doesn't exist...

directory="./projEnv"
actfile="$directory/bin/activate"
if [ ! -d "$directory" ]  || [ ! -f "$actfile" ] ; then

   python3 -m venv projEnv
   source $actfile

   pip install -r requirements.txt

else
   source $actfile
fi

cp BuildScripts/build.rh-based.NodeTool.spec jenkinsTools
cp BuildScripts/build.rh-based.PipelineTool.spec jenkinsTools
cp BuildScripts/build.rh-based.AddSshKeyTool.spec jenkinsTools

pushd jenkinsTools

pyinstaller --clean -y build.rh-based.NodeTool.spec
pyinstaller -y build.rh-based.NodeTool.spec

pyinstaller --clean -y build.rh-based.PipelineTool.spec
pyinstaller -y build.rh-based.PipelineTool.spec

cp JenkinsTools/AddSshKeyCredential.py .
pyinstaller --clean -y build.rh-based.AddSshKeyTool.spec
pyinstaller -y build.rh-based.AddSshKeyTool.spec

rm build.rh-based.NodeTool.spec
rm build.rh-based.PipelineTool.spec
rm build.rh-based.AddSshKeyTool.spec
rm AddSshKeyCredential.py

popd
popd


