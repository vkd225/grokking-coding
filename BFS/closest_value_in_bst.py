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


tree = {
  "nodes": [
    {"id": "10", "left": "5", "right": "15", "value": 10},
    {"id": "15", "left": "13", "right": "22", "value": 15},
    {"id": "22", "left": null, "right": null, "value": 22},
    {"id": "13", "left": null, "right": "14", "value": 13},
    {"id": "14", "left": null, "right": null, "value": 14},
    {"id": "5", "left": "2", "right": "5-2", "value": 5},
    {"id": "5-2", "left": null, "right": null, "value": 5},
    {"id": "2", "left": "1", "right": null, "value": 2},
    {"id": "1", "left": null, "right": null, "value": 1}
  ],
  "root": "10"
}

target = 12