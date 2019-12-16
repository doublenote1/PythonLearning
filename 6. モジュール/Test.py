import os
import pprint
import sys


"スクリプトファイルの一階層上のディレクトリ"
dir_up = os.path.join(os.path.dirname(__file__), '..')
print(dir_up)
# -> D:/Documents/Projects/Python Learning/6. モジュール\..

sys.path.append(dir_up)
pprint.pprint(sys.path)
# -> [...,
# ->  ...,
# ->  'D:/Documents/Projects/Python Learning/6. モジュール\\..']
