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


stack = Stack()
n = int(input())
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'push':
        stack.push(int(cmd[1]))
    elif cmd[0] == 'pop':
        stack.pop()
    elif cmd[0] == 'max' and not stack.is_empty():
        print(stack.max())
