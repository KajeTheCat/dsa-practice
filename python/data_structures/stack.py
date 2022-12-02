from invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Stack:
    """
    Functions to Push, Pop, Peek, and also return a Boolean if the stack is empty or not.
    """

    def __init__(self):
        self.top = None

    def __str__(self):
        current = self.top
        print(current.value)
        str = ''
        while current:
            str += f'{{ {current.value} }} -> '
            current = current.next
        return str + "NULL"

    def push(self, value):
        node = Node(value)
        if self.top is None:
            self.top = node
        else:
            temp = self.top
            self.top = node
            self.top.next = temp

    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            return temp.value
        else:
            raise InvalidOperationError

    def peek(self):
        if self.top:
            return self.top.value
        else:
            raise InvalidOperationError

    def is_empty(self):
        if self.top:
            return False
        else:
            return True
