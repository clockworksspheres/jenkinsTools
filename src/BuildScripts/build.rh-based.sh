#!/bin/bash

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
cp BuildScripts/build.rh-based.SshKeyWrangling.spec jenkinsTools
cp BuildScripts/build.rh-based.ToolsGui.spec jenkinsTools

pushd jenkinsTools

pyinstaller --clean -y build.rh-based.NodeTool.spec
pyinstaller -y build.rh-based.NodeTool.spec

pyinstaller --clean -y build.rh-based.PipelineTool.spec
pyinstaller -y build.rh-based.PipelineTool.spec

pyinstaller --clean -y build.rh-based.SshKeyWrangling.spec
pyinstaller -y build.rh-based.SshKeyWrangling.spec

pyinstaller --clean -y build.rh-based.ToolsGui.spec
pyinstaller -y build.rh-based.ToolsGui.spec

rm build.rh-based.NodeTool.spec
rm build.rh-based.PipelineTool.spec
rm build.rh-based.SshKeyWrangling.spec
rm build.rh-based.ToolsGui.spec

popd
popd


