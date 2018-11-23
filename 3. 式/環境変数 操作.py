# === カレントディレクトリを取得 ===

import os

path = os.getcwd()  # get current working directory の略
print(path)
print(type(path))

# === カレントディレクトリを変更(移動) ===

os.chdir('../')  # 上の階層への移動

print(os.getcwd())

# === 実行ファイルの場所(パス)を取得する ===

print('__file__: ', __file__)
