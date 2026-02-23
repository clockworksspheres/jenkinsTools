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
   python -m venv packenv
   source packenv/bin/activate

   pip install --upgrade pip
   pip install python-jenkins
   pip install PyInstaller
else
   source packenv/bin/activate
fi

cp BuildScripts/build.macos.NodeTool.spec jenkinsTools
cp BuildScripts/build.macos.PipelineTool.spec jenkinsTools

pushd jenkinsTools

pyinstaller --clean -y build.macos.NodeTool.spec
pyinstaller -y build.macos.NodeTool.spec

pyinstaller --clean -y build.macos.PipelineTool.spec
pyinstaller -y build.macos.PipelineTool.spec

rm build.macos.NodeTool.spec
rm build.macos.PipelineTool.spec

popd
popd


