def findClosestValueInBst(tree, target):
    closest_node_value = tree.value
    difference =  abs(target - closest_node_value)
    current_node = tree

    while current_node is not None:

        if abs(target - current_node.value) < difference:
            closest_node_value = current_node.value
            difference =  abs(target - closest_node_value)


        if target < current_node.value:
            current_node = current_node.left

        elif target > tree.value:
            current_node = current_node.right

        else:
            break

    return closest_node_value