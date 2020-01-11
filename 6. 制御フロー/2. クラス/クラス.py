import datetime as dt


# ****** 基本型 ******

class Apple:
    """Apple class"""

    # === クラスメンバ ===

    # クラス変数の定義
    farmer = "近藤清史"
    count = 0
    __shipment_days = 5  # private variable
    __arrival_days = 5  # private variable
    __date_format_str = '%Y/%m/%d %H:%M'  # private variable
    __temp = 10.0  # private variable

    # クラスメソッドの定義
    @classmethod
    def __count_up(cls):  # private method
        cls.count += 1

    # === インスタンスメンバ ===

    # コンストラクタ(インスタンス作成時、実行される／インスタンス変数の定義)
    def __init__(self, weight, color='red', arrival=None):
        Apple.__count_up()
        self.__now = self.__date_conv(dt.datetime.now())
        self.number = Apple.count
        if arrival is None:
            self.arrival = self.__now
        else:
            self.arrival = dt.datetime.strptime(arrival, '%Y/%m/%d')
        self.harvest = self.__date_conv(self.arrival - dt.timedelta(days=Apple.__shipment_days + Apple.__arrival_days))
        self.shipment = self.__date_conv(self.arrival - dt.timedelta(days=Apple.__arrival_days))
        self.weight = weight
        self.color = color
        self.display()


    # === インスタンスメソッドの定義 ===


    def fresh(self):
        days = (self.__now - self.shipment).days
        temp = float(Apple.__temp)
        freshness = days * Apple.__temp
        return f"入荷してから{days}日、平均{temp}度で保管されており新鮮度は{freshness}です。"


    def display(self):
        lines = [
            '---' + str(self.number) + '個目 ---',
            '重さ:   ' + str(self.weight),
            '色:     ' + str(self.color),
            '出荷日: ' + str(self.shipment).replace('-', '/'),
            self.fresh()
        ]
        for line in lines:
            print(line)
        print()


    def __date_conv(self, orig):
        return dt.date(orig.year, orig.month, orig.day)


# クラス変数参照
print('クラス名:', Apple.__doc__)  # -> クラス名: Apple class
print('生産者  :', Apple.farmer)  # -> 生産者  : 近藤清史
print('入荷個数:', Apple.count)  # -> 入荷個数: 0
print()

# インスタンス作成
apple1 = Apple(10, "dark red", '2018/7/18')

# インスタンスの型
print(type(apple1))  # -> <class '__main__.Apple'>

# インスタンス変数(属性)参照
print('apple1.number =', apple1.number)
print('apple1.weight =', apple1.weight)  # -> weight = 10
print('apple1.color =', apple1.color)  # -> color = dark red
print()

apple2 = Apple(8, "light red")
apple3 = Apple(6)

# インスタンスメソッドの実行
print('==== Method execution ====')
print()

# ****** クラスやインスタンスの変数やメソッドの追加・変更・削除 ******

print('==== メンバの追加・変更・削除 ====')
print()


class Example:

    # デストラクタ(インスタンス削除時、実行される) ※ 非推奨
    def __del__(self):
        print('デストラクタが呼ばれました')


    pass


Example_instance = Example()


def sample_func1():
    print('This is sample_func1!!!')


def sample_func2():
    print('This is sample_func2!!!')


def sample_func3():
    print('This is sample_func3!!!')


def sample_func4():
    print('This is sample_func4!!!')


def sample_display():
    members = [
        'Example.x                      = ' + str(Example.x),
        'Example.say_func_name          = ' + str(Example.say_func_name),
        'Example_instance.x             = ' + str(Example_instance.x),
        'Example_instance.say_func_name = ' + str(Example_instance.say_func_name),
    ]
    for member in members:
        print(member)


# === 追加 ===
print('-- 追加 --')
print()

# クラス変数の追加
Example.x = 1
# クラスメソッドの追加
Example.say_func_name = sample_func1
# インスタンス変数の追加
Example_instance.x = 2
# インスタンスメソッドの追加
Example_instance.say_func_name = sample_func2

# メソッド実行
Example.say_func_name()
Example_instance.say_func_name()
print()

sample_display()
print()

# === 変更 ===
print('-- 変更 --')
print()

# クラス変数の変更
Example.x *= 10000
# クラスメソッドの変更
Example.say_func_name = sample_func3
# インスタンス変数の変更
Example_instance.x *= 10000
# インスタンスメソッドの変更
Example_instance.say_func_name = sample_func4

# メソッド実行
Example.say_func_name()
Example_instance.say_func_name()
print()

sample_display()
print()

# === 削除 ===
print('-- 削除 --')
print()

# -- Noneで削除 --
Example.x = None
Example.say_func_name = None
Example_instance.x = None
Example_instance.say_func_name = None

sample_display()
print()

# -- del 文で削除 --
del Example.x
del Example.say_func_name
del Example_instance.x
del Example_instance.say_func_name

del Example  # class の削除(デストラクタは呼ばれない)
del Example_instance  # instance の削除(デストラクタが呼ばれる)
print()

# ****** 継承 ******

print('==== 継承 ====')
print()


class A:
    a = 'A'


    def say_hello(self):
        print('Hello!')


class B:
    b = 'B'


class C(A):  # class:A を継承
    c = 'C'


    def say_hello(self):  # 引数を共有し、内容を上書き
        print('こんにちは!')


    def say_morning(self):  # 独自メソッド
        print('Good morning!')


class D(A, B):  # class:A, class:B を継承
    d = 'D'


inst_a = A()
inst_b = B()
inst_c = C()
inst_d = D()

# -- A --
print('-- A --')
print(inst_a.a)
inst_a.say_hello()
print()

# -- B --
print('-- B --')
print(inst_b.b)
print()

# -- C --
print('-- C --')
print(inst_c.a, inst_c.c, sep=', ')
inst_c.say_hello()
inst_c.say_morning()
print()

# -- D --
print('-- D --')
print(inst_d.a, inst_d.b, inst_d.d, sep=', ')
inst_d.say_hello()
print()
