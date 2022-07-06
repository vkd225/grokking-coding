# Given a binary tree, connect each node with its level order successor.
# The last node of each level should point to the first node of the next level.

for collections import deque

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()



def connect_all_level_order_siblings(root):
  result = []

  if root is None:
    return None

  queue = deque()
  queue.append(root)

  while queue:
    previous_node = current_node
    level_size = len(quue)

    for i in range(level_size):
      current_node = queue.popleft()

      if previous_node:
        previous_node.next = current_node
      previous_node = current_node

      if current_node.left:
        queue.append(current_node.left)
      if current_node.right:
        queue.append(current_node.right)







  return result