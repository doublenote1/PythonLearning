> `enumerate()`関数を使うと、
  forループの中でリスト(配列)などのイテラブルオブジェクトの要素と同時に
  インデックス番号(カウント、順番)を取得できる。

`enumerate型 = enumerate(iterable, start=0)`

>` enumerate()`関数が返すオブジェクトは`enumerate型`"

```python
names = ['Alice', 'Bob', 'Charlie']
print(enumerate(names))  # -> <enumerate object at 0x000002898890E5E8>
print(type(enumerate(names)))  # -> <class 'enumerate'>
print(list(enumerate(names)))
# -> [(0, 'Alice'), (1, 'Bob'), (2, 'Charlie')]
```

```python
names = ['Alice', 'Bob', 'Charlie']

"=== range関数でインデックスと要素を取得する場合 ==="

for i in range(len(names)):
    print(i, names[i])
# -> 0 Alice
# -> 1 Bob
# -> 2 Charlie

"=== enumerate関数でインデックスと要素を取得する場合 ==="

"ターンごとにタプルとして取得"
for tpl in enumerate(names):
    print(tpl[0], tpl[1])
# -> 0 Alice
# -> 1 Bob
# -> 2 Charlie

"for文内で、上記のタプルからそれぞれの変数へ展開し取得"
for i, name in enumerate(names):
    print(i, name)
# -> 0 Alice
# -> 1 Bob
# -> 2 Charlie

"開始位置(start)を指定"
for i, name in enumerate(names, 1):
    print(i, name)
# -> 1 Alice
# -> 2 Bob
# -> 3 Charlie

"増分(step)を指定"
step = 3
for i, name in enumerate(names):
    print(i * step, name)
# -> 0 Alice
# -> 3 Bob
# -> 6 Charlie
```
