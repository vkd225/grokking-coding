class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        output = [] # should be using array

        while len(queue) > 0:
            current_node = queue.pop(0)

            if current_node is None:
                continue

            output.append(current_node.name)

            for child in current_node.children:
                queue.append(child)

        return output

# time complexity = O(V+E) => vertices  + edges
# space_complexity = O(V)


