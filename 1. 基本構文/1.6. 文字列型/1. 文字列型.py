# ****** エスケープシーケンス ******

r"""
\\         : '\' 文字そのもの
\'         : シングルクオーテーション
\"         : ダブルクオーテーション
\a         : ベル
\b         : バックスペース
\f         : 改ページ
\r         : キャリッジリターン
\n         : 改行
\t         : 水平タブ
\v         : 垂直タブ
\N{name}   : Unicode データベース中で名前 name を持つ文字
\uxxxx     : 16ビットの16進数値xxxxを持つUnicode文字
\Uxxxxxxxx : 32ビットの16進数値xxxxxxxxを持つUnicode文字
\ooo       : 8進数oooを持つASCII文字
\xhh       : 16進数hhを持つASCII文字
\0         : NULL
"""

# === エスケープシーケンスを無効化(raw 文字列) ===

print('C:\some\\name\\test')  # 通常文字列
print(r'C:\some\name\test')  # raw 文字列

# 末尾に奇数個の '\' を表現したい場合
print('C:\some\\name\\test\\')  # 通常文字列
print(r'C:\some\name\test' + '\\')  # raw 文字列 + 通常文字列

# 末尾に偶数個の '\' を表現したい場合
print('C:\some\\name\\test\\\\')  # 通常文字列
print(r'C:\some\name\test\\')  # raw 文字列
print()

# ****** コード上、長い行を複数に分ける ******

# === 括弧を使わない場合 ===

# ①行末の '\' でその後の改行が無視される
n = 1 + 2 \
    + 3
print(n)

# ②連続した文字列リテラルは連結される
s = 'Py' 'thon'
print(s)

# 上記①と②の法則の組み合わせ
s = 'abc' \
    'efg' \
    'hij'
print(s)
print()

# === 括弧を使う場合 ===

'''
括弧内はトークン間以外なら '\' が無くても自由に改行可能
'''

x = ('Put several strings within parentheses '
     'to have them joined together.')
print(x)

x = (1 + 2
     + 3)
print(x)

print()

# ****** 改行を含む文字列の取得 ******

# === 三連引用符 ===

s = """\
Line1
Line2
Line3
"""
print(s, end='')
print()

# === コード上にインデントをつけたい場合 ===

s = 'Line1\n' \
    'Line2\n' \
    'Line3'
print(s)
print()

s = (
    'Line1\n'
    'Line2\n'
    'Line3'
)
print(s)
print()

# === 文字列中にインデントを加えたい場合

s = """\
Line1
    Line2
        Line3
"""
print(s, end='')
print()

s = 'Line1\n' \
    '    Line2\n' \
    '        Line3\n'
print(s, end='')
print()

s = (
    'Line1\n'
    '    Line2\n'
    '        Line3\n'
)
print(s, end='')
print()

# ****** 文字列とリストの相互変換 ******

# --- 連結して文字列をかえす ---

lst = ['Line1', 'Line2', 'Line3']
print(', '.join(lst))
print('\n'.join(lst))
print()

# --- 分割してリストをかえす ---

# 空白で分割
print('one two     three\nfour\tfive'.split())

# 指定文字列で分割
print('one, two, three, four, five'.split(', '))

# 正規表現で分割
import re

print(re.split(r'\W+', 'one  two  ,: three-four::: five'))

# 改行で分割
print('Line1\nLine2\r\nLine3\rline4\n'.splitlines())
# 結果に改行を含む
print('Line1\nLine2\r\nLine3\rline4\n'.splitlines(True))
print()

# === 区切り文字の置換 ===

import re

# 改行文字
print(', '.join('one\ntwo\r\nthree\rfour'.splitlines()))

# 空白
print(', '.join('one two  \t   three\nfour'.split()))

# 文字列を split(<区切り文字>) で区切り、
# 区切った要素の左右の余分な文字を x.strip(<削除文字>) で削除し、
# リストの要素に追加する時、内容のない物は除外(if文)
s = 'one ,, two::,::three--,--,four,'
e = ' :-'
print(', '.join([x.strip(e) for x in s.split(',') if not x.strip(e) == '']))

# 正規表現で区切り文字を指定
# s = 'one 　two\r\n\tthree,:{~four'
print(', '.join(re.split(r'\W+', s)))

print()

# 最大分割回数を指定
s = 'one,two,three,four'
print(' - '.join(s.split(',', maxsplit=2)))
print(' - '.join(s.rsplit(',', maxsplit=2)))
print()

# === 区切り文字以降(以前)の文字列を削除してかえす ===

s = 'one,two,three,four'

# n番目の区切り文字以前を削除
print(s.split(',', 1)[-1])
print(s.split(',', 2)[-1])
print(s.split(',', 3)[-1])

# 後ろからn番目の区切り文字以降を削除
print(s.rsplit(',', 1)[0])
print(s.rsplit(',', 2)[0])
print(s.rsplit(',', 3)[0])
