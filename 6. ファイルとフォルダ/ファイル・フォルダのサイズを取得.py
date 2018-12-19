# ****** ファイル・フォルダの存在確認 ******

import os

filepath = './data/temp/dir/file.txt'
dirpath = './data/temp/dir'

source: os_path_exists_isfile_isdir.py

パス文字列の操作については以下の記事を参照。

関連記事: Pythonでパス文字列からファイル名・フォルダ名・拡張子を取得、結合

ファイルまたはディレクトリ（フォルダ）の存在確認: os.path.exists()

パスが存在しているかどうかを確認するにはos.path.exists()を使う。

ファイルでもディレクトリでも、存在していればTrue、存在していなければFalseを返す。

print(os.path.exists(filepath))
# True

print(os.path.exists(dirpath))
# True

source: os_path_exists_isfile_isdir.py
ファイルの存在確認: os.path.isfile()

パスが存在しているファイルであるかどうかを確認するにはos.path.isfile()を使う。

ディレクトリ（フォルダ）を示すパスの場合は存在していてもFalseを返す。

print(os.path.isfile(filepath))
# True

print(os.path.isfile(dirpath))
# False

source: os_path_exists_isfile_isdir.py

拡張子のないファイル名（Makefileなど）もファイルとして認識して正しく判定してくれる。
ディレクトリ（フォルダ）の存在確認: os.path.isdir()

パスが存在しているディレクトリ（フォルダ）であるかどうかを確認するにはos.path.isdir()を使う。

ファイルを示すパスの場合は存在していてもFalseを返す。

print(os.path.isdir(filepath))
# False

print(os.path.isdir(dirpath))
# True

source: os_path_exists_isfile_isdir.py

パス文字列の末尾に区切り文字がついていてもOK。

dirpath_with_sep = './data/temp/dir/'

print(os.path.isfile(dirpath_with_sep))
# False

print(os.path.isdir(dirpath_with_sep))
# True


# ****** ファイルのサイズ取得: ******
# os.path.getsize(path)

"""引数にサイズを取得したいファイルのパスを与える"""

import os

file_path = os.path.basename(__file__)

print(os.path.getsize(file_path))

# ****** フォルダ・ファイルのサイズ取得用関数: ******
# os.DirEntry インスタンス(イテレータ) = os.scandir(path='.')
# os.DirEntry.stat(*, follow_symlinks=True)
# os.DirEntry.is_dir(*, follow_symlinks=True)
# os.DirEntry.is_file(*, follow_symlinks=True)

def get_size(path=os.path.dirname(__file__)):
    import os

    def get_dir_size(path):
        total = 0
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    total += entry.stat().st_size
                elif entry.is_dir():
                    total += get_dir_size(entry.path)
        return total

    name = os.path.basename(path)
    if os.path.isfile(path):
        size = os.path.getsize(path)
    elif os.path.isdir(path):
        size = get_dir_size(path)
    print(name, ': ', size, sep='')

get_size()
get_size(file_path)

"""
・os.scandir() で得られる os.DirEntry オブジェクトに対して、
  is_file(), is_dir() メソッドでファイルかディレクトリかを判定
・ファイルの場合は stat_result オブジェクト(stat() でアクセス)の st_size 属性でサイズを取得、
  ディレクトリの場合はこの関数を再帰的に呼び出し、
  すべてのサイズを加算し合計サイズを返している

・デフォルトでは、is_file() はファイルへのシンボリックリンク、
  is_dir() はディレクトリへのシンボリックリンクに対しても True を返す
・シンボリックリンクを無視したい場合は、
  is_file(), is_dir() の引数 follow_symlinks を False とする
"""
