# ****** フォルダを作成 ******

# === 新しいフォルダを作成: ===
# os.mkdir(path, mode=0o777, *, dir_fd=None)

"""
・末尾の区切り文字（UNIX, Macはスラッシュ、Windows はバックスラッシュ）はあっても無くても OK
・既に存在しているディレクトリを指定するとエラー（FileExistsError例外）が発生する
  例えば、同じパス文字列に対して繰り返し os.mkdir() を実行するとエラーとなる
"""
import os

new_dir_path = 'new-dir'
os.mkdir(new_dir_path)
try:
    os.mkdir(new_dir_path)
except FileExistsError as e:
    print(e)
os.rmdir(new_dir_path)

"""
まだ存在していないディレクトリの中に新たなディレクトリを作成する場合もエラー
"""
new_dir_path_recursive = 'new-dir/new-sub-dir'
try:
    os.mkdir(new_dir_path_recursive)
except FileNotFoundError as e:
    print(e)
print()

"""
・os.mkdir() を使う場合は作成するディレクトリの直上までのディレクトリが存在している必要がある
・一気に新規作成するには次に説明する os.makedirs() を使う
"""

# === 深い階層のディレクトリまで再帰的に作成: ===
# os.makedirs(name, mode=0o777, exist_ok=False)

"""
・os.makedirs() は再帰的にディレクトリを作成する関数
・深い階層のディレクトリまで一気に新規作成することができる
・既に存在しているディレクトリを指定するとエラー（FileExistsError例外）が発生する
・例えば、同じパス文字列に対して繰り返し os.makedirs() を実行するとエラーとなる
・引数 exist_ok=True とすると既に存在しているディレクトリを指定してもエラーにならない
"""

os.makedirs(new_dir_path_recursive)
os.makedirs(new_dir_path_recursive, exist_ok=True)
try:
    os.makedirs(new_dir_path_recursive)
except FileExistsError as e:
    print(e)
os.rmdir(new_dir_path_recursive)

def my_makedirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

my_makedirs(new_dir_path_recursive)
import shutil

shutil.rmtree(new_dir_path)
