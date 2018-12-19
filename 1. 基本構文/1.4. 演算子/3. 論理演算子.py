# 1. bool型の論理演算

print(True and True)  # -> True
print(False and False)  # -> False
print(True and False)  # -> False
print()

print(True or True)  # -> True
print(False or False)  # -> False
print(True or False)  # -> True
print()

print(not True)  # -> False
print(not False)  # -> True
print()

print(True and True and True)  # -> True
print(False or True and True)  # -> True
print()

# 2. bool型以外の論理演算

"""
式 x and y は、まず x を評価します
x が偽なら x の値を返します
それ以外の場合には、 y の値を評価し、その結果を返します。

式 x or y は、まず x を評価します
x が真なら x の値を返します
それ以外の場合には、 y の値を評価し、その結果を返します。

+---+---+-------+---------+--------+
|   x   |   y   | x and y | x or y |
+-------+-------+---------+--------+
| True  | False |    y    |    x   |
+-------+-------+---------+--------+
| False | True  |    x    |    y   |
+-------+-------+---------+--------+
| True  | True  |    y    |    x   |
+-------+-------+---------+--------+
| False | False |    x    |    y   |
+-------+-------+---------+--------+
"""

print(10 and 100)  # -> 100
print(100 and 10)  # -> 10
print(10 or 100)  # -> 10
print(100 or 10)  # -> 100
print()

print(0 and 0.0)  # -> 0
print(0.0 and 0)  # -> 0.0
print(0 or 0.0)  # -> 0.0
print(0.0 or 0)  # -> 0
print()

print(0 and 1)  # -> 0
print(1 and 0)  # -> 0
print(0 or 1)  # -> 1
print(1 or 0)  # -> 1
print()

def func(text):
    return text

print(True and func('True and func()'))  # -> True and func()
print(False and func('False and func()'))  # -> False
print(True or func('True or func()'))  # -> True
print(False or func('False or func()'))  # -> False or func()
