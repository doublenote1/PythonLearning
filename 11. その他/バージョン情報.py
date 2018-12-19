# ****** Python のバージョン ******

# === コマンドラインでバージョンを確認、表示 ===

"""
python --version
python -V
"""

# === コード中でバージョンを取得 ===

# --- sys ---

import sys

# - 1: バージョン番号を含む様々な情報の文字列 -

print(sys.version)
# -> 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
print()

# - 2: バージョン番号の数値などのタプル -

print(sys.version_info)
# -> sys.version_info(major=3, minor=7, micro=0, releaselevel='final', serial=0)

# インデックスで値を取得

print([sys.version_info[i] for i in range(5)])  # -> [3, 7, 0, 'final', 0]

# 属性で値を取得

if sys.version_info.major == 3:
    print('python3')  # -> python3
else:
    print('python2')
print()

# --- platform ---

import platform

# - 1: バージョン番号の文字列 -

print(platform.python_version())  # -> 3.7.0
print()

# - 2: バージョン番号の文字列のタプル

print(platform.python_version_tuple())  # -> ('3', '7', '0')
print()

# ****** パッケージのバージョン ******

import jinja2
import pip

print(jinja2.__version__)  # -> 2.10
print(pip.__version__)  # -> 18.0
print()

