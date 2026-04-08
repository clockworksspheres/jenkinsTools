
# /usr/bin/find . -iname "*.pyc" -print -exec rm {} \;
# /usr/bin/find . -iname "__pycache__" -print -exec rm -rf {} \;

Get-ChildItem -Path . -Recurse -Directory -Filter '*.pyc' | Remove-Item -Recurse -Force
Get-ChildItem -Path . -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force
