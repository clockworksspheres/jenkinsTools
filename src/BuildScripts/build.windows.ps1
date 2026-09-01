
# https://pyinstaller.org/en/stable/

# before script is run:
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
# powershell -File ".\build.windows.ps1"

#####
# If used in Jenkins, in the Jenkins node, under ssh, advanced - 
# put the "Set-ExecutionPolicy" line above (with a semi-colon at 
# the end) in the "Prefix Start Agent Command" field.

pushd ..

$directory = ".\projEnv"
$actfile = ".\projEnv\Scripts\Activate.ps1"
if (!(Test-Path -Path $directory -PathType Container)) {
   #if (!(Test-Path -Path ".\packenv" -PathType Container)) {
   
   python -m venv $directory

   .\projEnv\Scripts\Activate.ps1

   pip install -r requirements.txt
} else {
   powershell -File $actfile
}

#####
# Do every time, to make sure everyone knows source of E.ico icon, so 
# proper license can be found
# cp .\resources\icons\Barkerbaggies-Bag-O-Tiles-E.ico .\resources\icons\E.ico

cp BuildScripts/build.windows11.ToolsGui.spec jenkinsTools
cp BuildScripts/build.windows11.NodeTool.spec jenkinsTools
cp BuildScripts/build.windows11.PipelineTool.spec jenkinsTools
cp BuildScripts/build.windows11.SshKeyWrangling.spec jenkinsTools

pushd jenkinsTools

pyinstaller --clean -y build.windows11.ToolsGui.spec
pyinstaller -y build.windows11.ToolsGui.spec

pyinstaller --clean -y build.windows11.NodeTool.spec
pyinstaller -y build.windows11.NodeTool.spec

pyinstaller --clean -y build.windows11.PipelineTool.spec
pyinstaller -y build.windows11.PipelineTool.spec

pyinstaller --clean -y build.windows11.SshKeyWrangling.spec
pyinstaller -y build.windows11.SshKeyWrangling.spec

rm build.windows11.ToolsGui.spec
rm build.windows11.NodeTool.spec
rm build.windows11.PipelineTool.spec
rm build.windows11.SshKeyWrangling.spec

popd
popd


