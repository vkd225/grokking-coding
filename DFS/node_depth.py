# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



# recursive approach
# def nodeDepths(root, depth = 0):
#     if root is None:
#         return 0

#     return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


def nodeDepths(root):
    total_depth = 0
    stack = [{"node": root, "depth": 0}]

    while len(stack) > 0:
        node_info = stack.pop()
        curr_node, curr_depth = node_info["node"], node_info["depth"]

        if curr_node is None:
          continue

        total_depth += curr_depth
        stack.append({"node": curr_node.left, "depth": curr_depth + 1})
        stack.append({"node": curr_node.right, "depth": curr_depth + 1})

    return total_depth