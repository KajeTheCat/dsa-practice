from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.back = None

    def __str__(self):
        current = self.front
        print(current.value)
        str = ''
        while current:
            str += f'{{ {current.value} }} -> '
            current = current.next
        return str + "NULL"

    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError
        temp = self.front
        if self.front == self.back:
            self.back = None
        self.front = self.front.next
        return temp.value

    def peek(self):
        if self.front is None:
            raise InvalidOperationError
        else:
            return self.front.value

    def is_empty(self):
        if self.front:
            return False
        else:
            return True
