> Pythonの組み込み関数`zip()`は複数のイテラブルオブジェクト
  (リストやタプルなど)の要素をまとめる関数。
> forループで複数のリストの要素を取得する際などに使う。

# 基本

`zip型 = zip(*iterables)`

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]
points = [100, 85, 90]

print(zip(names, ages, points))  # -> <zip object at 0x000001DAE1AE9588>
print(type(zip(names, ages, points)))  # -> <class 'zip'>
print(list(zip(names, ages, points)))
# -> [('Alice', 24, 100), ('Bob', 50, 85), ('Charlie', 18, 90)]

"2つのイテラブルで回す"
for name, age in zip(names, ages):
    print(name, age)
# -> Alice 24
# -> Bob 50
# -> Charlie 18

"3つ以上のイテラブルで回す事も可能"
for name, age, point in zip(names, ages, points):
    print(name, age, point)
# -> Alice 24 100
# -> Bob 50 85
# -> Charlie 18 90
```

# 回すイテラブルの要素数が異なる場合

## 多い分の要素を無視

> `zip()`関数では、それぞれのリストの要素数が異なる場合、
  少ない(短い)方の要素数までが返され、多い分は無視される。

```python
names = ['Alice', 'Bob', 'Charlie', 'Dave']
ages = [24, 50, 18]

for name, age in zip(names, ages):
    print(name, age)
# -> Alice 24
# -> Bob 50
# -> Charlie 18
```

## 足りない要素をすべて同じ値で埋める

> 標準ライブラリ`itertools`モジュールの`zip_longest()`を使うと、
  それぞれのリストの要素数が異なる場合に、
  足りない要素を任意の値で埋めることができる。
> デフォルトでは`None`で埋められる。

`itertools.zip_longest(*iterables, fillvalue=None)`

```python
import itertools

names = ['Alice', 'Bob', 'Charlie', 'Dave']
ages = [24, 50]

print(itertools.zip_longest(names, ages))
# -> <itertools.zip_longest object at 0x000001DAE19EA728>
print(type(itertools.zip_longest(names, ages)))
# -> <class 'itertools.zip_longest'>
print(list(itertools.zip_longest(names, ages)))
# -> [('Alice', 24), ('Bob', 50), ('Charlie', None), ('Dave', None)]

for name, age in itertools.zip_longest(names, ages):
    print(name, age)
# -> Alice 24
# -> Bob 50
# -> Charlie None
# -> Dave None

"「fillvalue引数」を指定するとその値で埋められる"
for name, age in itertools.zip_longest(names, ages, fillvalue=20):
    print(name, age)
# -> Alice 24
# -> Bob 50
# -> Charlie 20
# -> Dave 20

"""要素が足りないリストが複数ある場合も埋める値は一律。
別々の値を指定することはできない。"""

names = ['Alice', 'Bob', 'Charlie', 'Dave']
ages = [24, 50]
points = [100, 85]

for name, age, point in itertools.zip_longest(
    names, ages, points, fillvalue=20
):
    print(name, age, point)
# -> Alice 24 100
# -> Bob 50 85
# -> Charlie 20 20
# -> Dave 20 20
```

## 足りない要素をイテラブルごとの値で埋める

> `zip_longest()`の中でさらに`zip_longest()`を使えば
  別の値を指定することも可能だが、
  前もってどのリストの要素が足りないか分かっている必要があるので
  実用的ではない。

> 要素数が不明の複数のリストをそれぞれ別の値で埋めたい場合は、
    1. すべてのリストに対して埋める値を定義しておく
    2. 最大の要素数を取得する
    3. すべてのリストを最大の要素数まで埋める
    4. `zip()`関数を使う
  といった手順が考えられる。

```python
names = ['Alice', 'Bob', 'Charlie', 'Dave']
ages = [24, 50, 18]
points = [100, 85]

"1. デフォルト値の定義"
fill_name = 'XXX'
fill_age = 20
fill_point = 50

len_names = len(names)
len_ages = len(ages)
len_points = len(points)

"2. 最大の要素数を取得"
max_len = max(len_names, len_ages, len_points)

"""3. すべてのリストに、
最大要素数に足りない数のデフォルト値のリストを結合させる"""
names = names + [fill_name] * (max_len - len_names)
ages = ages + [fill_age] * (max_len - len_ages)
points = points + [fill_point] * (max_len - len_points)
print(names)  # -> ['Alice', 'Bob', 'Charlie', 'Dave']
print(ages)  # -> [24, 50, 18, 20]
print(points)  # -> [100, 85, 50, 50]

"4. `zip()`関数を使う"
for name, age, point in zip(names, ages, points):
    print(name, age, point)
# -> Alice 24 100
# -> Bob 50 85
# -> Charlie 18 50
# -> Dave 20 50
```

> これを関数化すると以下のようになる。
  元のリストとリストを埋める値をそれぞれイテラブルで
  引数に指定するようにしている。

```python
def my_zip_longest(iterables, fillvalues):
    max_len = max(len(i) for i in iterables)
    return zip(*[list(i) + [v] * (max_len - len(i)) for i, v in zip(iterables, fillvalues)])

names = ['Alice', 'Bob', 'Charlie', 'Dave']
ages = [24, 50, 18]
points = [100, 85]

for name, age, point in my_zip_longest((names, ages, points), ('XXX', 20, 50)):
    print(name, age, point)
# Alice 24 100
# Bob 50 85
# Charlie 18 50
# Dave 20 50
```

