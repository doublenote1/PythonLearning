"""
・Python では、標準の csv モジュールを使って
  csv ファイルを簡単に読み書きできる

・例えば、

11,12,13,14
21,22,23,24
31,32,33,34

という sample.csv は以下のように読める
"""

import csv

with open('sample.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
print()
# -> ['11', '12', '13', '14']
# -> ['21', '22', '23', '24']
# -> ['31', '32', '33', '34']

"""
・ここで注意が必要なのが、コンマの後に空白（スペース）がある場合
・本来、コンマの後には不要な空白を入れるべきではないが、
  たまにスペースが入ってるファイルを見かける
・そのような場合、デフォルトでは空白が無視されずそのまま読み込まれてしまう

11, 12, 13, 14
21, 22, 23, 24
31, 32, 33, 34

という、コンマの後にスペースが入ったファイルを上のコードで読み込むと、
"""

with open('sample_space.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
print()
# -> ['11', ' 12', ' 13', ' 14']
# -> ['21', ' 22', ' 23', ' 24']
# -> ['31', ' 32', ' 33', ' 34']

"""と出力される"""

"""
csv.reader で skipinitialspace=True と指定すると、
コンマの後の空白がスキップされる
"""

with open('sample_space.csv', 'r') as f:
    reader = csv.reader(f, skipinitialspace=True)
    for row in reader:
        print(row)
print()
# -> ['11', '12', '13', '14']
# -> ['21', '22', '23', '24']
# -> ['31', '32', '33', '34']

"""
上のような簡単な例であれば strip() で空白を消去してやってもいいが、
問題は、次のようなダブルクオーテーションで囲まれている場合


"one,one", "two,two", "three,three"


ダブルクオーテーションで囲まれている部分は一つの要素として見なしてほしいが、
skipinitialspace=False（デフォルト）だと、
"""

with open('sample_double_quotation.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
print()
# ['one,one', ' "two', 'two"', ' "three', 'three"']

"""となってしまう"""

"""skipinitialspace=True とすると OK"""

with open('sample_double_quotation.csv', 'r') as f:
    reader = csv.reader(f, skipinitialspace=True)
    for row in reader:
        print(row)
# ['one,one', 'two,two', 'three,three']

"""
・pandas の read_csv() で csv ファイルを読むときも同様
・コンマの後にスペースがある csv ファイルの場合は
  read_csv(skipinitialspace=True) とする
"""
