# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    output_sum = []
    traverse_tree(root, output_sum, 0)
    return output_sum



def traverse_tree(root, output_sum, sum):
    if root is None:
        return

    sum += root.value
    if root.left is None and root.right is None:
        output_sum.append(sum)
        return

    traverse_tree(root.left, output_sum, sum)
    traverse_tree(root.right, output_sum, sum)
