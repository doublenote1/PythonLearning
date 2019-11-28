from user import save_file

dir_path = 'zip'
save_file(dir_path, 'test1.txt')
save_file(dir_path, 'test2.txt')
save_file(dir_path, 'test3.txt')
save_file(dir_path, 'test4.txt')

# ****** 圧縮 ******

# === 複数のファイルをzipファイルに圧縮 ===

"""
・ZipFileオブジェクトを作成し、write() メソッドで圧縮したいファイルを追加していく

・zipファイルを新規作成する場合は、
  ZipFileオブジェクトのコンストラクタの第一引数 file に
  作成する zip ファイルのパスを指定し、
  第二引数modeを'w'とする。

・さらに、第三引数 compression で圧縮方式を指定できる

    zipfile.ZIP_STORED:   圧縮せず複数ファイルをまとめるだけ（デフォルト）
    zipfile.ZIP_DEFLATED: 通常のZIP圧縮（要 zlib モジュール）
    zipfile.ZIP_BZIP2:    BZIP2圧縮（要 bz2 モジュール）
    zipfile.ZIP_LZMA:     LZMA圧縮（要 lzma モジュール）

・BZIP2、LZMA のほうが圧縮率が高い（より小さいサイズに圧縮できる）が、
  圧縮にかかる時間が長くなる

・write() メソッドでは、第一引数 filename のファイルを
  第二引数 arcname という名前でzipファイルに書き込む
・arcname は省略するとfilename がそのまま使われる
・arcnameにディレクトリ構造を指定することも可能

・ZipFile オブジェクトは close() メソッドでクローズする必要があるが、
  with文を使うとブロックが終了したときに自動的にクローズされる
"""

import zipfile

with zipfile.ZipFile(dir_path + '/comp.zip', 'w',
                     compression=zipfile.ZIP_DEFLATED) as new_zip:
    new_zip.write(dir_path + '/test1.txt', arcname='test1.txt')
    new_zip.write(dir_path + '/test2.txt', arcname='zipdir/test2.txt')
    new_zip.write(dir_path + '/test3.txt', arcname='zipdir/sub_dir/test3.txt')

"""
write()メソッドの引数compress_typeを指定することで、
ファイルごとに圧縮方式を選択することもできる。
"""

with zipfile.ZipFile(dir_path + '/comp_single.zip', 'w') as new_zip:
    new_zip.write(dir_path + '/test1.txt', arcname='test1.txt',
                  compress_type=zipfile.ZIP_DEFLATED)
    new_zip.write(dir_path + '/test2.txt', arcname='zipdir/test2.txt',
                  compress_type=zipfile.ZIP_BZIP2)
    new_zip.write(dir_path + '/test3.txt', arcname='zipdir/sub_dir/test3.txt',
                  compress_type=zipfile.ZIP_LZMA)

# === 既存のzipファイルに新たなファイルを追加 ===

"""
・既存のzipファイルに新たなファイルを追加するには、
  ZipFile オブジェクトを作成する際に、
  コンストラクタの第一引数 file を既存の zip ファイルのパス、
  第二引数 mode を 'a' とする

・あとは上の例と同じく、write() メソッドでファイルを追加すればOK。
"""

with zipfile.ZipFile(dir_path + '/comp.zip', 'a') as existing_zip:
    existing_zip.write(dir_path + '/test4.txt', arcname='test4.txt')

# === フォルダをzipファイルに圧縮: ===
# shutil.make_archive()

"""
・第一引数base_nameには作成するzipファイルの名前（拡張子なし）、
  第二引数formatにはアーカイブフォーマットを指定する。

・第二引数formatには、 zip, tar, gztar, bztar, xztar が選択可能。

・第三引数root_dirには圧縮するディレクトリのルートディレクトリのパス、
  第四引数base_dirには圧縮するディレクトリのroot_dirからの相対パスを指定する。
・どちらもデフォルトはカレントディレクトリ: '.'。
・base_dir を省略すると、root_dir 全体が圧縮される。
"""

"""
オリジナル:

dir
├── dir_sub
│     └── test_sub.txt
└── test.txt
"""
save_file(dir_path + '/dir/dir_sub', 'test_sub.txt')
save_file(dir_path + '/dir', 'test.txt')

import shutil

# --- base_dir を省略した場合 ---

shutil.make_archive(dir_path + '/dir', 'zip', root_dir=dir_path + '/dir')

"""
結果:

dir.zip
├─ dir_sub
│   └─ test_sub.txt
└─ test.txt
"""

# --- base_dirにroot_dirの中のディレクトリを指定した場合 ---

shutil.make_archive(dir_path + '/dir_sub', 'zip', root_dir=dir_path + '/dir',
                    base_dir='dir_sub')

"""
結果:

dir_sub.zip
└─ dir_sub
     └─ test_sub.txt
"""

# === パスワード付きのzipファイルに圧縮 ===

"""
・zipfile モジュールでは、パスワードで保護された zip を作成することはできない。

・ファイルをパスワード付きの zip ファイルに圧縮したい場合は、
  サードパーティのライブラリ pyminizip を使う。
"""

import pyminizip

pyminizip.compress(dir_path + "/test1.txt", "dir", dir_path + "/pass.zip", "aaa", 5)

# ****** 解凍 ******

"""
・ZipFile オブジェクトを、
  コンストラクタの第一引数 file を既存の zip ファイルのパス、
  第二引数 mode を 'r' として作成する。
・引数 mode はデフォルトが r なので省略可能。
"""

# === zipファイルの中身を確認 ===

with zipfile.ZipFile(dir_path + '/comp.zip') as existing_zip:
    print(existing_zip.namelist())

# === zipファイルの中身をすべて解凍（展開） ===

"""
・第一引数 path に展開先のディレクトリのパスを指定する。
・省略するとカレントディレクトリに解凍される。
"""

with zipfile.ZipFile(dir_path + '/comp.zip') as existing_zip:
    existing_zip.extractall(dir_path + '/ext_comp')

"""
・パスワード付きの zip ファイルは
  extractall() メソッドの引数 pwd にパスワードを指定すると解凍できる。
"""

with zipfile.ZipFile(dir_path + '/pass.zip') as pass_zip:
    pass_zip.extractall(dir_path + '/ext_pass', pwd=b'aaa')

# === zipファイルの中身を選択して解凍（展開） ===

"""
・extract()メソッドの第一引数に解凍するファイル名
  （zipファイル内のディレクトリに格納されている場合はそれも含めたパス）、
  第二引数 path に展開先のディレクトリのパスを指定する。
・引数 path は省略するとカレントディレクトリに解凍される。
"""

with zipfile.ZipFile(dir_path + '/comp.zip') as existing_zip:
    existing_zip.extract('test1.txt', dir_path + '/ext_comp2')

"""
extract()メソッドもextractall()メソッドと同様、
引数pwdにパスワードを指定できる。
"""

with zipfile.ZipFile(dir_path + '/pass.zip') as pass_zip:
    pass_zip.extract('dir/test1.txt', dir_path + '/ext_pass2', pwd=b'aaa')

# ===============================

import shutil

shutil.rmtree(dir_path)
