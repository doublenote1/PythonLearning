import os

# ****** OS によるパスの区切り文字の違い ******

"""
・パスの区切り文字はOSによって異なる
・UNIX（Mac を含む）ではスラッシュ '/'、Windows ではバックスラッシュ '\' が使われる
・Python が動作している OS における区切り文字は os.sep または os.path.sep で取得、確認できる
"""

print(os.sep)
print(os.sep is os.path.sep)
print()

# ****** パス文字列からファイル名・フォルダ名・拡張子を取得、結合 ******

file_path = './dir/subdir/filename.ext'
ex_dir_path = './dir/subdir'

# === ファイル名・最下層のフォルダ名(ベースネーム)を取得: ===
# os.path.basename(path)

print(os.path.basename(file_path))
print(os.path.basename(ex_dir_path))
print()

# === ベースネーム直上のフォルダパスを取得: ===
# os.path.dirname(path)

print(os.path.dirname(file_path))
print(os.path.dirname(ex_dir_path))
print()

# === ベースネーム直上のフォルダ名のみを取得 ===

print(os.path.basename(os.path.dirname(file_path)))
print(os.path.basename(os.path.dirname(ex_dir_path)))
print()

# === フォルダパスとファイル名のペアを取得: ===
# os.path.split(path)

"""
os.path.dirname() で取得できるフォルダパスの文字列と
os.path.basename() で取得できるファイル名の文字列のタプルを返す
"""

print(os.path.split(file_path))
print(os.path.split(file_path)[0] == os.path.dirname(file_path))
print(os.path.split(file_path)[1] == os.path.basename(file_path))
print()

"""タプルのアンパックを利用してそれぞれの変数に代入することが可能"""
dir_name, file_name = os.path.split(file_path)
print(dir_name)
print(file_name)
print()

# === 末尾に区切り文字がある場合 ===

"""
最下層のフォルダ名を取得するには、
os.path.dirname() とos.path.basename() を組み合わせる
"""

dir_path_with_sep = '../dir/subdir/'

print(os.path.split(dir_path_with_sep))
print(os.path.basename(os.path.dirname(dir_path_with_sep)))
print()

# === 拡張子を取得: ===
# os.path.splitext(path)

"""
・拡張子とそれ以外に分割されてタプルとして返される
・拡張子はピリオド.込みの文字列
"""

print(os.path.splitext(file_path))

"""タプルのアンパックを利用してそれぞれの変数に代入することが可能"""
root, ext = os.path.splitext(file_path)
print(root)
print(ext)
print()

"""拡張子を変更したパス文字列を作成"""
print(os.path.splitext(file_path)[0] + '.jpg')
print()

"""ピリオドなしの拡張子を取得"""
print(os.path.splitext(file_path)[1][1:])

# === ファイル名とフォルダ名を結合してパス文字列を作成: ===
# os.path.join(path, *paths)

"""引数に指定した文字列が区切り文字で区切られて結合される"""

print(os.path.join('dir', 'subdir', 'filename.ext'))

"""同じフォルダの別のファイルのパス文字列を作成"""
print(os.path.join(os.path.dirname(file_path), 'other_file.ext'))

