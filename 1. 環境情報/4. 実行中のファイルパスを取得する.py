import os

"作業ディレクトリを取得"
print(os.getcwd())
# -> D:\Documents\Projects\Python Learning\11. 環境情報

"実行ファイルの作業ディレクトリからの相対パスを取得"
print(__file__)
# -> D:/Documents/Projects/Python Learning/11. 環境情報/4. 実行中のファイルのパスを取得する.py

"「__file__」から「ファイル名」を取得"
print(os.path.basename(__file__))
# -> 4. 実行中のファイルのパスを取得する.py
"""「__file__」から「ディレクトリ名」を
作業ディレクトリからの「相対パス」で取得"""
print(os.path.dirname(__file__))
# -> D:/Documents/Projects/Python Learning/11. 環境情報

"「__file__」から「ファイル名」を「絶対パス」で取得"
print(os.path.abspath(__file__))
# -> D:\Documents\Projects\Python Learning\11. 環境情報\4. 実行中のファイルのパスを取得する.py
"「__file__」から「ディレクトリ名」を「絶対パス」で取得"
print(os.path.dirname(os.path.abspath(__file__)))
# -> D:\Documents\Projects\Python Learning\11. 環境情報

"実行中のファイルの場所を基準にほかのファイルを読み込み"
target_path_1 = os.path.join(os.path.dirname(__file__), 'test.txt')
with open(target_path_1) as f:
    print(f.read())
# -> line 1
# -> line 2
# -> line 3

# [nkmk note](https://note.nkmk.me/python-script-file-path/)
