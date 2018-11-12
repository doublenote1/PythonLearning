# ****** 数値型 ******

print(2 + 3.0)  # float を含むと 結果は float
print(17 / 3)  # '/' は常に浮動小数点を返す
print(9 / 3)
print(17 // 3)  # 商
print(17 % 3)  # 余り
print(2 ** 7)  # 階乗
print(2 + 5 * 3)  # 優先順位有り
print(4 * 3.75 - 1)  # 複数の型の計算
print()

# ****** 文字列型 ******

# === エスケープシーケンス ===

# \\         : '\' 文字そのもの
# \'         : シングルクオーテーション
# \"         : ダブルクオーテーション
# \a         : ベル
# \b         : バックスペース
# \f         : 改ページ
# \r         : キャリッジリターン
# \n         : 改行
# \t         : 水平タブ
# \v         : 垂直タブ
# \N{name}   : Unicode データベース中で名前 name を持つ文字
# \uxxxx     : 16ビットの16進数値xxxxを持つUnicode文字
# \Uxxxxxxxx : 32ビットの16進数値xxxxxxxxを持つUnicode文字
# \ooo       : 8進数oooを持つASCII文字
# \xhh       : 16進数hhを持つASCII文字
# \0         : NULL

# === 文字列演算 ===

print('Py' + 3 * 'Thon')
print()

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
