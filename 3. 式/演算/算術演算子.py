# ****** 算術演算 ******

print(2 + 3.0)  # float を含むと 結果は float
print(17 / 3)  # '/' は常に浮動小数点を返す
print(9 / 3)
print(17 // 3)  # 商
print(17 % 3)  # 余り
print(2 ** 7)  # 階乗
print(2 + 5 * 3)  # 優先順位有り
print(4 * 3.75 - 1)  # 複数の型の計算
print()

# === 割り算の商と余りを同時に取得 ===

'''(a // b, a % b)のタプルを返す'''

q, mod = divmod(10, 3)
print(q, mod)

answer = divmod(10, 3)
print(answer)
print(answer[0], answer[1])
print()

