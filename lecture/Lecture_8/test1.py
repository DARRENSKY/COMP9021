class Node:
    def __init__(self, value = None):
        self.value = value
        self.next_node = None


class LinkedList:
    def __init__(self, L = None, key = lambda x: x):
        '''Creates an empty list or a list built from a subscriptable object,
        the key of each value being by default the value itself.

        >>> LinkedList().print()
        >>> LinkedList([]).print()
        >>> LinkedList((0,)).print()
        0
        >>> LinkedList(range(4)).print()
        0, 1, 2, 3
        '''
        self.key = key
        if L is None:
            self.head = None
            return
        # If L is not subscriptable, then will generate an exception that reads:
        # TypeError: 'type_of_L' object is not subscriptable
        if not len(L[: 1]):
            self.head = None
            return
        node = Node(L[0])
        self.head = node
        for e in L[1: ]:
            node.next_node = Node(e)
            node = node.next_node
    def append(self, value):
        '''
        >>> L = LinkedList()
        >>> L.append(0)
        >>> L.print()
        0
        >>> L = LinkedList([0])
        >>> L.append(1)
        >>> L.print()
        0, 1
        >>> L = LinkedList(range(2))
        >>> L.append(2)
        >>> L.print()
        0, 1, 2
        '''
        if not self.head:
            self.head = Node(value)
            return
        node = self.head
        while node.next_node:
            node = node.next_node
        node.next_node = Node(value)
 
    def prepend(self, value):
        '''
        >>> L = LinkedList()
        >>> L.prepend(0)
        >>> L.print()
        0
        >>> L = LinkedList([1])
        >>> L.prepend(0)
        >>> L.print()
        0, 1
        '''
        if not self.head:
            self.head = Node(value)
            return
        head = self.head
        self.head = Node(value)
        self.head.next_node = head
    def delete_value(self, value):
        '''
        >>> L = LinkedList([0, 1, 1, 2])
        >>> L.delete_value(3)
        False
        >>> L.delete_value(1)
        True
        >>> L.print()
        0, 1, 2
        >>> L.delete_value(0)
        True
        >>> L.print()
        1, 2
        >>> L.delete_value(2)
        True
        >>> L.print()
        1
        >>> L.delete_value(1)
        True
        >>> L.print()
        >>> L.delete_value(0)
        False
        '''
        if not self.head:
            return False
        if self.head.value == value:
            self.head = self.head.next_node
            return True
        node = self.head
        while node.next_node and node.next_node.value != value:
            node = node.next_node
        if node.next_node:
            node.next_node = node.next_node.next_node
            return True
        return False


         
