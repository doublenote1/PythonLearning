> Pythonでリスト(配列)の最大値・最小値から順に`n`個の要素を取得したい場合、
  `n=1`であれば、組み込み関数`max()`, `min()`、
  `n>1`であれば、リストをソート(並び替え)する方法と標準ライブラリの
  `heapq`モジュールを使う方法がある。

> 取得する要素の個数が多い場合は
  `sorted()`や`sort()`で先にソートするほうが効率的で、
  少ない場合は`heapq`モジュールの`nlargest()`, `nsmallest()`が効率的。

# 最大値・最小値を取得: max(), min()

> リストの最大値・最小値となる要素を取得するには
  組み込み関数`max()`, `min()`を使う。

```python
lst = [3, 6, 7, -1, 23, -10, 18]
print(max(lst))  # -> 23
print(min(lst))  # -> -10
```

# 最大値・最小値から順にn個の要素を取得: ソート

> リストの最大値・最小値から順に`n`個の要素を取得したい場合、
  まずリストをソート(並び替え)する方法がある。

> リストをソートするには、
  組み込み関数`sorted()`か、リストの`sort()`メソッドを使う。
> `sorted()`はソートされた新たなリストを返し、
  `sort()`は元のリストを並び替える。

> 昇順・降順を引数`reverse`で切り替え、
  先頭から任意の個数をスライスで選択すれば、
  リストの最大値・最小値から順に`n`個の要素を取得できる。
[関連記事](https://note.nkmk.me/python-list-sort-sorted/)
[関連記事](https://note.nkmk.me/python-slice-usage/)

```python
lst = [3, 6, 7, -1, 23, -10, 18]

lst_ascend = sorted(lst)
print(lst_ascend)  # -> [-10, -1, 3, 6, 7, 18, 23]
print(lst_ascend[:3])  # -> [-10, -1, 3]

lst_descend = sorted(lst, reverse=True)
print(lst_descend)  # -> [23, 18, 7, 6, 3, -1, -10]
print(lst_descend[:3])  # -> [23, 18, 7]

"一行にまとめて書いてもOK"

print(sorted(lst)[:3])  # -> [-10, -1, 3]
print(sorted(lst, reverse=True)[:3])  # -> [23, 18, 7]

"元のリストの順番が変わっても問題なければ、sort()メソッドでもよい"

print(lst)  # -> [3, 6, 7, -1, 23, -10, 18]

lst.sort()
print(lst[:3])  # -> [-10, -1, 3]
print(lst)  # -> [-10, -1, 3, 6, 7, 18, 23]

lst.sort(reverse=True)
print(lst[:3])  # -> [23, 18, 7]
print(lst)  # -> [23, 18, 7, 6, 3, -1, -10]
```

# 最大値・最小値から順にn個の要素を取得: heapqモジュール

> リストの最大値・最小値から順に`n`個の要素を取得したい場合、
  `heapq`モジュールを使う方法もある。
[Python ドキュメント](https://docs.python.org/ja/3/library/heapq.html)

> `heapq`モジュールの関数`nlargest()`, `nsmallest()`を使う。
  この場合、元のリストは変更されない。

> 第一引数に取得する要素の個数、
  第二引数に対象とするイテラブル(リストなど)を指定する。

```python
import heapq

lst = [3, 6, 7, -1, 23, -10, 18]

print(heapq.nlargest(3, lst))  # -> [23, 18, 7]
print(heapq.nsmallest(3, lst))  # -> [-10, -1, 3]
print(lst)  # -> [3, 6, 7, -1, 23, -10, 18]
```

> 最初に書いたように、取得する要素の個数が多い場合は
  `sorted()`や`sort()`で先にソートするほうが効率的で、
  少ない場合は`heapq`モジュールの`nlargest()`, `nsmallest()`が効率的。

# リンク

[](https://note.nkmk.me/python-max-min-heapq-nlargest-nsmallest/)
