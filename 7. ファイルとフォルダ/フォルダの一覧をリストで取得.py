# ****** フォルダの一覧をリストで取得: ******
# os.listdir(path='.')

import os

"""
・
└─testdir
    ├─dir1
    ├─dir2
    ├─file1
    ├─file2.txt
    └─file3.jpg
"""

os.makedirs('testdir', exist_ok=True)
os.makedirs('testdir/dir1', exist_ok=True)
os.makedirs('testdir/dir2', exist_ok=True)
with open('testdir/file1', 'w'):
    pass
with open('testdir/file2.txt', 'w'):
    pass
with open('testdir/file3.jpg', 'w'):
    pass

# === ファイル名とディレクトリ名の両方の一覧を取得 ===

"""
os.listdir() をそのまま使うと、
ファイル名とディレクトリ名の両方のリストが返る
"""

path = "./testdir"

files = os.listdir(path)
print(type(files))  # <class 'list'>
print(files)  # ['dir1', 'dir2', 'file1', 'file2.txt', 'file3.jpg']

# === ファイル名のみの一覧を取得 ===

"""
・ファイル名のみの一覧を取得したい場合は、
  path がファイルかどうかを判定する os.path.isfile() とリスト内包表記を用いる
・os.path.isfile() にファイル名だけ渡すとうまくいかないので、
  以下のように os.path.isfile(os.path.join(path, f)) としてフルパスにして渡す
"""

files = os.listdir(path)
files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
print(files_file)  # ['file1', 'file2.txt', 'file3.jpg']

# === ディレクトリ名のみの一覧を取得 ===

"""
ディレクトリ名のみの一覧を取得したい場合は、同じように、os.path.isdir() を使う
"""

files = os.listdir(path)
files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
print(files_dir)  # ['dir1', 'dir2']

# =====================

import shutil

shutil.rmtree('testdir')
