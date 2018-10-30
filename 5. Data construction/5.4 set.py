# Create set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

# Create Empty Set
empty = set()
print(type(empty))  # -> <class 'set'>
empty = {}  # <- empty dictionary
print(type(empty))  # -> <class 'dict'>

print('orange' in basket)  # -> True
print('crabgrass' in basket)  # -> False

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)  # -> {'b', 'd', 'r', 'a', 'c'}

print(a - b)  # -> {'b', 'd', 'r'}
print(a | b)  # -> {'b', 'd', 'z', 'l', 'm', 'r', 'a', 'c'}
print(a & b)  # -> {'c', 'a'}
print(a ^ b)  # -> {'b', 'z', 'l', 'd', 'm', 'r'}

# set Comprehension
print({x for x in 'abracadabra' if x not in 'abc'})  # -> {'d', 'r'}
