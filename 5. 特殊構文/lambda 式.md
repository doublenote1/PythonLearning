> Pythonでは`def文`で関数を定義するが、
  `lambda(ラムダ式)`で名前を持たない「無名関数」を作成することもできる。
> `lambda`は引数として関数を指定する場合などに使うと便利。

# 「def文」と「lambda式」の対応関係

> `def文`による「関数定義」とそれに相当する「ラムダ式での無名関数」の
  対応関係は以下のようになる。


> 関数定義

`def <関数名>(<仮引数>, ...):
    return <仮引数を含む式(戻り値)>`

`<関数名> = lambda <仮引数>, ...: <仮引数を含む式(戻り値)>`

> 関数定義・呼出

`def <関数名>(<仮引数>, ...):
    return <仮引数を含む式(戻り値)>
<関数名>(<実引数>, ...)`

`(lambda <仮引数>, ...: <仮引数を含む式(戻り値)>)(<実引数>, ...)`


> 具体的には以下のようになる。
  この例のようにデフォルト引数を指定することもできる。

```python
"関数定義"

def add_def(a, b=1):
    return a + b

print(add_def(3, 4))  # -> 7
print(add_def(3))  # -> 4

"ラムダ式"

add_lambda = lambda a, b=1: a + b
print(add_lambda(3, 4))  # -> 7
print(add_lambda(3))  # -> 4

print((lambda a, b=1: a + b)(3, 4))  # -> 7
print((lambda a, b=1: a + b)(3))  # -> 4
```

# lambda式でif文を使う

> ラムダ式では複数行にまたがる文を使うことはできないが、
  if文に相当する三項演算子は使用可能。

```python
get_odd_even = lambda x: 'even' if x % 2 == 0 else 'odd'

print(get_odd_even(3))  # -> odd
print(get_odd_even(4))  # -> even
```

# PEP8ではlambda式には名前を付けないのが推奨

> ラムダ式に名前を割り当てる(ラムダ式を変数に代入する)と
  Pythonのコーディング規約PEP8の自動チェックツールなどで
  「Warning」が出ることがある。
  `Do not assign a lambda expression, use a def (E731)`

> ラムダ式は呼び出し可能なオブジェクトを引数で渡すときなどに
  名前を付けずに使うためのもので、
  名前を付けて関数を定義する場合は`def`を使うべき、
  というのがPEP8の考え方。

# lambda式の具体的な使い方・活用例

## 「sorted」関数等の「key引数」に指定

> リストをソートする組み込み関数`sorted()`やリストのメソッド`sort()`、
  最大値や最小値を返す組み込み関数`max()`や`min()`には「key引数」がある。
> 「key引数」には、ソートや最大値・最小値の算出の前に(各要素が比較される前に)
  リストの各要素に適用される関数を指定する。

```python
"=== 「sorted()関数」の例 ==="

lst = ['Mick', 'Bob', 'Alice']

"文字列のリストは、デフォルトではアルファベット順にソートされる。"
print(sorted(lst))  # -> ['Alice', 'Bob', 'Mick']

"文字数が少ない順(昇順)にソート(key引数にlen()関数を指定)"
print(sorted(lst, key=len))  # -> ['Bob', 'Mick', 'Alice']

"""事前に定義した関数を「key引数」で指定すると、
各要素をその関数に引数として渡した時の戻り値によってソートする"""
def sec_char(text):
    "文字列の2番目の文字を返す"
    return text[1]

print(sorted(lst, key=sec_char))  # -> ['Mick', 'Alice', 'Bob']

"上記と同じことをラムダ式で行うと下記コードになる"
print(sorted(lst, key=lambda x: x[1]))  # -> ['Mick', 'Alice', 'Bob']

"=== 「max()関数」の例 ==="

print(max(lst))  # -> Mick
print(max(lst, key=len))  # -> Alice
def sec_char(text):
    return text[1]

print(max(lst, key=sec_char))  # -> Bob
print(max(lst, key=lambda x: x[1]))  # -> Bob
```

## 「map()」や「filter()」の第一引数に指定

> リストの各要素に対して関数を適用する組み込み関数`map()`や、
  条件を満たす要素のみ抽出する組み込み関数`filter()`では、
  第一引数に関数、第二引数にリストなどのイテラブルオブジェクトを指定する。

> 任意の関数を指定したい場合、`def`文で関数を定義するより
  ラムダ式で無名関数を指定したほうが簡潔に書ける。

> `map()`・`filter()`関数はイテレータを返す

> なお、`map()`関数や`filter()`関数と同様の処理は
  リスト内包表記やジェネレータ式(ジェネレータ内包表記)でも書ける。

### 「map()」関数の例

> `map()`関数の例として、第一引数に値を二乗するラムダ式を指定する。

`iterator = map(function, iterable, ...)`

```python
lst = [0, 1, 2, 3]

"map()関数"
map_square = map(lambda x: x**2, lst)
print(type(map_square))  # -> <class 'map'>
print(list(map_square))  # -> [0, 1, 4, 9]

"リスト内包表記"
lst_square = [x ** 2 for x in lst] 
print(type(lst_square))  # -> <class 'list'>
print(lst_square)  # -> [0, 1, 4, 9]

"ジェネレータ内包表記"
g_square = (x**2 for x in lst)
print(type(g_square))  # -> <class 'generator'>
print(list(g_square))  # -> [0, 1, 4, 9]
```

### 「filter()」関数の例

`iterator = filter(function, iterable)`

> `filter()`関数の例として、第一引数に偶数を`True`とするラムダ式を指定する。

```python
lst = [0, 1, 2, 3]

"filter()関数"
filter_even = filter(lambda x: x % 2 == 0, lst)
print(type(filter_even))  # -> <class 'filter'>
print(list(filter_even))  # -> [0, 2]

"リスト内包表記"
lst_even = [x for x in lst if x % 2 == 0]
print(type(lst_even))  # -> <class 'list'>
print(list(lst_even))  # -> [0, 2]

"ジェネレータ内包表記"
g_even = (x for x in lst if x % 2 == 0)
print(type(g_even))  # -> <class 'generator'>
print(list(lst_even))  # -> [0, 2]g
```

# リンク

[](https://note.nkmk.me/python-lambda-usage/)
