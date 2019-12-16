> Python3.0以降では関数アノテーション(Function Annotations)という仕組み
  によって、関数の引数や返り値にアノテーション(注釈)となる式を
  記述することができる。

  [関数定義](https://docs.python.org/ja/3/reference/compound_stmts.html#function-definitions)

> さらに、関数アノテーションに型情報を書く場合(型アノテーション)の記述方法
  がPEP484で規定され、それを実現するためにPython3.5で暫定的に
  標準ライブラリに`typing`モジュールが追加された。

  [typing — 型ヒントのサポート](https://docs.python.org/ja/3/library/typing.html)

> 関数の説明はdocstringに記述することもできる。以下の記事を参照。

  [](「ドキュメンテーション文字列」の書き方.md)

> 関数アノテーションとdocstringは二者択一ではなく、
  型は関数アノテーション、詳しい説明文はdocstringというように併用して
  記述する例が多い。

# 関数アノテーションの書き方

## 通常の関数

> アノテーションを含まない通常の関数は以下の通り。

```python
def func(x, y):
    return x * y

print(func('abc', 3))  # -> abcabcabc
print(func(4, 3))  # -> 12
```

## 関数アノテーション

> 関数アノテーションは以下のように記述する。

> 引数名のあとの`: <式>`がそれぞれの引数に対するアノテーション(注釈)、
  括弧と末尾のコロン`:`の間の`-> <式>`が返り値に対するアノテーションとなる。
> アノテーションを記述するものと記述しないものが混在していても問題ない。

> 関数としての使い方は通常の関数と同じ。

```python
def func_annotations(x: 'description-x', y: 'description-y') -> 'description-return':
    return x * y

print(func_annotations('abc', 3))  # -> abcabcabc
print(func_annotations(4, 3))  # -> 12
```

> デフォルト引数はアノテーションのあとに記述する。

```python
def func_annotations_default(x: 'description-x', y: 'description-y' = 3) -> 'description-return':
    return x * y

print(func_annotations_default('abc'))  # -> abcabcabc
print(func_annotations_default(4))  # -> 12
```

## 関数アノテーションはあくまでもただの注釈

> 関数アノテーションはあくまでも引数や返り値に対する注釈で、
  それをもとに特別な処理が行われることはない。

> 例えば、アノテーションとして型を指定することもできるが、
  実行時に型チェックが行われたりはしないので
  アノテーションで指定した型以外の引数を渡しても
  何も起こらない(エラーにならない)。

```python
def func_annotations_type(x: str, y: int) -> str:
    return x * y

print(func_annotations_type('abc', 3))  # -> abcabcabc
print(func_annotations_type(4, 3))  # -> 12
```

# __annotations__ 属性

> 関数アノテーションは`__annotations__`属性に
  辞書として格納されている。

> 引数に対するアノテーションは辞書のキーが引数名、
  返り値に対するアノテーションはキーが`return`となる。

```python
def func_annotations(x: 'description-x', y: 'description-y') -> 'description-return':
    return x * y

print(type(func_annotations.__annotations__))  # -> <class 'dict'>
print(func_annotations.__annotations__)
# {'x': 'description-x', 'y': 'description-y', 'return': 'description-return'}
print(func_annotations.__annotations__['x'])  # -> description-x
```

# 型ヒント(Type Hints)

> PEP3107の関数アノテーション(Function Annotations)では
  アノテーション(注釈)に何を書くかは定義されていない。

> PEP484で関数アノテーションに型を書く場合(型アノテーション)の
  標準の記述方法が新たに規定され、
  それを実現するためにPython3.5で暫定的に標準ライブラリに
  `typing`モジュールが追加された。

  [typing — 型ヒントのサポート](https://docs.python.org/ja/3/library/typing.html)

> あくまでも「型をアノテーションとして書く場合にはこのように書きましょう」
  という規定であって、型アノテーションを書くことは必須ではなく、
  型以外の情報をアノテーションとして書くことも認められている。

> また、上述のようにアノテーションはただの注釈に過ぎないので、
  型ヒントを利用するライブラリやIDE、エディタなどを使わない限り
  型チェックなどは行われない。

> `typing`モジュールを利用すると、例えば以下のように型アノテーションを書ける。リストの要素の型の指定や、複数の型のいずれかといった指定が可能になった。

```python
from typing import Union, List

def func_u(x: List[Union[int, float]]) -> float:
    return sum(x) ** 0.5

print(func_u([0.5, 9.5, 90]))
# 10.0
```

> `List[X]`: 要素の型がXのリスト(list)
  `Union[X, Y]`: XかYいずれかの型
  `Any`: 任意の型
  `Callable[[X ...], Y]]`: 引数の型のリストが[X ...]、
                           返り値の型がYの呼び出し可能オブジェクト
  `Dict[X, Y]`: キーの型がX, 値の型がYの辞書(dict)
などが使える。

# リンク

[](https://note.nkmk.me/python-function-annotations-typing/)
