from relative_ref import mod2
from relative_ref.sub_package2 import sub_mod2

mod2.func_same()
print()
mod2.func_sub()
print()
sub_mod2.func_parent()
print()
sub_mod2.func_parent_sub()
