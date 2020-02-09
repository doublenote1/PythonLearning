# クラス名はパスカルケースで表記
# クラス名後部の括弧(継承元を指定する時使用)は省略すると、すべてのオブジェクトの基底クラスである「object」クラスのみ継承する様になる
import datetime
from dateutil.relativedelta import relativedelta


class Man():
    # === クラス変数 ===
    count = 0
    ages = []

    # === インスタンスメソッド ===

    # --- コンストラクタ(初期化メソッド。インスタンス作成時実行) ---

    def __init__(self, name, birthday):  # ここで引数を受け取る
        # インスタンスメソッド内からクラス変数へアクセスする方法①
        Man.count += 1

        # 渡された引数はそのままでは、このブロック内でのみ参照可能
        print(f'私の名前は「{name}」です')

        # 渡された引数を他のインスタンスメソッドで参照したい場合、「インスタンス変数」へ格納する

        self.name = name

        today = datetime.date.today()
        date_birthday = datetime.datetime.strptime(birthday, '%Y/%m/%d').date()
        self.age = relativedelta(today, date_birthday).years

        s_year, s_month, s_day = date_birthday.year, date_birthday.month, date_birthday.day
        date_next_birthday = datetime.datetime.strptime(f'{today.year}/{s_month}/{s_day}', '%Y/%m/%d').date()
        if date_next_birthday < today:
            date_next_birthday = datetime.datetime.strptime(f'{today.year + 1}/{s_month}/{s_day}', '%Y/%m/%d').date()
        self.days_to_birthday = (date_next_birthday - today).days

        # インスタンスメソッドからクラス変数へアクセスする方法②
        self.__class__.ages.append(self.age)

    # --- 通常のインスタンスメソッド ---

    def print_age(self):
        print(f'年齢は{self.age:>2}才です')

    def print_days_to_birthday(self):
        print(f'次の誕生日まで{self.days_to_birthday:>3}日です')

    #TODO: 他のインスタンスメソッドの呼び出しの例を追加

    # --- クラスメソッド ---

    @classmethod
    def print_count(cls):
        print(f'{cls.count}人います')

    @classmethod
    def print_max_age(cls):
        max_age = max(cls.ages)
        print(f'最高年齢は{max_age:>2}才です')

    @classmethod
    def print_min_age(cls):
        min_age = min(cls.ages)
        print(f'最小年齢は{min_age:>2}才です')

    @classmethod
    def print_average_age(cls):
        average_age = round(sum(cls.ages) / cls.count)
        print(f'平均年齢は{average_age:>2}才です')

# === クラスのデータ型 ===

print(type(Man))  # -> <class 'type'>

# === インスタンス作成 ===

kondo = Man('近藤清史', '1971/2/28')  # -> 私の名前は「近藤清史」です
isoguchi = Man('磯口美里', '1967/2/27')  # -> 私の名前は「磯口美里」です
setsuko = Man('臼田節子', '1975/4/14')  # -> 私の名前は「臼田節子」です

# === インスタンス作成時、コンストラクタで定義した引数の指定が必須 ===

try:
    test = Man()
except TypeError as e:
    print(e)
# -> __init__() missing 2 required positional arguments: 'name' and 'birthday'
try:
    test = Man(1, 2, 3)
except TypeError as e:
    print(e)
# -> __init__() takes 3 positional arguments but 4 were given

# === インスタンスのデータ型 ===
# (「__main__.」の部分は、オブジェクトのクラスが同じコード(実行環境、モジュール)上にあることを意味する)

print(type(kondo))  # -> <class '__main__.Man'>

# === メソッド呼び出し ===

# クラスからクラスメソッド呼び出し
Man.print_count()  # -> 3人います

# インスタンスからクラスメソッド呼び出し
# (もし同名のインスタンスメソッドがあれば、そちらが実行される)
kondo.print_max_age()  # -> 最高年齢は52才です
kondo.print_min_age()  # -> 最小年齢は44才です
kondo.print_average_age()  # -> 平均年齢は48才です

# インスタンスメソッド呼び出し
kondo.print_age()  # -> 年齢は48才です
isoguchi.print_days_to_birthday()  # -> 次の誕生日まで 17日です

# === 変数へアクセス ===

# クラスからクラス変数へアクセス
print(Man.count)  # -> 3

# インスタンスからクラス変数へアクセス
# (もし同名のインスタンス変数があれば、そちらが返される)
print(kondo.count)  # -> 3

# インスタンス変数へアクセス
print(kondo.age)  # -> 48

# === インスタンスに属性を加える ===

# インスタンス変数を定義
kondo.job = 'テレフォンオペレーター'
print(kondo.job)  # -> テレフォンオペレーター

# インスタンスメソッドを定義
kondo.print_job = lambda: print(f'{kondo.name}の仕事は{kondo.job}です')
kondo.print_job()  # -> 近藤清史の仕事はテレフォンオペレーターです

# リンク

# https://www.headboost.jp/python-class/
# https://www.headboost.jp/python-class-inheritance/
# https://www.atmarkit.co.jp/ait/articles/1907/26/news020.html
# https://www.atmarkit.co.jp/ait/articles/1907/30/news021.html
# https://www.atmarkit.co.jp/ait/articles/1908/06/news015.html
