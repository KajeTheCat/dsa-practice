from data_structures.queue import Queue,Node
from data_structures.invalid_operation_error import InvalidOperationError


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    def __str__(self):
        current = self.front
        str = ''
        while current:
            str += f'{{ {current.value} }} -> '
            current = current.next
        return str + "NULL"

    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self, value):
        current = self.front

        if self.front is None:
            raise InvalidOperationError

        if value == 'cat' or value == 'dog':
            first = None
            previous = None
            if str(self.front.value) == value:
                first = self.front
                self.front = self.front.next
                return first.value
            while current:
                previous = current
                # print('hi ', type(current.value))
                if str(current.next.value) == value:
                    first = current.next
                    print(current)
                    if str(self.front.value) == value:
                        self.front = self.front.next
                    elif str(self.rear.value) == value:
                        current.next = None
                    elif current.next.next:
                        previous.next = current.next.next
                    break
                current = current.next
            return first.value
        return None


class Dog:
    def __str__(self):
        return 'dog'


class Cat:
    def __str__(self):
        return 'cat'
