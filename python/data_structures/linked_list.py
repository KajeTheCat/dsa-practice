class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError:
    def __init__(self):
        self.message = "Something went wrong."

    def __str__(self):
        return self.message


class LinkedList:
    """
    Linked list data structure implementation containing functions for:
    insert, append, insert before, insert after, to string, includes, reverse, and kth from end.
    """

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        current = self.head
        str = ""
        while current:
            str += f"{{ {current.value} }} -> "
            current = current.next
        return str + "NULL"

    def linked_list_insert(self, value):
        new_node = Node(value)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, value, target):
        pass

    def insert_after(self, value, target):
        pass

    def linked_list_to_string(self):
        current = self.head
        str = ""
        while current:
            str += f"{ {current.value} } -> "
            current = current.next
        return str + "NULL"

    def linked_list_includes(self, val):
        current = self.head
        while current:
            if current.value == val:
                return True
            current = current.next
        return False

    def linked_list_reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def kth_from_end(self, value):
        new_node = Node(value)
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        length = length - value
        while length != 0:
            length -= 1
            current = current.next
        return new_node
