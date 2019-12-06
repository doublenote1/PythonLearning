# === os モジュールと glob モジュールを使って一括でリネーム ===

import os

"""
・
└─testdir1
    ├─a.jpg
    ├─b.jpg
    ├─c.jpg
    ├─d.jpg
    └─e.jpg
└─testdir2
    ├─...
└─...

"""

def lst_files(i):
    lst = glob.glob(f'{folders[i]}/*')
    lst = [x.replace(folders[i] + '\\', '') for x in lst]
    print(lst)

num = 5
folder_name = 'testdir'
folders = []
for i in range(num):
    folders.append(f'{folder_name}{i}')
    os.makedirs(folders[i], exist_ok=True)
    for tmp in ['a', 'b', 'c', 'd', 'e']:
        with open(f'{folders[i]}/{tmp}.jpg', 'w'):
            pass


# --- globモジュールでファイルリストを取得: ---
# glob.glob(pathname, *, recursive=False)

import glob

lst_files(0)
print()

"""
*:      すべてのものにマッチする
?:      任意の一文字にマッチする
[abc]:  a, b, cのいずれかの一文字にマッチする
[!abc]: a, b, c以外の一文字にマッチする
"""

# --- ファイルまたはディレクトリ src の名前を dst へ変更 ---
# os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)

import os

os.rename(f'{folders[0]}/a.jpg', f'{folders[0]}/000.jpg')
lst_files(0)

# --- ファイルの前に文字列・連番を追加するコードの例 ---

"""
・os.path.basename()でファイル名を取得し、その前に文字列や連番を追加してから、
  os.path.join()で元のパスと連結する。
・以下の例では、すべてのファイル名の前にimg_を追加する。
"""

import os
import glob

files = glob.glob(folders[1] + '\*')

for f in files:
    os.rename(f, os.path.join(folders[1], 'img_' + os.path.basename(f)))
lst_files(1)
"""
結果:

・
└─testdir
    ├─img_a.jpg
    ├─img_b.jpg
    ├─img_c.jpg
    ├─img_d.jpg
    └─img_e.jpg
"""

"""
・連番を追加する場合はfor文のところをこんな感じに変える。
・enumerate()でfor文を回すことで、0から順番にカウントされる数値を取得できる。
・ここでは三桁で0埋めしている。
・000からじゃなくて001から始めたい場合は、enumerateの第二引数を1とする
"""
files = glob.glob(folders[2] + '\*')
for i, f in enumerate(files):
    os.rename(f, os.path.join(folders[2], '{0:03d}'.format(i) + '_' + os.path.basename(f)))
lst_files(2)
"""
結果:

・
└─testdir
    ├─000_a.jpg
    ├─001_b.jpg
    ├─002_c.jpg
    ├─003_d.jpg
    └─004_e.jpg
"""

# --- ファイルの後ろに文字列・連番を追加するコードの例 ---

"""
・os.path.splitext()で拡張子とルートパスに分割してから、
  ルートパスの方に文字列や連番を追加する
・以下の例では、すべてのファイル名の後に_imgを追加する。
"""

import os
import glob

files = glob.glob(folders[3] + '\*')

for f in files:
    ftitle, fext = os.path.splitext(f)
    os.rename(f, ftitle + '_img' + fext)
lst_files(3)

"""
ファイルの前に文字列・連番を追加するときと同様に、
連番を追加する場合はfor文のところを変える
"""
files = glob.glob(folders[4] + '\*')
for i, f in enumerate(files):
    ftitle, fext = os.path.splitext(f)
    os.rename(f, ftitle + '_' + '{0:03d}'.format(i) + fext)
lst_files(4)
"""
結果:

・
└─testdir
    ├─a_000.jpg
    ├─b_001.jpg
    ├─c_002.jpg
    ├─d_003.jpg
    └─e_004.jpg
"""

# =====================

import shutil

for i in range(num):
    shutil.rmtree(f'{folder_name}{i}')
