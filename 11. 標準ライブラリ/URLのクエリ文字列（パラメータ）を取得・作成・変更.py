"""
・Python の標準ライブラリの urllib.parse モジュールを使うと、
  URL のクエリ文字列（クエリパラメータ）を取得したり、作成したりできる。
"""

import urllib.parse

クエリ文字列（クエリパラメータ）とは

例えば、Googleで「桜」を画像検索した結果のURLは以下の通り。

https://www.google.co.jp/search?q=%E6%A1%9C&tbm=isch

q=%E6%A1%9C&tbm=ischの部分をクエリ文字列（クエリパラメータ）という。

key1=value1&key2=value2&...のように、keyとvalueが=を連結した要素が&で連結されている。

上のGoogleの例のクエリ文字列q=%E6%A1%9C&tbm=ischでは、

q=%E6%A1%9Cは検索ワード（q）が「桜」（%E6%A1%9C）であること
tbm=ischは検索の種類（tbm）が画像検索（isch）であること

を示している。

「桜」のような日本語の文字は%E6%A1%9CのようにURLエンコードされる。

関連記事: PythonでURLエンコード・デコード（urllib.parse.quote, unquote）

以下で説明する関数では自動的にURLエンコード処理が行われる。
URLからクエリ文字列（パラメータ）を取得
urllib.parse.urlparse()

urllib.parse.urlparse()でURLを構成要素に分解（パース）できる。

21.8. urllib.parse.urlparse() — URL を解析して構成要素にする — Python 3.6.5 ドキュメント

urllib.parse.urlparse()は名前付きタプルを返し、queryでクエリ文字列を取得できる。

url = 'https://www.google.co.jp/search?q=%E6%A1%9C&tbm=isch'

print(urllib.parse.urlparse(url))
# ParseResult(scheme='https', netloc='www.google.co.jp', path='/search', params='', query='q=%E6%A1%9C&tbm=isch', fragment='')

qs = urllib.parse.urlparse(url).query

print(qs)
# q=%E6%A1%9C&tbm=isch

print(type(qs))
# <class 'str'>

source: urllib_parse_query_string.py
クエリ文字列（パラメータ）を辞書・リストに変換
辞書に変換: urllib.parse.parse_qs()

urllib.parse.parse_qs()でクエリ文字列を辞書に変換できる。

qs_d = urllib.parse.parse_qs(qs)

print(qs_d)
# {'q': ['桜'], 'tbm': ['isch']}

print(type(qs_d))
# <class 'dict'>

source: urllib_parse_query_string.py

辞書の値はリストで、その中に値がURLデコードされた文字列として格納。

print(qs_d['q'])
# ['桜']

print(type(qs_d['q']))
# <class 'list'>

print(qs_d['q'][0])
# 桜

print(type(qs_d['q'][0]))
# <class 'str'>

source: urllib_parse_query_string.py
リストに変換: urllib.parse.parse_qsl()

urllib.parse.parse_qsl()でクエリ文字列をリストに変換できる。

qs_l = urllib.parse.parse_qsl(qs)

print(qs_l)
# [('q', '桜'), ('tbm', 'isch')]

print(type(qs_l))
# <class 'list'>

source: urllib_parse_query_string.py

リストの要素はクエリ文字列のkeyとvalueのペアのタプル。URLデコードされている。

print(qs_l[0])
# ('q', '桜')

print(type(qs_l[0]))
# <class 'tuple'>

print(qs_l[0][1])
# 桜

print(type(qs_l[0][1]))
# <class 'str'>

source: urllib_parse_query_string.py
辞書・リストからクエリ文字列（パラメータ）を作成
urllib.parse.urlencode()

第一引数に辞書を指定するとクエリ文字列が返される。

d_qs = urllib.parse.urlencode(d)

print(d_qs)
# key1=value+%2F+one&key2=%E3%83%90%E3%83%AA%E3%83%A5%E3%83%BC2

print(type(d_qs))
# <class 'str'>

source: urllib_parse_query_string.py

第一引数にはリストも指定可能。リストの要素はクエリ文字列のkeyとvalueのペアのタプル（urllib.parse.parse_qsl()で取得できる形）である必要がある。

l = [('key1', 'value / one'), ('key2', 'バリュー2')]

l_qs = urllib.parse.urlencode(l)

print(l_qs)
# key1=value+%2F+one&key2=%E3%83%90%E3%83%AA%E3%83%A5%E3%83%BC2

print(type(l_qs))
# <class 'str'>

source: urllib_parse_query_string.py

例から分かるように、それぞれの要素はURLエンコードされる。URLエンコード処理は引数quote_via, safeで細かく設定可能。
引数quote_via, safe

デフォルトではURLエンコードにはurllib.parse.quote_plus()が使われるが、引数quote_viaを指定することでurllib.parse.quote()を使うことが可能。

urllib.parse.quote_plus()は空白を+に変換し、urllib.parse.quote()は空白を%20に変換する。

print(urllib.parse.urlencode(d))
# key1=value+%2F+one&key2=%E3%83%90%E3%83%AA%E3%83%A5%E3%83%BC2

print(urllib.parse.urlencode(d, quote_via=urllib.parse.quote))
# key1=value%20%2F%20one&key2=%E3%83%90%E3%83%AA%E3%83%A5%E3%83%BC2

source: urllib_parse_query_string.py

さらに、引数safeでURLエンコードしない文字を指定できる。半角文字、数字、および-, _, .はsafeによらず変換されない。デフォルトはsafe=''（空文字列）なので、それ以外の文字すべてが変換される。

print(urllib.parse.urlencode(d, safe='/'))
# key1=value+/+one&key2=%E3%83%90%E3%83%AA%E3%83%A5%E3%83%BC2

print(urllib.parse.urlencode(d, safe='/', quote_via=urllib.parse.quote))
# key1=value%20/%20one&key2=%E3%83%90%E3%83%AA%E3%83%A5%E3%83%BC2

source: urllib_parse_query_string.py

URLエンコードについては以下の記事も参照。

関連記事: PythonでURLエンコード・デコード（urllib.parse.quote, unquote）

引数doseq

上述のように、urllib.parse.parse_qs()は値がリストの辞書を返す。これをそのままurllib.parse.urlencode()に渡すと、リストの括弧[]などを含んだ文字列に変換されてしまう。

print(qs_d)
# {'q': ['桜'], 'tbm': ['isch']}

print(urllib.parse.urlencode(qs_d))
# q=%5B%27%E6%A1%9C%27%5D&tbm=%5B%27isch%27%5D

source: urllib_parse_query_string.py

引数doseq=Trueとすると、リスト内の要素に対して処理される。

print(urllib.parse.urlencode(qs_d, doseq=True))
# q=%E6%A1%9C&tbm=isch

source: urllib_parse_query_string.py
既存のURLのクエリ文字列（パラメータ）を変更

これまで説明した関数を使って既存のURLのクエリ文字列（パラメータ）を変更する方法を示す。

はじめに使った、Googleで「桜」を画像検索した結果のURLを例とする。

print(url)
# https://www.google.co.jp/search?q=%E6%A1%9C&tbm=isch

source: urllib_parse_query_string.py
クエリ文字列（パラメータ）を上書き・追加

例えば、検索の種類（tbm）を画像検索（isch）から動画検索（vid）に変更する場合、もっとも簡単なのは文字列メソッドreplace()で置換する方法。

print(url.replace('isch', 'vid'))
# https://www.google.co.jp/search?q=%E6%A1%9C&tbm=vid

source: urllib_parse_query_string.py

ただし、この方法だとURL文字列の他の部分に置換元の文字列が含まれていると余計に置換されてしまい、正しい結果が得られない。

安全に処理したい場合、以下のような関数で変更できる。

def update_query(url, key, org_val, new_val):
    pr = urllib.parse.urlparse(url)
    d = urllib.parse.parse_qs(pr.query)
    l = d.get(key)
    if l:
        d[key] = [new_val if v == org_val else v for v in l]
    else:
        d[key] = new_val
    return urllib.parse.urlunparse(pr._replace(query=urllib.parse.urlencode(d, doseq=True)))

source: urllib_parse_query_string.py

処理の流れは以下の通り。

urllib.parse.urlparse()でURLを構成要素に分解（パース）
抽出したクエリ文字列をurllib.parse.parse_qs()で辞書に変換
引数で指定したkeyに応じて辞書の値を変更
keyが存在する場合は、リストの要素を新しい値に置換
keyが存在しない場合は、新しいkeyと新しい値を追加
urllib.parse.urlencode()でクエリ文字列を作成
元の名前付きタプルnamedtupleの値を_replace()メソッドで置き換え
urllib.parse.urlunparse()でURLを再構築

細かい処理部分は以下の記事を参照。

関連記事: Pythonの辞書のgetメソッドでキーから値を取得（存在しないキーでもOK）
関連記事: Pythonのリスト（配列）の特定の要素を抽出、置換、変換
8.3. collections somenamedtuple._replace() — コンテナデータ型 — Python 3.6.5 ドキュメント

結果を確認。

print(update_query(url, 'tbm', 'isch', 'vid'))
# https://www.google.co.jp/search?q=%E6%A1%9C&tbm=vid

print(update_query(url, 'q', '桜', '梅'))
# https://www.google.co.jp/search?q=%E6%A2%85&tbm=isch

print(update_query(url, 'new-key', 'xxx', 'yyy'))
# https://www.google.co.jp/search?q=%E6%A1%9C&tbm=isch&new-key=yyy

source: urllib_parse_query_string.py

elseブロックを削除するとkeyが存在しない場合に新たに追加されなくなる。
クエリ文字列（パラメータ）を削除

keyを指定して削除する関数は以下の通り。

def remove_query(url, key):
    pr = urllib.parse.urlparse(url)
    d = urllib.parse.parse_qs(pr.query)
    d.pop(key, None)
    return urllib.parse.urlunparse(pr._replace(query=urllib.parse.urlencode(d, doseq=True)))

source: urllib_parse_query_string.py

関連記事: Pythonで辞書の要素を削除するclear, pop, popitem, del

結果を確認。keyが存在しない場合は変化なし。

print(remove_query(url, 'tbm'))
# https://www.google.co.jp/search?q=%E6%A1%9C

print(remove_query(url, 'new-key'))
# https://www.google.co.jp/search?q=%E6%A1%9C&tbm=isch

source: urllib_parse_query_string.py

クエリ文字列をすべて削除する関数は以下の通り。

def remove_all_query(url):
    return urllib.parse.urlunparse(urllib.parse.urlparse(url)._replace(query=None))

print(remove_all_query(url))
# https://www.google.co.jp/search
