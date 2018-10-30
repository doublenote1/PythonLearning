import datetime as dt

# ****** 基本型 ******
import re

class Apple:
    """Apple class"""

    # === クラスメンバ ===

    # クラス変数の定義
    farmer = "anonymous"
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

    # コンストラクタ（インスタンス作成時、実行される／インスタンス変数の定義）
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

    # デストラクタ（インスタンス削除時、実行される） ※ 非推奨
    def __del__(self):
        print('デストラクタが呼ばれました')

    # === インスタンスメソッドの定義 ===

    def fresh(self):
        days = (self.__now - self.shipment).days
        temp = float(Apple.__temp)
        freshness = days * Apple.__temp
        return f"入荷してから{days}日、平均{temp}度で保管されており新鮮度は{freshness}です。"

    def display(self):
        lines = [
            str(self.number) + '個目',
            '重さ: ' + str(self.weight),
            '色: ' + str(self.color),
            '出荷日: ' + str(self.shipment).replace('-', '/'),
            self.fresh()
        ]
        for line in lines:
            print(line)
        print()

    def __date_conv(self, orig):
        return dt.date(orig.year, orig.month, orig.day)

# クラス変数参照
print(Apple.__doc__)
print(Apple.farmer)  # -> anonymous
print(Apple.count)  # -> 0
print()

# インスタンス作成
apple1 = Apple(10, "dark red", '2018/7/18')
apple2 = Apple(8, "light red")
apple3 = Apple(6)

# インスタンスの型
print(type(apple1))  # -> <class '__main__.Apple'>

# インスタンス変数（属性）参照
print('apple1.number =', apple1.number)
print('apple1.weight =', apple1.weight)  # -> weight = 10
print('apple1.color =', apple1.color)  # -> color = dark red

# インスタンス変数（属性）の変更
apple1.weight = 8
print('apple1.weight =', apple1.weight)  # -> weight = 8

# 初期化メソッドによってインクリメントされたクラス変数
print('Apple.count =', Apple.count)  # -> 2
print()

# インスタンスメソッドの実行
print('-- Method execution --')
print()

# ****** クラスやインスタンスの変数やメソッドの追加と削除 ******

print('-- Add and Delete --')
print()

class Example:
    pass

Example_instance = Example()

def sample_func(msg='こんにちは'):
    print(msg)

# === 追加 ===

# クラス変数の追加
Example.x = 100
print(Example.x)

# クラスメソッドの追加
Example.greeting = sample_func
Example.greeting()

# インスタンス変数の追加
Example_instance.x = 123
print(Example_instance.x)

# インスタンスメソッドの追加
Example_instance.greeting = sample_func
Example_instance.greeting()

# === 削除 ===

Example.x = None
Example.greeting = None
Example_instance.x = None
Example_instance.greeting = None

print(Example.x)
print(Example.greeting)
print(Example_instance.x)
print(Example_instance.greeting)
print()

# ****** 継承 ******

print('-- inheritance --')
print()

# === 基本型 ===

class DerivedApple(Apple):  # class:Apple を継承した class を作成
    def shipment(self):  # 引数を共有し、内容を上書き
        print('DerivedApple.shipment()')
        self.fresh(3, 10)

    def specific(self):
        print('specific!!')

derived_apple = DerivedApple(100, 'blue')
print(derived_apple.count)
derived_apple.display()
derived_apple.specific()
print()

# === 多重継承 ===

class A:
    a = 'a'

class B:
    b = 'b'

class C(A, B):  # class:A, class:B を継承
    c = 'c'

m = C()
print(m.a, m.b, m.c)
print()
