# === リストオブジェクトの大小比較 ===

"""
Pythonにおけるリストオブジェクトの大小比較は、
最初の等しくない要素に対して行われる
"""

print([100] > [-100])
print([1, 2, 100] > [1, 2, -100])
print([1, 2, 100] > [1, 100])
print()

# === 2次元配列（リストのリスト）のソート ===

"""以下、sort() メソッドでも sorted() 関数でも同様"""

from pprint import pprint

def pp40(text):
    pprint(text, width=40)

l_2d = [[2, 30, 100], [1, 20, 300], [3, 10, 200]]
pp40(l_2d)

# 引数無
pp40(sorted(l_2d))

# 引数 key に無名関数（ラムダ式）を指定
pp40(sorted(l_2d, key=lambda x: x[1]))

# 引数 reverse で降順・昇順を指定
pp40(sorted(l_2d, reverse=True))
print()

# === 3次元以上の配列でも同様 ===

l_3d = [[[0, 1, 2], [2, 30, 100]], [[3, 4, 5], [1, 20, 300]],
        [[6, 7, 8], [3, 10, 200]]]
pp40(l_3d)
pp40(sorted(l_3d, key=lambda x: x[1][0]))
