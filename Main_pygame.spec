# -*- mode: python -*-

block_cipher = None


a = Analysis(['Main_pygame.py'],
             pathex=['C:\\Users\\Ilya\\Desktop\\UIRS 0.3.1n\\UIRS 0.2'],
             binaries=[],
             datas=[('.\\Add\\*.jpg', 'Add'), ('.\\Add\\*.png', 'Add'), ('.\\Add\\*.txt', 'Add'), ('.\\Add\\*.mp3', 'Add')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Main_pygame',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='12345.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Main_pygame')
