# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from PyInstaller.utils.hooks import collect_submodules, collect_data_files
from PyInstaller.utils.hooks import collect_all

block_cipher = None

# 收集必要的子模块和数据文件
readchar_hidden_imports = collect_submodules('readchar')
inquirer_hidden_imports = collect_submodules('inquirer')
ipython_hidden_imports = collect_submodules('IPython')
pymobiledevice3_hidden_imports = collect_submodules('pymobiledevice3')
readchar_datas = collect_data_files('readchar')
inquirer_datas = collect_data_files('inquirer')
pymobiledevice3_datas = collect_data_files('pymobiledevice3')
ipython_datas = collect_data_files('IPython')

a = Analysis(
    ['src/main.py'],
    pathex=[os.path.dirname(os.path.abspath(sys.argv[0]))],
    binaries=[],
    datas=[
        ('src/templates', 'templates'),
        ('images', 'images'),
        ('D:\\geoport-4.0.2\\GeoPort\\venv\\lib\\site-packages\\pytun_pmd3\\wintun\\bin\\amd64\\wintun.dll', 'pytun_pmd3/wintun/bin/amd64'),
        ('D:\\geoport-4.0.2\\GeoPort\\venv\\lib\\site-packages\\readchar-4.2.1.dist-info', 'readchar-4.2.1.dist-info'),
        ('D:\\geoport-4.0.2\\GeoPort\\venv\\lib\\site-packages\\inquirer3-0.6.1.dist-info', 'inquirer3-0.6.1.dist-info'),
        ('D:\\geoport-4.0.2\\GeoPort\\venv\\lib\\site-packages\\pymobiledevice3-4.17.2.dist-info', 'pymobiledevice3-4.17.2.dist-info'),
    ] + readchar_datas + inquirer_datas + pymobiledevice3_datas + ipython_datas,
    hiddenimports=[
        'engineio.async_drivers.threading',
        'flask',
        'psutil',
        'pycountry',
        'pyuac',
        'pymobiledevice3.usbmux',
        'pymobiledevice3.lockdown',
        'pymobiledevice3.services.amfi',
        'pymobiledevice3.services.dvt.dvt_secure_socket_proxy',
        'pymobiledevice3.services.dvt.instruments.location_simulation',
        'pymobiledevice3.lockdown_service_provider',
        'pymobiledevice3.service_connection',
        'readchar.readchar',
        'readchar.readkey',
        'inquirer3',
        'inquirer3.render.console',
        'inquirer3.render.console.base',
        'inquirer3.events',
        'IPython',
        'IPython.core',
        'IPython.utils',
        'IPython.terminal',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'Tkinter', 'PIL', 'notebook', 'matplotlib'],  # 移除了 IPython
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

# 添加核心子模块
a.hiddenimports.extend(readchar_hidden_imports)
a.hiddenimports.extend(inquirer_hidden_imports)
a.hiddenimports.extend(ipython_hidden_imports)
a.hiddenimports.extend(pymobiledevice3_hidden_imports)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='GeoPort',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
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
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='GeoPort'
)