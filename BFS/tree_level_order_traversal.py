# Given a binary tree, populate an array to represent its level-by-level traversal.
# You should populate the values of all nodes of each level from left to right in separate sub-arrays.


# Level Order Traversal:
#  [[1],[2,3],[4,5,6,7]]


# Solution#
# Since we need to traverse all nodes of each level before moving onto the next level, we can use the Breadth First Search (BFS) technique to solve this problem.

# We can use a Queue to efficiently traverse in BFS fashion. Here are the steps of our algorithm:

# 1. Start by pushing the root node to the queue.
# 2. Keep iterating until the queue is empty.
# 3. In each iteration, first count the elements in the queue (let's call it levelSize). We will have these many nodes in the current level.
# 4. Next, remove levelSize nodes from the queue and push their value in an array to represent the current level.
# 5. After removing each node from the queue, insert both of its children into the queue.
# 6. If the queue is not empty, repeat from step 3 for the next level.

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def traverse(root):
  result = []

  queue = deque()
  queue.append(root)

  while queue:
    level_size = len(queue)
    current_level = []
    for i in range(level_size):
      current_node = queue.popleft()

      # add the node to the current level
      current_level.append(current_node.val)

      # insert the children of current node in the queue
      if current_node.left:
        queue.append(current_node.left)
      if current_node.right:
        queue.append(current_node.right)

    result.append(current_level)

  return result


from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None



# Given a binary tree, populate an array to represent the averages of all of its levels.


def traverse_sum(root):
  result = []

  if root is None:
    return result

  queue = deque()
  queue.append(root)

  while queue:
    level_size = len(queue)
    current_level = []
    level_sum = 0.0
    for i in range(level_size):
      current_node = queue.popleft()

      level_sum += current_node.val

      # add the node to the current level
      current_level.append(current_node.val)

      # insert the children of current node in the queue
      if current_node.left:
        queue.append(current_node.left)
      if current_node.right:
        queue.append(current_node.right)

    result.append(level_size / level_size)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()




