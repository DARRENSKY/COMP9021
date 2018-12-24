# Written by Eric Martin for COMP9021


'''
A Stack abstract data type
'''


class EmptyStackError(Exception):
    def __init__(self, message):
        self.message = message


class Stack:
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def peek(self):
        '''
        >>> stack = Stack()
        >>> stack.peek()
        Traceback (most recent call last):
        ...
        EmptyStackError: Cannot peek at top of empty stack
        '''
        if self.is_empty():
            raise EmptyStackError('Cannot peek at top of empty stack')
        return self._data[-1]

    def push(self, datum):
        self._data.append(datum)

    def pop(self):
        '''
        >>> stack = Stack()
        >>> stack.peek()
        Traceback (most recent call last):
        ...
        EmptyStackError: Cannot pop from top of empty stack
        '''
        if self.is_empty():
            raise EmptyStackError('Cannot pop from top of empty stack')
        return self._data.pop()

T={1:[2,4,5],2:[3],5:[6,11,13],6:[7,8,10],8:[9],11:[12]}

def depth_first_exploration():
    stack=Stack()
    stack.push([1])
    while not stack.is_empty():
        path=stack.pop()
        print(path)
        print('------')
        print(path[-1])
        if path[-1] in T:
            for child in reversed(T[path[-1]]):
                print(child)
            
                stack.push(list(path)+[child])
depth_first_exploration()
