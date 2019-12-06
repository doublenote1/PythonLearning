# ****** URLエンコード（パーセントエンコーディング）とは ******

"""
・URLエンコードは、URLで使用できない日本語（全角文字）やスペースなどの記号を使う際に行われる符号化（エンコード）。
・%xx の形に変換されるのでパーセントエンコーディングとも呼ばれる。

・例えば、Wikipediaの「日本語」のページは以下のようなURLになっている。
・https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E8%AA%9E
・この%E6%97%A5%E6%9C%AC%E8%AA%9Eの部分が「日本語」をURLエンコードした文字列。

・%E6%97%A5%E6%9C%AC%E8%AA%9Eを「日本語」に戻すことをURLデコードという。
・ブラウザのアドレスバーではURLデコードされて表示されている。
"""

# ****** URLエンコード: urllib.parse.quote()など ******

import urllib.parse

# === urllib.parse.quote() ===

# --- 基本的な使い方 ---

"""第一引数に文字列（str型）を渡すとURLエンコードされた文字列が返される。"""

s = '日本語'
s_quote = urllib.parse.quote(s)
print(s_quote)  # -> %E6%97%A5%E6%9C%AC%E8%AA%9E
print(type(s_quote))  # -> <class 'str'>

# --- バイト列を URL エンコード ---

"""
・第一引数にはバイト列（bytes型）を渡すことも可能。
・encode() メソッドでエンコードしたバイト列を例とする。
・デフォルトでは utf-8 でエンコードされる。
"""

s = '日本語'
b = s.encode()
print(b)  # -> b'\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e'
print(type(b))  # -> <class 'bytes'>
print(urllib.parse.quote(b))  # -> %E6%97%A5%E6%9C%AC%E8%AA%9E

# --- エンコーディングを指定: 引数encoding ---

"""
・第一引数に文字列を指定したとき、
  引数 encoding で 非ASCII文字をバイト列にエンコードする際に使われるエンコーディングを指定できる。
・デフォルトは'utf-8'。

・文字コードを指定して URL エンコードしたい場合は、この引数 encoding を使う。
"""

s_quote_sj = urllib.parse.quote(s, encoding='shift-jis')
print(s_quote_sj)  # -> %93%FA%96%7B%8C%EA

"""
元の文字列を encode() メソッドで該当のエンコーディングでエンコードした
バイト列を第一引数に指定するのと等価。
"""

b_sj_quote = urllib.parse.quote(s.encode('shift-jis'))
print(b_sj_quote)  # -> %93%FA%96%7B%8C%EA
print(s_quote_sj == b_sj_quote)  # -> True

# --- 変換しない文字を指定: 引数safe ---

"""デフォルトでは半角文字、数字、および '-', '_', '.', '/' は変換されない"""

print(urllib.parse.quote('http://x-y_z.com'))  # -> http%3A//x-y_z.com

"""
・引数 safe を指定することで変換されない文字を指定できる
・デフォルトで '/' が変換されないのは、引数 safe のデフォルト値が '/' だから。
・空文字列 '' を指定するとバックスラッシュ '/' も変換されるようになる。
・半角文字、数字、および '-', '_', '.' は safe によらず常に変換されない。
"""

print(urllib.parse.quote('http://x-y_z.com', safe=''))  # -> http%3A%2F%2Fx-y_z.com

"""複数の文字を指定する場合は '' の中にすべての文字を記述すれば OK"""

print(urllib.parse.quote('http://x-y_z.com', safe='/:'))  # -> http://x-y_z.com

# === urllib.parse.quote_plus() ===

"""
・urllib.parse.quote() と urllib.parse.quote_plus() は共通の引数を持ち、
  どちらもURLエンコードされた文字列を返す。
・違いは空白（スペース）の処理と引数 safe のデフォルト値。
・urllib.parse.quote() は空白（スペース）を %20 に変換し、
  引数 safe のデフォルト値は '/'、
・urllib.parse.quote_plus() は空白（スペース）を '+' に変換し、
  引数 safe のデフォルト値は ''（空文字列）。
"""

print(urllib.parse.quote('+ /'))  # -> %2B%20/
print(urllib.parse.quote_plus('+ /'))  # -> %2B+%2F
print(urllib.parse.quote_plus('+ /', safe='+/'))  # -> ++/

# === URLエンコードの活用法 ===

"""
・はじめに示したように、例えば Wikipedia（日本語版）の URL は
  https://ja.wikipedia.org/wiki/<ページ名>となっている。
・Wikipedia のページの URL は urllib.parse.quote() を使って以下のように作成できる。
"""

page_title = '日本語'
base_ja = 'https://ja.wikipedia.org/wiki/'
print(base_ja + urllib.parse.quote(page_title))
# -> https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E8%AA%9E

"""
・日本語部分（URLエンコードしたい部分）が分割されていない
  フルの URL の場合は引数 safe=':/'とすればOK
・デフォルトではコロン:も変換されてしまうので注意。
"""

full_url = 'https://ja.wikipedia.org/wiki/日本語'
print(urllib.parse.quote(full_url, safe=':/'))
# -> https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E8%AA%9E

"""
・Wikipedia の URL では、空白（半角スペース）はアンダースコア_で表されている。
・例えば「OK コンピューター」のページの URL は以下の通り。
・https://ja.wikipedia.org/wiki/OK_%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF%E3%83%BC
・urllib.parse.quote() では、空白（半角スペース）は %20 に変換される
"""

# --- クエリ文字列 ---

"""
・例えばGoogleの検索結果のURLは以下のようになっている。
https://www.google.co.jp/search?q=%E6%97%A5%E6%9C%AC%E8%AA%9E

・このq=<検索ワード>のような文字列（クエリ文字列）を作成するには
  urllib.parse.urlencode() を使うほうが簡単。
・URL エンコードも処理してくれる
"""

# ****** URLデコード: urllib.parse.unquote()など ******

# === urllib.parse.unquote() ===

# --- 基本的な使い方 ---

print(s_quote)  # -> %E6%97%A5%E6%9C%AC%E8%AA%9E
print(urllib.parse.unquote(s_quote))  # -> 日本語

# --- エンコーディングを指定: 引数encoding ---

"""
・URL デコードされたバイト列から文字列にデコードするときに使われる
  エンコーディングを引数 encoding に指定する
・デフォルトは 'utf-8'。

・元の文字列をバイト列にエンコードするときに
  utf-8 以外のエンコーディングを使っていた場合は、
  引数encodingを正しく指定しないと文字化けする。
"""

print(s_quote_sj)  # -> %93%FA%96%7B%8C%EA
print(urllib.parse.unquote(s_quote_sj))  # -> ���{��
print(urllib.parse.unquote(s_quote_sj, 'shift-jis'))  # -> 日本語

# === urllib.parse.unquote_plus() ===

"""
・urllib.parse.unquote_plus() は '+' を空白に置き換える。
・それ以外は urllib.parse.unquote() と同じ。
"""

print(urllib.parse.unquote('a+b'))  # -> a+b
print(urllib.parse.unquote_plus('a+b'))  # -> a b

# === urllib.parse.unquote_to_bytes() ===

"""
・URL デコードされたバイト列は urllib.parse.unquote_to_bytes() で取得できる。
・このバイト列を decode() メソッドでデコードすると
  urllib.parse.unquote() が返す文字列となる。
"""

b_unquote = urllib.parse.unquote_to_bytes(s_quote)
print(b_unquote)  # -> b'\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e'
print(b_unquote.decode())  # -> 日本語

"""
utf-8 以外のエンコーディングの場合は
decode() の引数でエンコーディングを指定する。
"""

b_unquote_sj = urllib.parse.unquote_to_bytes(s_quote_sj)
print(b_unquote_sj)  # -> b'\x93\xfa\x96{\x8c\xea'
print(b_unquote_sj.decode('shift-jis'))  # -> 日本語
