from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue

def fizz_buzz_tree(tree, Node = None):
    new_tree = copy.deepcopy(tree)
    if not tree.root:
        return "no tree found"

    queue = Queue()

    queue.enqueue(new_tree.root)

    while not queue.is_empty():
        node = queue.dequeue()
        if node.value % 15 == 0:
            node.value = "FizzBuzz"
        elif node.value % 3 == 0:
            node.value = "Fizz"
        elif node.value % 5 == 0:
            node.value = "Buzz"
        else:
            node.value = str(node.value)

        for child in node.children:
            queue.enqueue(child)

    return new_tree
