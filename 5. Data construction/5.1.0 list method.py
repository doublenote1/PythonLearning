# Original List
lst = [1, 2, 3, 4]

# append
lst.append('appended')
print(lst)  # -> [1, 2, 3, 4, 'appended']

# extend
lst.extend(['1', '2'])
print(lst)  # -> [1, 2, 3, 4, 'appended', '1', '2']

# insert
lst.insert(5, 'inserted')
print(lst)  # -> [1, 2, 3, 4, 'appended', 'inserted', '1', '2']

# remove
lst.remove('inserted')
lst.remove('appended')
print(lst)  # -> [1, 2, 3, 4, '1', '2']

# pop
print(lst.pop())  # -> 2
print(lst)  # -> [1, 2, 3, 4, '1']
print(lst.pop())  # -> 1
print(lst)  # -> [1, 2, 3, 4]

# clear
lst.clear()
print(lst)  # -> []

# Original List
lst = [3, 4, 1, 2, 3, 'target', 3, 3]

# index
print(lst.index('target'))  # -> 5

# count
print(lst.count(3))  # -> 4

# sort
lst.remove('target')
lst.sort()
print(lst)  # -> [1, 2, 3, 3, 3, 3, 4]

# reverse
lst.reverse()
print(lst)  # -> [4, 3, 3, 3, 3, 2, 1]
