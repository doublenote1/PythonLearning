> Python標準ライブラリのrandomモジュールの関数
  choice(), sample(), choices()を使うと、
  リストやタプル、文字列などのシーケンスオブジェクトから
  ランダムに要素を選択して取得(ランダムサンプリング)できる。

> choice()は要素を一つ取得、sample(), choices()は複数の要素を
  リストで取得できる。
  sample()は重複なしの非復元抽出、choices()は重複ありの復元抽出。
[Python ドキュメント](https://docs.python.org/ja/3/library/random.html)

> ランダムではなく任意の条件で要素を抽出したい場合は以下の記事を参照。
[](リスト(配列)の特定の要素を抽出、置換、変換.md)

> リストの要素をランダムに並べ替えたい場合や、
  乱数やそのリスト自体を生成したい場合は以下の記事を参照。
[関連記事](https://note.nkmk.me/python-random-shuffle/)
[関連記事](https://note.nkmk.me/python-random-randrange-randint/)

# ランダムに要素を一つ選択: random.choice()

> randomモジュールの関数choice()で、
  リストからランダムで要素が一つ選択され取得できる。
[Python ドキュメント](https://docs.python.org/ja/3/library/random.html#random.choice)

```python
import random

lst = [0, 1, 2, 3, 4]
print(random.choice(lst))  # -> 0

"タプルや文字列でも同様。文字列の場合は一文字が選択される"

print(random.choice(('xxx', 'yyy', 'zzz')))  # -> yyy
print(random.choice('abcde'))  # -> b

"空のリストやタプル、文字列を引数として指定するとエラー"

# print(random.choice([]))
# IndexError: Cannot choose from an empty sequence
```

# ランダムに複数の要素を選択(重複なし): random.sample()

> randomモジュールの関数sample()で、
  リストからランダムで複数の要素を取得できる。
  要素の重複はなし(非復元抽出)。

> 第一引数にリスト、第二引数に取得したい要素の個数を指定する。
  リストが返される。
[Python ドキュメント](https://docs.python.org/ja/3/library/random.html#random.sample)

```python
import random

lst = [0, 1, 2, 3, 4]

print(random.sample(lst, 3))  # -> [1, 3, 2]
print(type(random.sample(lst, 3)))  # -> <class 'list'>

"""第二引数を1とした場合も要素が一つのリストが返される。
0とした場合は空のリスト。
第一引数に指定したリストの要素数を超える値だとエラーとなる"""

print(random.sample(lst, 1))  # -> [0]
print(random.sample(lst, 0))  # -> []

try:
    print(random.sample(lst, 10))
except ValueError as e:
    print(e)  # -> Sample larger than population or is negative

"第一引数をタプルや文字列にした場合も返されるのはリスト"

print(random.sample(('xxx', 'yyy', 'zzz'), 2))  # -> ['xxx', 'yyy']
print(random.sample('abcde', 2))  # -> ['a', 'e']
```

> タプルや文字列に戻したい場合はtuple(), join()を使う。
[](リストとタプルを相互に変換する.md)
[関連記事](https://note.nkmk.me/python-string-concat/)

```python
import random

print(tuple(random.sample(('xxx', 'yyy', 'zzz'), 2)))  # -> ('yyy', 'xxx')
print(''.join(random.sample('abcde', 2)))  # -> de
```

# ランダムに複数の要素を選択(重複あり): random.choices()

> randomモジュールの関数choices()で、
  リストからランダムで複数の要素を取得できる。
> sample()とは異なり、要素の重複を許して選択される(復元抽出)。

> 引数`k`で取得したい要素の個数を指定する。
  重複が認められているので、取得する要素数`k`を元のリストの要素数より
  大きくすることもできる。

> `k`はキーワード専用引数なので`k=3`などのようにキーワードを指定する
  必要がある。

```python
import random

lst = [0, 1, 2, 3, 4]

print(random.choices(lst, k=3))  # -> [2, 1, 0]
print(random.choices(lst, k=10))  # -> [3, 4, 1, 4, 4, 2, 0, 4, 2, 0]

"kのデフォルトは1。省略した場合は要素数1のリストが返される"

print(random.choices(lst))  # -> [1]

"""引数weightsでそれぞれの要素が選ばれる重み(確率)を指定できる。
weightsに指定するリストの要素の型はintでもfloatでもOK。
0にするとその要素は選ばれない"""

print(random.choices(lst, k=3, weights=[1, 1, 1, 10, 1]))  # -> [0, 2, 3]
print(random.choices(lst, k=3, weights=[1, 1, 0, 0, 0]))  # -> [0, 1, 1]

"""引数cum_weightsに累積的な重みとして指定することもできる。
以下のサンプルコードのcum_weightsは上の一つ目のweightsと等価。"""

print(random.choices(lst, k=3, cum_weights=[1, 2, 3, 13, 14]))
# -> [3, 2, 3]

"""引数weights, cum_weightsのデフォルトはどちらもNoneで、
それぞれの要素が同じ確率で選択される。
引数weightsまたはcum_weightsの長さ(要素数)が元のリストと異なると
エラーが発生する。"""

try:
    print(random.choices(lst, k=3, weights=[1, 1, 1, 10, 1, 1, 1]))
except ValueError as e:
    print(e)  # -> The number of weights does not match the population_

"また、weightsとcum_weightsを同時に指定してもエラーとなる"

try:
    print(random.choices(lst, k=3, weights=[1, 1, 1, 10, 1]
                            , cum_weights=[1, 2, 3, 13, 14]))
except TypeError as e:
    print(e)  # -> Cannot specify both weights and cumulative weights

"""ここまでサンプルコードで例として第一引数にリストを指定していたが、
タプルや文字列でも同様"""
```

# 乱数シードを固定

> randomモジュールの関数seed()に任意の整数を与えることで、
  乱数シードを固定することができる。常に同じ要素が選択される。

```python
import random

lst = [0, 1, 2, 3, 4]

random.seed(0)
print(random.choice(lst))  # -> 3
```

# リンク

[](https://note.nkmk.me/python-random-choice-sample-choices/)
