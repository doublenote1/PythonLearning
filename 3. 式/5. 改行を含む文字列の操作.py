# === 改行を含む文字列の取得 ===

# --- 三連引用符 ---

s = """\
Line1
Line2
Line3\
"""
print(s)
print()

# --- コード上にインデントをつけたい場合 ---

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

# --- 文字列中にインデントを加えたい場合

s = """\
Line1
    Line2
        Line3\
"""
print(s)
print()

s = 'Line1\n' \
    '    Line2\n' \
    '        Line3'
print(s)
print()

s = (
    'Line1\n'
    '    Line2\n'
    '        Line3'
)
print(s)
print()

# === 文字列とリストの相互変換 ===

# 文字列のリストを改行して連結

lst = ['Line1', 'Line2', 'Line3']
s = '\n'.join(lst)
print(s)
print()

# 文字列を改行ごとにリスト要素へ分割

s = 'Line1\nLine2\r\nLine3'
lst = s.splitlines()
print(lst)
print()

# === 改行コードの削除、置き換え ===

s = 'Line1\nLine2\r\nLine3'

# --- 削除 ---

s_new = ''.join(s.splitlines())
print(s_new)

# --- 置き換え ---

s_new = ' '.join(s.splitlines())
print(s_new)

s_new = ','.join(s.splitlines())
print(s_new)

s_new = '\r\n'.join(s.splitlines())
print(s_new)
