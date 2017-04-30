class Stack(list):
    """
    Stack implementation with MAX option
    """

    def __init__(self):
        self.__data = []
        self.__maxs = []

    def is_empty(self):
        return not self.__data

    def push(self, val):
        if self.is_empty():
            self.__maxs += [val]
        elif val >= self.__maxs[-1]:
            self.__maxs += [val]
        else:
            self.__maxs += [self.__maxs[-1]]

        self.__data += [val]

    def top(self):
        if not self.is_empty():
            return self.__data[-1]

    def pop(self):
        del self.__maxs[-1]
        return self.__data.pop()

    def max(self):
        if not self.is_empty():
            return self.__maxs[-1]

class Queue(list):
    """
    a Queue implementation with current MAX available (using two stacks)
    """

    def __init__(self):
        self.setter = Stack()
        self.getter = Stack()

    def is_empty(self):
        return self.getter.is_empty() and self.setter.is_empty()

    def push_back(self, val):
        self.setter.push(val)

    def pop_front(self):
        if self.getter.is_empty():
            while not self.setter.is_empty():
                self.getter.push(self.setter.pop())
            return self.getter.pop()
        else:
            return self.getter.pop()

    def max(self):
        if self.getter.is_empty():
            if not self.setter.is_empty():
                return self.setter.max()
        elif self.setter.is_empty():
            if not self.getter.is_empty():
                return  self.getter.max()
        else:
            return max(self.getter.max(),self.setter.max())


q = Queue()
n = int(input())
a = [int(x) for x in input().split()]
k = int(input())
maxs = []
for i in range(k):
    q.push_back(a[i])
maxs += [q.max()]
for i in range(k, n):
    q.push_back(a[i])
    q.pop_front()
    maxs += [q.max()]

for it in maxs:
    print(it, end=' ')