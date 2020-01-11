import argparse
import sys

# === sys.argv ===
# コマンドライン引数のリストを出力
# 一番目の要素に実行ファイルのパスが格納される
# 要素の型はすべて文字列

args_size = len(sys.argv)

print('type(sys.argv):', type(sys.argv))
print('len(sys.argv) :', args_size)
print()
for i in range(args_size):
    print("sys.argv[", i, "]: ", sys.argv[i], sep='')
print()
