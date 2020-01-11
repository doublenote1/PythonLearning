> `map()`は、リストなどの各要素に指定関数の処理を適用し、
  イテレータを返す組み込み関数。

`iterator = map(function, iterable, ...)`

---------------------------------------------------------------------------

> リストがほしいときは`list()`で囲む。
> `map()`ではなくリスト内包表記を使ってもいい。

```python
"=== 文字列を`split()`で分割してから`int()`で整数に変換する例 ==="

i = '1 2 3'

print(map(int, i.split(' ')))  # -> <map object at 0x0000016AF6557E20>
print(type(map(int, i.split(' '))))  # -> <class 'map'>
print(list(map(int, i.split(' '))))  # -> [1, 2, 3]

"リスト内包表記でも表現できる"
print([int(x) for x in i.split(' ')])  # -> [1, 2, 3]

"引数<function>にlambdaを使う"
print(list(map(lambda x: int(x) ** 2, i.split(' '))))  # -> [1, 4, 9]


"=== リストの各要素を`split()`で分割してから`int()`で整数に変換する例 ==="

lst_2d = ['1 2 3', '4 5 6', '7 8 9']

input_array = []
for data in lst_2d:
    input_array.append(list(map(int, data.split(' '))))
print(input_array)  # -> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"リスト内包表記でも表現できる"
input_array = []
for data in lst_2d:
    input_array.append([int(x) for x in data.split(' ')])
print(input_array)  # -> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"引数<function>にlambdaを使う"
input_array = []
for data in lst_2d:
    input_array.append(list(map(lambda x: int(x) ** 2, data.split(' '))))
print(input_array)  # -> [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
```

# リンク

[note.nkmk.me](https://note.nkmk.me/python-map-list-iterator/)
