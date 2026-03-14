# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['jenkinsNodeTool.py'],
    pathex=['.', 'lib', 'ui'],
    binaries=[],
    datas=[],
    hiddenimports=[ 
        'JenkinsTools.AddJenkinsNode.py',
        'JenkinsTools.AddSshKeyCredential.py',
        'JenkinsTools.CheckJenkinsPipelineRun.py',
        'JenkinsTools.ConfigJob.py',
        'JenkinsTools.CreateJenkinsPipeline.py',
        'JenkinsTools.NodeManage_basic.py',
        'JenkinsTools.NodeManage_name.py',
        'JenkinsTools.NodeManage.py',
        'JenkinsTools.NodeStatus_basic.py',
        'JenkinsTools.NodeStatus.py',
        'JenkinsTools.RunJenkinsPipeline.py',
        'JenkinsTools.update_node.py',
    ], 
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='jenkinsNodeTool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='jenkinsNodeTool',
)
