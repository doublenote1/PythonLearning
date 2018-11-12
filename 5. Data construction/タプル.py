# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)  # -> ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)  # -> ([1, 2, 3], [3, 2, 1])

# Tuples are immutable:
try:
    t[0] = 88888
except:
    print('Error!')

# Empty or One Tuple
empty = ()
print(len(empty))  # -> 0
print(empty)  # -> ()

singleton = 'hello',  # <-- note trailing comma
print(len(singleton))  # -> 1
print(singleton)  # -> ('hello',)
