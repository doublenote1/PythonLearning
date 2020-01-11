print('☆ 「sub_pkg_mod_2」の一番最初')

from .. import pkg_mod
from .sub_pkg_mod import sub_pkg_mod_func


def sub_pkg_mod_2_func():
    print('☆ 関数実行: sub_pkg_mod_2_func in 「sub_pkg_mod_2」モジュール')


pkg_mod.pkg_mod_func()
sub_pkg_mod_func()
print('☆ 「sub_pkg_mod_2」モジュールの__name__ →', __name__)
