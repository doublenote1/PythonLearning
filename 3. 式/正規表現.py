import re

# === パターンにマッチするかを調べる ===

# 先頭からのパターンにマッチするか
# re.match(<正規表現>, <対象文字列>, [<フラグ>])

# 先頭からに限らず、パターンにマッチするか
# re.search(<正規表現>, <対象文字列>, [<フラグ>])

'''後述の match 部分は search に置換可能'''

s = 'aaa@xxx.com bbb@yyy.com ccc@zzz.com'

# --- マッチする場合 ---

# 最初にマッチした部分のマッチオブジェクトを取得
m = re.match(r'([a-z]+)@([a-z]+)', s, )
print(m)

# パターンにマッチした全体
print(m.group())
# パターンの()で囲まれた部分にマッチしたそれぞれの文字列のタプル
print(m.groups())
# パターンマッチの開始位置
print(m.start())
# パターンマッチの終了位置
print(m.end())
# 上記の start と end のタプル
print(m.span())

# --- マッチしない場合 ---

m = re.match('four', s)
print(m)

print()

# === マッチする部分の match オブジェクトをすべてイテレータで返す ===

# re.finditer(<正規表現>, <対象文字列>, [<フラグ>])

matches = re.finditer('([a-z]+)@([a-z]+)', s)
for match in matches:
    print(match.group(), end=' ')
    print(match.groups())
    print(match.span())
print()

# === マッチする部分すべてをリストで返す ===

# re.findall(<正規表現>, <対象文字列>, [<フラグ>])
'''()がなければマッチ全体をかえす'''

s = 'aaa@xxx.com bbb@yyy.com ccc@zzz.com'

print(re.findall('[a-z]+@[a-z]+\.com', s))
print(re.findall('(([a-z]+)@([a-z]+)\.com)', s))
print()

# === 文字列の、パターンでマッチした部分をすべて置換 ===

# re.sub(<正規表現>, <置換文字列>, <対象文字列>, [<最大置換回数>], [<フラグ>])

print(re.sub('[a-z]+@', 'ABC@', s, 2))
# サブマッチを使って置換
print(re.sub('([a-z]+)@', r'\1-123', s))

# 「置換後文字列」と「置換した文字列の数」のタプルを取得
# re.subn(<正規表現>, <置換文字列>, <対象文字列>, [<最大置換回数>], [<フラグ>])

print(re.subn('[a-z]*@', 'ABC@', s))

print()

# === パターンで文字列を分割したリストを返す ===

# re.split(<正規表現>, <対象文字列>, [<最大置換回数>], [<フラグ>])

print(re.split(' ', s))
print()

# === 正規表現オブジェクトをコンパイルする ===

# re.compile(<正規表現>, [<フラグ>])

p = re.compile('([a-z]+)@')
print(p.match(s))
print(p.findall(s))
print(p.sub(r'\1-123@', s))
print()

# === フラグ ===

'''
re.ASCII, re.A, (?a):
    \w 、\W 、\b 、\B 、\d 、\D 、\s 、\S に、ASCII 限定マッチングを行わせます

re.IGNORECASE, re.I, (?i):
    大文字・小文字を無視
    
re.MULTILINE, re.M, (?m):
    '^' は文字列・各行の先頭でマッチ
    '$' は文字列・各行の末尾でマッチ
    
re.DOTALL, re.S, (?s):
    '.' 特殊文字を、改行を含むあらゆる文字にマッチさせます
    
re.VERBOSE, re.X, (?x):
    空白(スペース・タブ・改行)は、無視されます。
'''

# re.ASCII

s = 'abcあいう,123１２３, 　'
print(re.findall(r'[\w\d\s]', s))
print(re.findall(r'(?a)[\w\d\s]', s, flags=re.ASCII))

print(re.findall(r'\w+\b', s))
print(re.findall(r'(?a)\w+\b', s))
print()

# re.IGNORE

s = 'abcDEF,ACBefg'
print(re.findall(r'[a-z]+', s))
print(re.findall(r'(?i)[a-z]+', s))
print()

# re.MULTILINE

s = '''\
abc
efg
xyz
'''
print(re.findall(r'^\w{3}', s))
print(re.findall(r'^\w{3}$', s))
print(re.findall(r'\w{3}$', s))
print(re.findall(r'(?m)^\w{3}', s))
print(re.findall(r'(?m)^\w{3}$', s))
print(re.findall(r'(?m)\w{3}$', s))
print()

# re.DOTALL

s = '''\
abc
efg
xyz
'''
print(re.findall(r'.+', s))
print(re.findall(r'(?s).+', s))
print()

# re.VERBOSE

files = r'''
    c:\folder\folder2\file.exe
    d:\file.txt
    *:\folder\folder4\file.exe
'''

file_path = re.compile(r'''(?xm)
    \b[a-zA-Z]:\\        # ドライブ
    (?:[\w-]+\\)*       # フォルダ
    [\w-]+\.[a-zA-Z]+\b  # ファイル
''')

print(file_path.findall(files))
