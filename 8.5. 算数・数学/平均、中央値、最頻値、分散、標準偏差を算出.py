import statistics
import math

l = [10, 1, 3, 7, 1]

# === 平均（算術平均、相加平均）: ===
# statistics.mean()

mean = statistics.mean(l)
print(mean)

"""
・組み込み関数 sum() と len() を使って平均を算出することも可能
・sum() は合計、len() は要素数を返す
"""
my_mean = sum(l) / len(l)
print(my_mean)

# === 調和平均: ===
# statistics.harmonic_mean()

harmonic_mean = statistics.harmonic_mean(l)
print(harmonic_mean)

"""調和平均は逆数の算術平均の逆数"""
my_harmonic_mean = len(l) / sum(1 / x for x in l)
print(my_harmonic_mean)

"""例ではジェネレータ式（リスト内包表記のジェネレータ版）を使っている"""

# === 中央値: ===
# statistics.median()

"""中央値はデータを昇順または降順に並べたときに中央に位置する値"""
median = statistics.median(l)
print(median)

# --- データの個数が偶数の場合 ---

"""
データの個数が偶数の場合、
statistics.median() では中央2個の値の算術平均が返される
"""
l_even = [10, 1, 3, 7, 1, 6]
median = statistics.median(l_even)
print(median)

"""
statistics.median_low() は小さい方の値、
statistics.median_high() は大きい方の値を返す
"""
median_low = statistics.median_low(l_even)
print(median_low)
median_high = statistics.median_high(l_even)
print(median_high)

"""
statistics.median_low() も statistics.median_high()も、
奇数個のデータの場合は statistics.median() と同じく中央の値を返す
"""
print(statistics.median_high(l) == statistics.median_low(l) == statistics.median(l))

# === 最頻値: ===
# statistics.mode()

mode = statistics.mode(l)
print(mode)

"""最頻値が一つでない場合はエラー StatisticsError となるので注意"""
l_mode_error = [1, 2, 3, 4, 5]
try:
    mode = statistics.mode(l_mode_error)
except StatisticsError as e:
    print(e)

l_mode_error = [1, 1, 1, 2, 2, 2, 3]

"""
Python標準ライブラリ collectionsのCounter クラスを使うと、
最頻値だけでなく各要素の出現回数をカウントしたり、
出現回数順に要素を取得したりできる
"""

# === 母分散: ===
# statistics.pvariance()

pvariance = statistics.pvariance(l)
print(pvariance)

"""組み込み関数 sum() と len() を使って算出することもできる"""
my_pvariance = sum((x - sum(l) / len(l))**2 for x in l) / len(l)
print(my_pvariance)

# === 母集団の標準偏差: ===
# statistics.pstdev()

pstdev = statistics.pstdev(l)
print(pstdev)

"""母集団の標準偏差は母分散の平方根である"""
print(math.sqrt(pvariance))

# === 不偏分散・標本分散: ===
# statistics.variance()

variance = statistics.variance(l)
print(variance)

"""組み込み関数 sum() と len() を使って算出することもできる"""
my_variance = sum((x - sum(l) / len(l))**2 for x in l) / (len(l) - 1)
print(my_variance)

# === 標本標準偏差: ===
# statistics.stdev()

stdev = statistics.stdev(l)
print(stdev)

"""
標本標準偏差と呼ばれたり不偏標準偏差と呼ばれたりするが、
statistics.stdev() で取得できるのは上述の不偏分散の平方根
"""
print(math.sqrt(variance))
