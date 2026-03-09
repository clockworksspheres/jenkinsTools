# FAST-STARTUP ONEFILE SPEC

a = Analysis(
    ['AddSshKeyCredential.py'],
    pathex=['.'],
    binaries=[],
    datas=[],
    hiddenimports=[ ],
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
    name='jenkinsAddSshKeyTool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=False,             # <-- No UPX = faster load
    upx_exclude=[],
    runtime_tmpdir=None,   # <-- Uses system temp (fastest)
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onefile=True,          # <-- You requested onefile
    noarchive=True,
)

