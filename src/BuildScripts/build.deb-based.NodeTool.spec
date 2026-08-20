# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['jenkinsNodeTool.py'],
    pathex=['.', 'lib', 'ui', 'JenkinsTools'],
    binaries=[],
    datas=[],
    hiddenimports=[
        'JenkinsTools',
    ], 
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=True,        # <-- Faster import time
    optimize=1,            # <-- Bytecode optimization
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    name='jenkinsNodeTool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=False,             # <-- No UPX = faster load
    runtime_tmpdir="/tmp",   # <-- Uses system temp (fastest)
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onefile=True,          # <-- You requested onefile
    noarchive=True,
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
