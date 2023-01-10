from data_structures.binary_tree import BinaryTree

def breadth_first(tree):

    queue = []

    horizontal = []

    current = tree.root

    queue.append(current)

    while len(queue) > 0:
        current = queue.pop(0)

        if current is None:
            return []

        horizontal.append(current.value)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return horizontal
