from data_structures.linked_list import TargetError

def zip_lists(llist1, llist2):
    if(llist1.head == None and llist2.head == None):
        raise TargetError
    if(llist1.head == None and llist2.head):
        return llist2
    if(llist1.head and llist2.head == None):
        return llist1

    current1 = llist1.head
    current2 = llist2.head

    while current1 and current2:

        temp1 = current1.next
        temp2 = current2.next

        current2.next = temp1
        current1.next = current2

        current1 = temp1
        current2 = temp2

        llist2.head = current2
    return llist1

