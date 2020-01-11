# === datetimeオブジェクト ===

"""
・datetime オブジェクトは日付（年、月、日）と時刻（時、分、秒、マイクロ秒）
  の両方の情報を持つオブジェクト。
・それらの情報に、属性 year, month, day, hour, minute, second, microsecondでアクセスできる。
"""

# --- datetime.now(): 今日の日付、現在時刻 ---

"""
datetime.now() で今日の日付（現在の日付）と
現在時刻の datetime オブジェクトが得られる。
"""

import datetime

dt_now = datetime.datetime.now()
print(dt_now)  # -> 2018-02-02 18:31:13.271231
print(type(dt_now))  # -> <class 'datetime.datetime'>
print(dt_now.year)  # -> 2018
print(dt_now.hour)  # -> 18
print()

# --- datetime オブジェクトのコンストラクタ ---

"""
・datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)

・任意の日付、時刻のdatetimeオブジェクトを生成することも可能。
・年 year、月 month、日 dayは必須でそのほかは省略可能。
・省略した場合は初期値の0になる。
"""

dt = datetime.datetime(2018, 2, 1, 12, 15, 30, 2000)
print(dt)  # -> 2018-02-01 12:15:30.002000
print(dt.minute)  # -> 15
print(dt.microsecond)  # -> 2000
print()

dt = datetime.datetime(2018, 2, 1)
print(dt)  # -> 2018-02-01 00:00:00
print(dt.minute)  # -> 0
print()

# --- datetimeオブジェクトからdateオブジェクトへの変換 ---

"""
datetime オブジェクトは date()メソッド で
次に説明する date オブジェクトに変換可能。
"""

print(dt_now)  # -> # 2018-02-02 18:31:13.271231
print(type(dt_now))  # -> # <class 'datetime.datetime'>
print()

print(dt_now.date())  # -> 2018-02-02
print(type(dt_now.date()))  # -> <class 'datetime.date'>
print()

# === dateオブジェクト ===

"""
・date オブジェクトは日付（年、月、日）の情報を持つオブジェクト。
・属性 year, month, day でアクセスできる。
"""

# --- date.today(): 今日の日付 ---

"""
date.today() で現在の日付（今日の日付）の date オブジェクトが得られる。
"""

d_today = datetime.date.today()
print(d_today)  # -> 2018-02-02
print(type(d_today))  # -> <class 'datetime.date'>
print(d_today.year)  # -> 2018
print()

# --- dateオブジェクトのコンストラクタ ---

"""
・date(year, month, day)

・すべて必須で、省略はできない
"""

d = datetime.date(2018, 2, 1)
print(d)  # -> 2018-02-01
print(d.month)  # -> 2
print()

# === timeオブジェクト ===

"""
・time オブジェクトは時刻（時、分、秒、マイクロ秒）の情報を持つオブジェクト。
・それらの情報に、属性 hour, minute, second, microsecond でアクセスできる。

・time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
・すべて省略可能で、省略した場合は0となる。
"""

t = datetime.time(12, 15, 30, 2000)
print(t)  # -> 12:15:30.002000
print(type(t))  # -> <class 'datetime.time'>
print(t.hour)  # -> 12

t = datetime.time()
print(t)  # -> 00:00:00
print()

# === timedeltaオブジェクト ===

"""
・timedelta オブジェクトは二つの日時の時間差、経過時間を表すオブジェクト。
・日数、秒数、マイクロ秒数の情報を持ち、
  属性 days, seconds, microseconds でアクセスできる。
・また、total_seconds() メソッドでトータルの秒数を取得することも可能。
"""

# --- datetime, date オブジェクトの引き算で timedelta オブジェクトを生成 ---

"""
・deltatime オブジェクト同士を引き算-すると、
  timedelta オブジェクトが得られる。
・delta オブジェクト同士の引き算でも同様に timedelta オブジェクトが得られる。
"""

td = dt_now - dt
print(td)  # -> 1 day, 18:31:13.271231
print(type(td))  # -> <class 'datetime.timedelta'>
print(td.days)  # -> 1
print(td.seconds)  # -> 66673
print(td.microseconds)  # -> 271231
print(td.total_seconds())  # -> 153073.271231
print()

# --- timedelta オブジェクトのコンストラクタ ---

"""
・timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

・すべて省略可能で、省略した場合は 0 となる。
・なお、timedelta オブジェクトが保持しているのは、
  あくまでも日数 days, 秒数 seconds, マイクロ秒数 microseconds の情報のみで、
  例えば weeks=1 は days=7 と等しい。
"""

td_1w = datetime.timedelta(weeks=1)
print(td_1w)  # -> 7 days, 0:00:00
print(td_1w.days)  # -> 7
print()

# --- timedelta オブジェクトを使った引き算、足し算 ---

"""
・timedelta オブジェクトは datetime オブジェクトや date オブジェクトと
  引き算や足し算などの演算が可能。
・例えば、1 週間前とか 10 日後の日付や 50 分後の時刻などを簡単に計算して取得できる。
"""

d_1w = d_today - td_1w
print(d_1w)  # -> 2018-01-26

td_10d = datetime.timedelta(days=10)
print(td_10d)  # -> 10 days, 0:00:00

dt_10d = dt_now + td_10d
print(dt_10d)  # -> 2018-02-12 18:31:13.271231

td_50m = datetime.timedelta(minutes=50)
print(td_50m)  # -> 0:50:00
print(td_50m.seconds)  # -> 3000

dt_50m = dt_now + td_50m
print(dt_50m)  # -> 2018-02-02 19:21:13.271231
print()

"""
特定の日付までの日数（東京オリンピック開会式まであと何日）
みたいな値を算出するのにも使える。
"""

d_target = datetime.date(2020, 7, 24)
td = d_target - d_today
print(td)  # -> 903 days, 0:00:00
print(td.days)  # -> 903
print()

# === strftime(): 日付、時間から文字列への変換 ===

"""
datetime オブジェクト、date オブジェクトの strftime() メソッドで、
日時（日付、時間）の情報を任意の書式フォーマットの文字列に変換できる。
"""

# --- 書式化コード ---

"""
+----+-------------------------------------------------+----------------------------------------+
| %Y | 西暦(4桁)                                       | 0001, …, 2018, …, 9999               |
| %y | 0埋めした 世紀無しの年                          | 00, 01, …, 99                         |
| %m | 0埋めした 月                                    | 01, 02, …, 12                         |
| %d | 0埋めした 月中の日にち                          | 01, 02, …, 31                         |
| %H | 0埋めした 時(24時間表記)                        | 00, 01, …, 23                         |
| %I | 0埋めした 時(12時間表記)                        | 01, 02, …, 12                         |
| %M | 0埋めした 分                                    | 00, 01, …, 59                         |
| %S | 0埋めした 秒                                    | 00, 01, …, 59                         |
| %f | 0埋めした マイクロ秒                            | 000000, …, 999999                     |
+----+-------------------------------------------------+----------------------------------------+
| %c | ロケールの 日時 を適切な形式で表示              | Tue Aug 16 21: 30:00 1988(en_US)       |
| %x | ロケールの 日付 を適切な形式で表示              | 0 8 / 16 / 1988(en_US)                 |
| %X | ロケールの 時間 を適切な形式で表示              | 21: 30:00(en_US)                       |
| %B | ロケールの 月名                                 | January, February, …, December(en_US) |
| %b | ロケールの 月名(短縮形)                         | Jan, Feb, …, Dec(en_US)               |
| %A | ロケールの 曜日名                               | Sunday, Monday, …, Saturday(en_US)    |
| %a | ロケールの 曜日名(短縮形)                       | Sun, Mon, …, Sat(en_US)               |
| %p | ロケールの 'AM' か 'PM' と等価な文字列          | AM, PM(en_US)                          |
+----+-------------------------------------------------+----------------------------------------+
| %j | 0埋めした 年中の日にち                          | 001, 002, …, 366                      |
| %U | 0埋めした 年中の週番号(週の始まりは日曜日)      | 00, 01, …, 53                         |
| %W | 0埋めした 年中の週番号(週の始まりは月曜日)      | 00, 01, …, 53                         |
+----+-------------------------------------------------+----------------------------------------+
| %w | 曜日を10進表記した文字列(0: 日曜日、6: 土曜日)  | 0, 1, …, 6                            |
| %z | UTCオフセットを '+HHMM' か '-HHMM' の形式で表示 | +0000, -0400, +1030                    |
| %Z | タイムゾーンの名前                              | UTC, EST, CST                          |
+----+-------------------------------------------------+----------------------------------------+
| %% | 文字 '%'を表示                                  |                                        |
+----+-------------------------------------------------+----------------------------------------+
"""

print(dt_now.strftime('%Y-%m-%d %H:%M:%S'))  # -> 2018-02-02 18:31:13
print(d_today.strftime('%y%m%d'))  # -> 180202
print(d_today.strftime('%A, %B %d, %Y'))  # -> Friday, February 02, 2018

import locale

locale.setlocale(locale.LC_ALL, '')

print(d_today.strftime('%Y年%m月%d日'))  # -> 2018年02月02日
print()

print('日番号（1年の何日目か / 正月が001）:', d_today.strftime('%j'))
# -> 日番号（1年の何日目か / 正月が001）: 033

print('週番号（週の始まりは日曜日 / 正月が00）:', d_today.strftime('%U'))
# -> 週番号（週の始まりは日曜日 / 正月が00）: 04

print('週番号（週の始まりは月曜日 / 正月が00）:', d_today.strftime('%W'))
# -> 週番号（週の始まりは月曜日 / 正月が00）: 05
print()

"""文字列ではなく数値を取得したい場合は、int() で整数に変換すれば OK"""
week_num_mon = int(d_today.strftime('%W'))
print(week_num_mon)  # -> 5
print(type(week_num_mon))  # -> <class 'int'>
print()

"""
timedelta オブジェクトと組み合わせて、例えば、
任意のフォーマットで隔週の日付のリストを作るみたいなことも簡単。
"""

def print_date_interval(year, month, day, week_interval=2, n=8):
    date = datetime.date(year, month, day)
    interval = datetime.timedelta(weeks=week_interval)
    df = '%Y年%m月%d日'
    l = []
    for i in range(n):
        l.append((date + i * interval).strftime(df))
    print(l)

print_date_interval(2018, 2, 1)
# -> ['2018年02月01日', '2018年02月15日', '2018年03月01日', '2018年03月15日', '2018年03月29日',
# '2018年04月12日', '2018年04月26日', '2018年05月10日']
print()

# === strptime(): 文字列から日付、時間への変換 ===

"""
・datetime の strptime() を使うと、
  日付や時刻を表す文字列から datetime オブジェクトを生成できる。
・元の文字列に対応する書式化文字列を指定する必要がある。
"""

date_str = '2018/2/1 12:30'
date_dt = datetime.datetime.strptime(date_str, '%Y/%m/%d %H:%M')
print(date_dt)  # -> 2018-02-01 12:30:00
print(type(date_dt))  # -> <class 'datetime.datetime'>
print()

"""
取得した datetime オブジェクトで strftime() メソッドを使うことで、
元の文字列と異なるフォーマットで日付や時刻を表すことができる。
"""

print(date_dt.strftime('%Y年%m月%d日 %H時%M分'))  # -> 2018年02月01日 12時30分
print()

"""
datetime オブジェクトに変換してしまえば timedelta オブジェクトとの演算も可能なので、
例えば同じフォーマットで10日前の日付の文字列を生成したりすることも可能。
"""

date_str = '2018年2月1日'
date_format = '%Y年%m月%d日'
td_10_d = datetime.timedelta(days=10)

date_dt = datetime.datetime.strptime(date_str, date_format)
date_dt_new = date_dt - td_10_d
date_str_new = date_dt_new.strftime(date_format)

print(date_str_new)  # -> 2018年01月22日

# ****** 日付から曜日や月の名前を日本語文字列で取得 ******

