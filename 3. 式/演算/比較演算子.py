# === 比較演算 ===

print(0 < 1)  # -> True
print(0 <= 1)  # -> True
print(0 > 1)  # -> False
print(0 >= 1)  # -> False
print(0 < 1 < 2)  # -> True
print(0 >= 1 >= 2)  # -> False
print()
print(0 == 1)  # -> False
print(0 == 0 == 0)  # -> True
print(0 != 1)  # -> True
print(0 != 1 != 0)  # -> True
print()
print(10 == 10.0)  # -> True
print(10 is 10.0)  # -> False
print(10 != 10.0)  # -> False
print(10 is not 10.0)  # -> True
print()
print(0 in [1, 2, 3])  # -> False
print(0 not in [1, 2, 3])  # -> True
print('a' in 'abc')  # -> True
print('a' not in 'abc')  # -> False
print()
print((1, 2, 3) < (1, 2, 4))  # -> True
print([1, 2, 3] < [1, 2, 4])  # -> True
print('ABC' < 'C' < 'Pascal' < 'Python')  # -> True
print((1, 2, 3, 4) < (1, 2, 4))  # -> True
print((1, 2) < (1, 2, -1))  # -> True
print((1, 2, 3) == (1.0, 2.0, 3.0))  # -> True
print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))  # -> True

'''
+------------+------------------------------------------+
|   演算子   |               結果                       |
+------------+------------------------------------------+
| x < y      | x が y より小さければ True               |
+------------+------------------------------------------+
| x <= y     | x が y より小さいか等しければ True       |
+------------+------------------------------------------+
| x > y      | x が y より大きければ True               |
+------------+------------------------------------------+
| x >= y     | x が y より大きいか等しければ True       |
+------------+------------------------------------------+
| x == y     | x と y の値が等しければ True             |
+------------+------------------------------------------+
| x != y     | x と y の値が等しくなければ True         |
+------------+------------------------------------------+
| x is y     | x と y が同じオブジェクトであれば True   |
+------------+------------------------------------------+
| x is not y | x と y が同じオブジェクトでなければ True |
+------------+------------------------------------------+
| x in y     | x が y に含まれていれば True             |
+------------+------------------------------------------+
| x not in y | x が y に含まれていなければ True         |
+------------+------------------------------------------+
'''

# === bool 型以外のオブジェクトのブール値 ===

'''
False 型:
    bool型のFalse
    None
    数値（int型やfloat型）の0, 0.0
    空の文字列''
    空のコンテナ（リスト、タプル、辞書など）[], (), {},
True 型:
    上記以外
'''

print(bool(True))  # -> True
print(bool(False))  # -> False
print()
print(bool(None))  # -> False
print(bool(0))  # -> False
print(bool(0.0))  # -> False
print(bool(''))  # -> False
print(bool([]))  # -> False
print(bool(()))  # -> False
print(bool({}))  # -> False
print()
print(bool(1))  # -> True
print(bool(1.0))  # -> True
print(bool('False'))  # -> True
print(bool([None]))  # -> True
print(bool((None,)))  # -> True
print(bool({None}))  # -> True


