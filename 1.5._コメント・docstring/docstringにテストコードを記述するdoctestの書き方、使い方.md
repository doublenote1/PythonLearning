> Pythonには、docstringの内容に応じたテストを行う
  `doctest`モジュールが標準で含まれている。
> docstringの中に入出力例を書くだけなので簡単、かつ、
  ドキュメントとしても分かりやすくなる。

  [doctest — 対話的な実行例をテストする](https://docs.python.org/ja/3/library/doctest.html)

# doctestによるテストのシンプルな例

> テストを加えたい関数のdocstring（"""または'''で囲まれた文字列）に
  Python対話モードの形式で関数の呼び出しと期待される出力値を記述し、
  doctest.testmod()で実行する。

## エラーがない場合

> 関数の内容とdocstringの内容に間違いがないコードを作成する。

```python
def add(a, b):
    '''
    >>> add(1, 2)
    3
    >>> add(5, 10)
    15
    '''

    return a + b


if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

> このファイルを実行する。

> エラーがない場合は何も出力されない。

> なお、`if __name__ == '__main__'`は「該当のスクリプトファイルが
  コマンドラインから実行された場合にのみ以降の処理を実行する」という意味。

   [](../6.%20モジュール/3.%20if%20__name__%20==%20'__main__'の意味と使い方.md)

## エラーがある場合

> 以下のような間違ったコードを作って実行するとエラーが出力される。

```python
def add(a, b):
    '''
    >>> add(1, 2)
    3
    >>> add(5, 10)
    10
    '''

    return a * b


if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

```dockerfile
$ python3 doctest_example_error.py
**********************************************************************
File "doctest_example_error.py", line 3, in __main__.add
Failed example:
    add(1, 2)
Expected:
    3
Got:
    2
**********************************************************************
File "doctest_example_error.py", line 5, in __main__.add
Failed example:
    add(5, 10)
Expected:
    10
Got:
    50
**********************************************************************
1 items had failures:
   2 of   2 in __main__.add
***Test Failed*** 2 failures.
```

> doctestに書いた期待される出力値が`Expected`、
  実際の出力値が`Got`で示されている。

# オプション、引数による出力結果の制御

## 「-v」オプション

> エラーがない場合でも出力結果を表示させたい場合は、
  コマンドラインで`-v`オプションを付けて実行する。

```dockerfile
$ python3 doctest_example.py -v
Trying:
    add(1, 2)
Expecting:
    3
ok
Trying:
    add(5, 10)
Expecting:
    15
ok
1 items had no tests:
    __main__
1 items passed all tests:
   2 tests in __main__.add
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
```

## verbose引数

> 常に出力結果を表示させたい場合は、
  pyファイル内の`doctest.testmod()`で引数`verbose=True`を指定する。

```python
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
```

> `-v`オプションを付けなくても、常に出力結果が表示される。

```dockerfile
$ python3 doctest_example_verbose.py
Trying:
    add(1, 2)
Expecting:
    3
ok
Trying:
    add(5, 10)
Expecting:
    15
ok
1 items had no tests:
    __main__
1 items passed all tests:
   2 tests in __main__.add
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
```

# コマンドラインからdoctestモジュールを実行

> `if __name__ == '__main__'`内では別の処理をさせたい場合、
  pyファイル内で`doctest.testmod()`を呼ばなくても
  コマンドラインから直接`doctest`モジュールを実行することができる。

> 例えば、次のような場合。

```python
def add(a, b):
    '''
    >>> add(1, 2)
    3
    >>> add(5, 10)
    15
    '''

    return a + b


if __name__ == '__main__':
    import sys
    result = add(int(sys.argv[1]), int(sys.argv[2]))
    print(result)
```

> 通常のようにコマンドライン引数を受け取って処理を実行することができる。

```dockerfile
$ python3 doctest_example_without_import.py 3 4
7
```

> `-m`オプションを付けて`doctest`をスクリプトとして実行すると、
  `doctest`が書かれた関数に対してテストが行われる。
> 出力結果を表示させたい場合はこれまでと同様に`-v`を付ける。

```dockerfile
$ python3 -m doctest doctest_example_without_import.py

$ python3 -m doctest -v doctest_example_without_import.py
Trying:
    add(1, 2)
Expecting:
    3
ok
Trying:
    add(5, 10)
Expecting:
    15
ok
1 items had no tests:
    doctest_example_without_import
1 items passed all tests:
   2 tests in doctest_example_without_import.add
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
```

# 外部のテキストファイルにテストを記述する

> docstringの中ではなく
  外部のテキストファイルにテストコードを記述することもできる。

## テキストファイルの書き方

> docstringに書いていたように、Python対話モードの形式で書く。
  使用する関数をインポートしておく必要がある。

> テスト対象の.pyファイルと同じディレクトリにテキストファイルを置く場合は
  `from <ファイル名> import <関数名>`とすればOK。

```dockerfile
>>> from doctest_example import add
>>> add(1, 2)
3
>>> add(5, 10)
15
```

## pyファイルから呼び出し

> テスト用の別の`.py`ファイルで`doctest.testfile()`を呼び出す。

> `doctest.testfile()`の引数に
  テストコードが記述されたテキストファイルのパスを指定。

```python
import doctest
doctest.testfile('doctest_text.txt')
```

> このpyファイルを実行する。

```dockerfile
$ python3 doctest_example_testfile.py -v
Trying:
    from doctest_example import add
Expecting nothing
ok
Trying:
    add(1, 2)
Expecting:
    3
ok
Trying:
    add(5, 10)
Expecting:
    15
ok
1 items passed all tests:
   3 tests in doctest_text.txt
3 tests in 1 items.
3 passed and 0 failed.
Test passed.
```

## テキストファイルを直接実行

> pyファイルがなくても、
  コマンドラインから直接テキストファイルを読んで
  テストを実行することもできる。

> Pythonコマンドに`-m`オプションを付けて`doctest`をスクリプトとして実行する。
> テキストファイルのパスをコマンドライン引数として指定すればOK。

```dockerfile
$ python3 -m doctest -v doctest_text.txt
Trying:
    from doctest_example import add
Expecting nothing
ok
Trying:
    add(1, 2)
Expecting:
    3
ok
Trying:
    add(5, 10)
Expecting:
    15
ok
1 items passed all tests:
   3 tests in doctest_text.txt
3 tests in 1 items.
3 passed and 0 failed.
Test passed.
```

# リンク

[](https://note.nkmk.me/python-doctest-example/)
