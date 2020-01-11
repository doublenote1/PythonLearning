> Pythonには、組み込み型として「リスト`list`」、標準ライブラリに「配列`array`」
  が用意されている。
> さらに数値計算ライブラリNumPyをインストールすると
  「多次元配列`numpy.ndarray`」を使うこともできる。

---------------------------------------------------------------------------

# リストと配列とnumpy.ndarrayの違い

## リスト - list

> 省略

## 配列 - array

[docs.python.org](https://docs.python.org/ja/3/library/array.html)

>   * 標準ライブラリの`array`モジュールをインポートして使う
    * 同じ型しか格納できない
    * 一次元配列のみ
    * 型に制限がある以外はリストと同様の処理が可能

> コンストラクタ`array.array()`で型コードを指定して生成する。
  型コードの一覧は公式ドキュメント参照。

> 型コードと一致しない型の要素は格納できない。

```python
import array

arr_int = array.array('i', [0, 1, 2])
print(arr_int)  # -> array('i', [0, 1, 2])
arr_float = array.array('f', [0.0, 0.1, 0.2])
print(arr_float)
# -> array('f', [0.0, 0.10000000149011612, 0.20000000298023224])

try:
    arr_int = array.array('i', [0, 0.1, 2])
except TypeError as e:
    print(e)  # -> integer argument expected, got float

"リストと同様の処理が可能"
print(arr_int[1])  # -> 1
print(sum(arr_int))  # -> 3
```

## 多次元配列 - numpy.ndarray

>   * NumPyをインストール、importして使う
    * 同じ型しか格納できない
        object型で様々な型へのポインタを格納することはできる
    * 多次元配列を表現できる
    * 数値計算のためのメソッド・関数が豊富で、高速な演算が可能
        行列演算や画像処理など様々な場面で使える

```python
import numpy as np

arr = np.array([0, 1, 2])
print(arr)  # -> [0 1 2]
arr_2d = np.array([[0, 1, 2], [3, 4, 5]])
print(arr_2d)
# -> [[0 1 2]
# ->  [3 4 5]]

"""多次元配列の場合はカンマ区切りで位置(インデックス)を指定する。
スライスも使用可能"""

print(arr[1])  # -> # 1
print(arr_2d[1, 1])  # -> # 4
print(arr_2d[0, 1:])  # -> # [1 2]

"要素ごとに演算をしたり(例は平方根)、行列積を求めたりできる"

print(np.sqrt(arr_2d))
# [[0.         1.         1.41421356]
#  [1.73205081 2.         2.23606798]]

arr_1 = np.array([[1, 2], [3, 4]])
arr_2 = np.array([[1, 2, 3], [4, 5, 6]])

print(np.dot(arr_1, arr_2))
# [[ 9 12 15]
#  [19 26 33]]
```

> なぜか混同されていることが多いが、`array`型ではなく`ndarray`型。
  `numpy.array()`は`ndarray`を生成する関数。

# 独断と偏見によるそれぞれの使い分け

> いわゆる配列ライクな処理をするのであればリストで十分な場合が多い。
> `array`は格納する要素の型が制限されているので厳密なメモリ管理が可能だが、
  特に気にする必要がなければ`list`、
  より効率的な数値計算を行いたければ`numpy.ndarray`のほうが適当。
  メモリサイズ、メモリアドレスを必要とするような処理以外に
  使いどころはない(と思う)。

> 多次元配列を扱う場合や配列に対する数値計算(科学技術演算)、
  行列演算を行う場合は`NumPy`配列`numpy.ndarray`を使う。
> コンピュータビジョンライブラリOpenCVや機械学習ライブラリscikit-learnなど
  多くのライブラリで`NumPy`配列`numpy.ndarray`が使われているので、
  それらのライブラリを使うと自動的に`numpy.ndarray`を使うことになる。

> なお、`list`と`numpy.ndarray`は相互に変換する事が可能。

# データ分析ライブラリpandas

> 表で表現されるような二次元データに対して統計的な処理を行う場合は、
  データ分析ライブラリ`pandas`が便利。

> `pandas`では二次元データを`pandas.DataFrame`として扱う。
  (`pandas.Seiries`として一次元データを扱うことも可能)

> `pandas.DataFrame`も`pandas.Series`も内部では`numpy.ndarray`で
  データを保持しているが、
  行・列ごとの操作や表計算ソフトにおけるピボットテーブルのような操作など、
  データ処理に便利な関数やメソッドが豊富に用意されている。

> 雰囲気は以下のような感じ。
  列ごとの平均値を算出したり、属性を指定して集計したりしている。

```python
import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)
df['sex'] = ['Female', 'Male', 'Male', 'Male', 'Female', 'Male']
print(df)
#          age state  point     sex
# name                             
# Alice     24    NY     64  Female
# Bob       42    CA     92    Male
# Charlie   18    CA     70    Male
# Dave      68    TX     70    Male
# Ellen     24    CA     88  Female
# Frank     30    NY     57    Male

print(df.mean())
# age      34.333333
# point    73.500000
# dtype: float64

print(df.pivot_table(index='state', columns='sex', aggfunc='mean'))
#          age        point      
# sex   Female  Male Female  Male
# state                          
# CA      24.0  30.0   88.0  81.0
# NY      24.0  30.0   64.0  57.0
# TX       NaN  68.0    NaN  70.0
```

> 例のような数値と文字列を含んだデータは`NumPy`だと扱いが面倒だが、
  `pandas`だと非常に簡単。

# リンク

[note.nkmk.me](https://note.nkmk.me/python-list-array-numpy-ndarray/)
