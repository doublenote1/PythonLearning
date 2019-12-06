print('■メインモジュールmain_modのコード開始')

from pkg.sub_pkg.mod2 import bbb1_def2

print('■メインモジュールmain_modのimport文実行完了')
bbb1_def2()
print('■メインモジュールmain_modの__name__→',__name__)
print('■メインモジュールmain_modのコード終了')
