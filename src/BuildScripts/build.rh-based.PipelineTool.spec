# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['jenkinsPipelineTool.py'],
    pathex=['.', 'lib', 'ui', 'JenkinsTools'],
    binaries=[],
    datas=[],
    hiddenimports=[],
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
    a.binaries,
    a.datas,
    [],
    name='jenkinsPipelineTool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,             # <-- No UPX = faster load
    upx_exclude=[],
    runtime_tmpdir='/tmp',   # <-- Uses system temp (fastest)
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onefile=True,          # <-- You requested onefile
    noarchive=True,
)
