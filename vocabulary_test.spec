# -*- mode: python -*-

block_cipher = None


a = Analysis(['vocabulary_test.py'],
             pathex=['/Users/Arina/Documents/git_projects/vocabulary-test'],
             binaries=[],
             datas=[('/Users/Arina/Documents/git_projects/vocabulary-test/vocabulary.txt', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='vocabulary_test',
          debug=True,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='vocabulary_test')
app = BUNDLE(coll,
             name='vocabulary_test.app',
             icon=None,
             bundle_identifier=None)
