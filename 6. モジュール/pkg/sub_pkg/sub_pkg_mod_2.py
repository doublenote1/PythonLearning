print('□bbb1_mod2の一番最初')

from .. import aaa1_mod1
from .mod_1 import bbb1_def1


def bbb1_def2():
    print('□モジュールbbb1_mod2の関数bbb1_def2')


aaa1_mod1.aaa1_def1()
bbb1_def1()
print('□モジュールbbb1_mod2の__name__→', __name__)
