from package.relative_ref import mod2
from package.relative_ref.sub_package2 import sub_mod2

mod2.func_same()
mod2.func_sub()
sub_mod2.func_parent()
sub_mod2.func_parent_sub()
