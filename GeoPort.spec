# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.utils.hooks import collect_all

block_cipher = None

# 收集 readchar 的所有子模块
readchar_hidden_imports = collect_submodules('readchar')
# 收集 inquirer 的所有子模块
inquirer_hidden_imports = collect_submodules('inquirer')

a = Analysis(
    ['src/main.py'],
    pathex=[os.path.dirname(os.path.abspath(sys.argv[0]))],
    binaries=[],  # Clear the binaries list. We'll use datas.
    datas=[
        ('src/templates', 'templates'),
        ('images', 'images'),
        ('D:\\geoport-4.0.2\\GeoPort\\venv\\lib\\site-packages\\readchar-4.2.1.dist-info', 'readchar-4.2.1.dist-info'),
        ('D:\\geoport-4.0.2\\GeoPort\\venv\\lib\\site-packages\\zeroconf-0.38.0.dist-info', 'zeroconf-0.38.0.dist-info'),
        # Correctly include the 64-bit wintun.dll using datas
        ('D:\\geoport-4.0.2\\GeoPort\\venv\\lib\\site-packages\\pytun_pmd3\\wintun\\bin\\amd64\\wintun.dll', 'pytun_pmd3/wintun/bin/amd64'),
        # 添加 pyimg4 的元数据
        ('D:\\geoport-4.0.2\\GeoPort\\venv\\lib\\site-packages\\pyimg4-0.8.6.dist-info', 'pyimg4-0.8.6.dist-info'),
    ],
    hiddenimports=[],  # No need for pytun_pmd3.wintun here if datas is correct
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

# 添加 readchar 的子模块
a.hiddenimports.extend([*readchar_hidden_imports])
# 添加 inquirer 的子模块
a.hiddenimports.extend([*inquirer_hidden_imports])

#  显式添加 zeroconf 的子模块
a.hiddenimports.extend([
    'zeroconf',
    'zeroconf._core',
    'zeroconf._exceptions',
    'zeroconf._impl',
    'zeroconf._services',
    'zeroconf._utils',
    'zeroconf._utils.ipaddress',
    'zeroconf.asyncio',
    'zeroconf.compat',
    'zeroconf.const',
    'zeroconf.dns',
    'zeroconf.dns.dns',
    'zeroconf.dns.base',
    'zeroconf.dns.types',
    'zeroconf.dns.compression',
    'zeroconf.dns.merger',
    'zeroconf.dns.record',
    'zeroconf.dns.resolver',
    'zeroconf.aio',
    'zeroconf.http',
    'zeroconf.interfaces',
    'zeroconf.lineprinter',
    'zeroconf.printing',
    'zeroconf.server',
    'zeroconf.utils._compat_ipaddress',
    'zeroconf.utils._compat_enum',
    'zeroconf._typing'
])

a.hiddenimports.extend([
    'engineio.async_drivers.threading',
    'flask',
    'psutil',
    'pycountry',
    'pyuac',
    'pymobiledevice3',
    'pymobiledevice3.usbmux',
    'pymobiledevice3.lockdown',
    'pymobiledevice3.services.amfi',
    'pymobiledevice3.services.dvt.dvt_secure_socket_proxy',
    'pymobiledevice3.services.dvt.instruments.location_simulation',
    'pymobiledevice3.remote.remote_service_discovery',
    'pymobiledevice3.remote.tunnel_service',
    'pymobiledevice3.remote.utils',
    'pymobiledevice3.osu.os_utils',
    'pymobiledevice3.bonjour',
    'pymobiledevice3.pair_records',
    'pycountry.db',
    'importlib_metadata',
    'importlib.abc',
    'importlib.machinery',
    'importlib.metadata._itertools',
    'importlib.metadata._functools',
    'importlib.metadata._collections',
    'importlib.metadata._meta',
])

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,  # Keep this, even if empty
    a.zipfiles,
    a.datas,
    [],
    name='Fake_Location_google_V2.17',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir="_MEIPASS2",
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='images/logo.ico'
)