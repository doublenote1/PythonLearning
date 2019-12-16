`range型 = range(stop)`
`range型 = range(start, stop[, step])`

```python
"range()はrange型オブジェクトを返す"
print(range(3))  # -> range(0, 3)
print(type(range(3)))  # -> <class 'range'>
print(list(range(3)))  # -> [0, 1, 2]

"for文で使う際にはリストに変換する必要はない"
for i in range(3):
    print(i)
# -> 0
# -> 1
# -> 2
```

# 0から任意の値までの連番(0 ≦ i < stop)

```python
print(list(range(3)))  # -> [0, 1, 2]

"0始まりで1ずつ増加する連番なので、負の値を指定すると空になる。"
print(list(range(-3)))  # -> []
```

# 任意の範囲の連番(start ≦ i < stop)

```python
print(list(range(3, 10)))  # -> [3, 4, 5, 6, 7, 8, 9]
print(list(range(-3, 3)))  # -> [-3, -2, -1, 0, 1, 2]

"1ずつ増加する連番なので、stop ≦ startのときは空となる。"
print(list(range(10, 3)))  # -> []
print(list(range(3, -3)))  # -> []

"第一引数startを0としたrange(0, stop)はrange(stop)と等価。"
print(range(0, 3) == range(3))  # -> True
```

# 任意の範囲、増分の等差数列(start ≦ i < stopでstepずつ増加)

```python
"引数stepに負の値を指定すると減少していく。"
print(list(range(3, 10, 2)))  # -> [3, 5, 7, 9]
print(list(range(10, 3, -2)))  # -> [10, 8, 6, 4]

"""stepが正の値の場合のstop ≦ startのときや、
stepが負の値の場合のstart ≦ stopのときに空となる"""
print(list(range(10, 3, 2)))  # -> []
print(list(range(3, 10, -2)))  # -> []

"第三引数stepを1としたrange(start, stop, 1)はrange(start, stop)と等価。"
print(range(3, 10, 1) == range(3, 10))  # -> True
"""さらに第一引数startを0としたrange(0, stop, 1)は
range(0, stop)およびrange(stop)と等価"""
print(range(0, 10, 1) == range(0, 10) == range(10))  # -> True
```

# 「reversed()」で逆順を指定

> 第三引数`step`に負の値を指定すれば
  減少する連番および等差数列が生成できるので、
  任意の`range()`の逆順を生成することが可能だが、
  `start`, `stop`と合わせて適切な値を指定する必要があるため面倒。

```python
print(list(range(3, 10, 2)))  # -> [3, 5, 7, 9]
print(list(range(9, 2, -2)))  # -> [9, 7, 5, 3]
```

> 組み込み関数`reversed()`を使うと結果をそのまま逆順にできる。

    todo: link: Pythonでリストや文字列を逆順に並べ替え（reverse, reversed）

```python
print(list(reversed(range(3, 10, 2))))  # -> [9, 7, 5, 3]

"reversed()の場合も、for文で使う場合はlist()は不要"
for i in reversed(range(3, 10, 2)):
    print(i)
# -> 9
# -> 7
# -> 5
# -> 3
```

# 浮動小数点数の場合

> これまでの例のように、`range()`の引数に指定できるのは整数のみ
> 浮動小数点数floatを指定するとエラーになる。

```python
try:
    print(list(range(0.3, 1.0, 0.2)))
except TypeError as e:
    print(e)  # -> 'float' object cannot be interpreted as an integer
```

> 浮動小数点数の等差数列を生成したい場合はリスト内包表記を使う
[](../5.%20特殊構文/内包表記.md)

```python
print([i / 10 for i in range(3, 10, 2)])  # -> [0.3, 0.5, 0.7, 0.9]
```

> 浮動小数点数との積を使うと誤差が生じる場合がある。
  これは`round()`で丸められる。
[](../3.5.%20基本データ型/1.%20数値型/2.%20端数処理.md)

```python
print([i * 0.1 for i in range(3, 10, 2)])
# -> [0.30000000000000004, 0.5, 0.7000000000000001, 0.9]
print([round(i * 0.1, 1) for i in range(3, 10, 2)])
# -> [0.3, 0.5, 0.7, 0.9]
```

> `NumPy`を使える環境であれば、`np.arange()`を使うほうが簡単。
  `np.arange()`の引数の指定は`range()`と同じで、浮動小数点数を指定可能。

```python
import numpy as np

print(np.arange(3))  # -> [0 1 2]
print(np.arange(3, 10))  # -> [3 4 5 6 7 8 9]
print(np.arange(3, 10, 2))  # -> [3 5 7 9]
print(np.arange(0.3, 1.0, 0.2))  # -> [0.3 0.5 0.7 0.9]
```
