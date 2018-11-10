import os

print(os.getcwd())  # カレントフォルダ
os.chdir(r'C:\Users')  # カレントフォルダ移動
print(os.getcwd())
os.chdir(r'C:\Users\KIYO\Projects\Python Learning')
print(os.getcwd())
os.system('mkdir today')  # Shell 実行

