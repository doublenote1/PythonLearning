import pprint  # pretty print の略

lst = [{'Name': 'Alice XXX', 'Age': 40, 'Points': [80, 20]},
     {'Name': 'Bob YYY', 'Age': 20, 'Points': [90, 10]},
     {'Name': 'Charlie ZZZ', 'Age': 30, 'Points': [70, 30]}]

# === print() ===

print(lst)
print()

# === pprint() ===

# --- 整形された文字列で print() ---

# 引数無
pprint.pprint(lst)
print()

# 出力幅の指定(デフォルト = 80)
pprint.pprint(lst, width=40)
print()

# 出力する要素の深さの指定より大きい場合、
# '...'で省略(デフォルト = None)
pprint.pprint(lst, depth=2)
print()

# インデント幅を指定(デフォルト = 1)
pprint.pprint(lst, indent=4, width=40)
print()

# 改行を最小限にする('width' に収まらない分のみ改行)

lst_long = [list(range(10)), list(range(100, 110))]

pprint.pprint(lst_long, width=40)
print()
pprint.pprint(lst_long, width=40, compact=True)
print()

# --- 整形された文字列を取得 ---

s_pp = pprint.pformat(lst)
print(s_pp)
