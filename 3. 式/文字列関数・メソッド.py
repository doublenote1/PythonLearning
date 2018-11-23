# ****** 文字列型へ型変換 ******

print(str(100) + str(0.123))
print()

# ****** 情報取得 ******

# ==== 文字列の長さを取得: ===
# len(seq|collection)

print(len('abcde'))                # -> 5
print(len('あいうえお'))           # -> 5
print(len('a\tb\\c\n'))            # -> 6
print(len(r'a\tb\\c\n'))           # -> 9
print(len('\u3042\u3044\u3046'))   # -> 3
print(len(r'\u3042\u3044\u3046'))  # -> 18
print()

# === 半角を1文字、全角を2文字として文字列の長さを取得 ===

import unicodedata

print(unicodedata.east_asian_width('あ'))  # -> W
print(unicodedata.east_asian_width('a'))   # -> Na
print(unicodedata.east_asian_width('Ａ'))  # -> F
print(unicodedata.east_asian_width('ｱ'))   # -> H
print(unicodedata.east_asian_width('Å'))  # -> A
print()

def get_east_asian_width_count(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count

print(get_east_asian_width_count('あいうえお'))  # -> 10
print(get_east_asian_width_count('abcde'))       # -> 5
print(get_east_asian_width_count('ｱｲｳｴｵ'))       # -> 5
print(get_east_asian_width_count('ａｂｃｄｅ'))  # -> 10
print(get_east_asian_width_count('あｱaａ'))      # -> 6
print()

# ****** 置換 ******

s = 'one two one two one'

# === 文字列 ===

# 置換した文字列を取得:
# str.replace(old,new[,count])

print(s.replace(' ', '-'))
print(s.replace(' ', ''))
print(s.replace(' ', '-', 2))
# 複数回の置換
print(s.replace('one', 'XXX').replace('two', 'YYY'))
print()

# === 文字 ===

# 変換テーブルを参考に置換した文字を取得:
# str.translate(table)

'''
table 作成方法

① 引数に 辞書を指定:
static str.maketrans(dict)

② 引数に 変換前文字列(x)、変換後文字列(y)、削除対象文字列(z) を指定:
static str.maketrans(x,y[,z])
'''

# --- table 作成 ---

# 引数が一つの場合、辞書にしなければならない
table_dict = str.maketrans({
    '、': None,
    '。': None,
    '・': None
})

# 引数が二つの場合、x と y の文字列が同じ長さで、
# x のそれぞれの文字が y の同じ位置の文字に対応付けられる
table2 = str.maketrans('、。', ',.')
# 辞書の場合
table2_dict = str.maketrans({
    '、': ',',
    '。': '.'
})

# 引数が三つの場合、引数が二つの場合に加え
# z の文字列が None に対応付けられる
table3 = str.maketrans('、。', ',.', '・')
# 辞書の場合
table3_dict = str.maketrans({
    '、': ',',
    '。': '.',
    '・': None
})

# --- table を使って文字列置換 ---

s = "A・B・C、E・F・G 。"

# 変換テーブル(辞書)を使用:

print(s.translate(table_dict))
print(s.translate(table2))
print(s.translate(table2_dict))
print(s.translate(table3))
print(s.translate(table3_dict))
print()

# ****** 大文字・小文字の操作 ******

# === 大文字・小文字変換 ===

s = "pYthon iS a gooD proGramming laNguage"
print(s)

# 先頭の一文字を大文字、他を小文字にする:
print(s.capitalize())

# すべての文字を小文字にする:
print(s.lower())

# すべての文字を大文字にする:
print(s.upper())

# 単語の先頭の一文字を大文字、他を小文字にする:
print(s.title())

# 大文字を小文字に、小文字を大文字にする:
print(s.swapcase())
print()

# === 大文字・小文字判定 ===

# --- すべての文字が小文字かどうか判定する ---

'''
小文字と大文字の区別がある文字が少なくとも一文字以上含まれていて、
その全てが小文字のときはTrue、それ以外はFalseを返す
'''

print('Python'.islower())
print('python'.islower())
# 全角も小文字大文字の区別がある文字とみなされる
print('ｐｙｔｈｏｎ'.islower())
# 数字やカタカナ、平仮名、漢字などは無視される
print('python パイソン 123'.islower())
# 小文字と大文字の区別がある文字が含まれていないとFalse
print('パイソン 123'.islower())
print()

# --- すべての文字が大文字かどうか判定する ---

'''
小文字と大文字の区別がある文字が少なくとも一文字以上含まれていて、
その全てが大文字のときはTrue、それ以外はFalseを返す
'''

print('PYTHON'.isupper())
print('Python'.isupper())
# 全角も小文字大文字の区別がある文字とみなされる
print('ＰＹＴＨＯＮ'.isupper())
# 数字やカタカナ、平仮名、漢字などは無視される
print('PYTHON パイソン 123'.isupper())
# 小文字と大文字の区別がある文字が含まれていないとFalse
print('パイソン 123'.isupper())
print()

# ****** 文字列種別判定 ******

def str_judge(s):

    def conv_b_to_s(b):
        if b:
            return '○'
        else:
            return '☓'
    print(s)
    # 数値
    print('decimal:', conv_b_to_s(s.isdecimal()), end=', ')
    print('digit:', conv_b_to_s(s.isdigit()), end=', ')
    print('numeric:', conv_b_to_s(s.isnumeric()), end=', ')
    # 文字
    print('alpha:', conv_b_to_s(s.isalpha()), end=', ')
    print('alnum:', conv_b_to_s(s.isalnum()))
    print()

# 数値
str_judge('1234567890')
str_judge('１２３４５６７８９０')
str_judge('①②③④⑤⑥⑦⑧⑨')
str_judge('\u00B2')
str_judge('ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ')
str_judge('一二三四五六七八九')
str_judge('壱億参阡萬')
str_judge('〇')  # 漢数時の0
str_judge('1.23')
str_judge('10,000,000')
str_judge('-100')

# 文字
str_judge('abc')
str_judge('あいうえお')
str_judge('アイウエオ')
str_judge('漢字')
str_judge('')

# ****** 埋め・寄せ ******

# --- ゼロ埋め: ---
# str.zfill(width)

print('1234'.zfill(8))
print('1234'.zfill(3))
print('-1234'.zfill(8))
print('+1234'.zfill(8))
print(str(1234).zfill(8))
print()

# --- 右寄せ、左寄せ、中央寄せ ---
# str.rjust|ljust|center(width[,fillchar])

s = '1234'
print(s.rjust(8))
print(s.ljust(8))
print(s.center(8))
print()
print(s.rjust(8, '_'))
print(s.ljust(8, '_'))
print(s.center(8, '_'))
print()
s = '-1234'
print(s.rjust(8, '_'))
print(s.ljust(8, '_'))
print(s.center(8, '_'))
print()
print(str(1234).rjust(8, '_'))
print()

# ****** 文字列折り返し・切り詰めして整形 ******

# === 文字列を折り返し ===

# textwrap.wrap|fill(<対象文字列>, width=70, max_lines=None, placeholder=' [...]')
'''
任意の文字数(半角・全角ともに一文字でカウント)に収まるように単語の切れ目で、
    ・分割したリストを取得: wrap
    ・改行した文字列を取得: fill
'''

# ------------

import textwrap

s = "Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages"

#  wrap:
print(textwrap.wrap(s, width=40))
print()

# fill:
print(textwrap.fill(s, width=40))
print()

# ------------

# max_line を指定すると、それ以降の行数は省略される
# デフォルトの省略文字列 '[...]' は placeholder で変更可能

print(textwrap.fill(s, width=40, max_lines=2, placeholder=' ~'))
print()

# initial_indentで最初の行の先頭に加えられる文字列を指定できる

print(textwrap.fill(s, width=40, initial_indent='  '))
print()

# === 文字列を切り詰め ===

# textwrap.shorten(<対象文字列>, width=70, placeholder=' [...]')
'''任意の文字数に収まるように末尾から単語が切り捨てられる'''

s = 'Python is powerful'

print(textwrap.shorten(s, 12))
print(textwrap.shorten(s, 12, placeholder=' ~'))
print()

# === 決まった設定で wrap() や fill() を行う ===

wrapper = textwrap.TextWrapper(width=30, max_lines=3, placeholder=' ~', initial_indent='  ')

s = "Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages"

print(wrapper.wrap(s))
print()
print(wrapper.fill(s))
