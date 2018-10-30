# Stack

# Original List
stack = [3, 4, 5]

stack.append(6)
stack.append(7)
print(stack)  # [3, 4, 5, 6, 7]

stack.pop()
print(stack)  # [3, 4, 5, 6]

stack.pop()
stack.pop()
print(stack)  # [3, 4]

# Queue

from collections import deque

queue = deque(["Eric", "John", "Michael"])
print(queue)  # -> deque(['Eric', 'John', 'Michael'])

queue.append("Terry")
queue.append("Graham")
print(queue)  # -> deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])

queue.popleft()  # -> deque(['John', 'Michael', 'Terry', 'Graham'])
print(queue)
queue.popleft()  # -> deque(['Michael', 'Terry', 'Graham'])
print(queue)
