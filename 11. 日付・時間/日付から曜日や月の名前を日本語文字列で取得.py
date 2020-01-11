# === ロケールを日本語に設定する ===

"""
環境によって異なるが、strftime() メソッドで書式化コード%A, %a, %B, %bを使うと、
曜日・月の名前が英語表記で得られる。
"""

import datetime
import locale

dt = datetime.datetime(2018, 1, 1)
print(dt)  # -> 2018-01-01 00:00:00
print(dt.strftime('%A, %a, %B, %b'))  # -> Monday, Mon, January, Jan
print()

"""
時刻の書式化に関するロケールカテゴリの設定 locale.LC_TIME を locale.getlocale() で確認すると、
日本語に設定されていない
"""

print(locale.getlocale(locale.LC_TIME))  # -> (None, None)
print()

"""
・locale.setlocale() で locale.LC_TIME を日本語（UTF-8）ja_JP.UTF-8 に設定すると、
  日本語表記の曜日・月名が得られる。
・locale.LC_ALL ですべてのロケールカテゴリを設定することもできるが、その場合、
  例えば金額に関する設定 locale.LC_MONETARY なども影響される

※Windows 環境ではうまくいかない？
"""

try:
    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
    print(locale.getlocale(locale.LC_TIME))  # -> ('ja_JP', 'UTF-8')
    print(dt.strftime('%A, %a, %B, %b'))  # -> 月曜日, 月, 1月, 1
    print()
except locale.Error as e:
    print('locale.Error:', e)
print()

"""
日付の文字列からその日付の曜日を日本語で取得したい場合は、

locale.setlocale() で locale.LC_TIME を日本語 （UTF-8）ja_JP.UTF-8 に設定
strptime() で文字列から datetime オブジェクトに変換
その datetime オブジェクトで strftime() を書式化コード%A, %a, %B, %bで呼び出し

という流れで実現できる。
"""

try:
    locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
    s = '2018-01-01'
    s_dow = datetime.datetime.strptime(s, '%Y-%m-%d').strftime('%A')
    print(s_dow)  # -> 月曜日
except locale.Error as e:
    print('locale.Error:', e)
print()


# === 新たな関数を定義 ===

"""
・ロケールをいじりたくない場合は、新たな関数を定義する。

・strftime() で書式化コード%wを使うと、
  日曜日が 0 で土曜日が 6 の 10進表記した文字列が得られる。
"""
import datetime

dt = datetime.datetime(2018, 1, 1)
print(dt)  # -> 2018-01-01 00:00:00

w_s = dt.strftime('%w')
print(w_s)  # -> 1
print(type(w_s))  # -> <class 'str'>
print()

"""
得られた文字列を int() で数値に変換し、
日本語文字列の曜日の名前のリストを定義して取り出せば、目的が達成できる。
"""

w_n = int(w_s)
print(w_n)  # -> 1
print(type(w_n))  # -> <class 'int'>

w_list = ['日曜日', '月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日']
print(w_list[w_n])  # -> 月曜日
print()

"""関数化する"""

def get_day_of_week_jp(dt):
    w_list = ['日曜日', '月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日']
    return(w_list[int(dt.strftime('%w'))])

dt2 = datetime.datetime(2018, 1, 2)
print(dt2)  # -> 2018-01-02 00:00:00
print(get_day_of_week_jp(dt2))  # -> 火曜日

"""
日付の文字列からその日付の曜日を日本語で取得したい場合も、
strptime() で文字列からdatetimeオブジェクトに変換するだけで、あとは同じ。
"""
s = '2018年1月10日'
print(get_day_of_week_jp(datetime.datetime.strptime(s, '%Y年%m月%d日'))) # -> 水曜日

"""
文字列のフォーマットが固定されているのであれば、
strptime() による変換も関数化してもいいかもしれない。
"""
def get_day_of_week_jp_s(s):
    return get_day_of_week_jp(datetime.datetime.strptime(s, '%Y年%m月%d日'))

print(get_day_of_week_jp_s(s))  # -> 水曜日

"""
月の名前を任意の文字列にしたい場合も考え方は同じ。
属性 month は数値なので int() を使う必要はない。
また、1月が 1 なのでリストの定義に注意。
"""
def get_month_jp(dt):
    m_list = [None, '睦月', '如月', '弥生', '卯月', '皐月', '水無月', '文月', '葉月', '長月', '神無月', '霜月', '師走']
    return(m_list[dt.month])

print(get_month_jp(dt2))  # -> 睦月
