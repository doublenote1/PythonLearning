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

# === 括弧内はトークン間以外なら '\' が無くても自由に改行可能 ===

x = ('Put several strings within parentheses '
     'to have them joined together.')
print(x)

x = (1 + 2
     + 3)
print(x)

print()
