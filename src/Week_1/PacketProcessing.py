import queue


class Buffer(queue):
    def __init__(self, size):
        self.log = []
        self.__buffer = queue.Queue()
        self.__cursize = 0
        self.__proc = 0
        self.__size = size

    def add_package(self, time, duration):
        if self.__check(time):
            self.__push(time, duration)
            self.__cursize += 1
            if self.__buffer:
                self.__proc = self.__buffer[-1]
        else:
            self.log += [-1]

    def __check(self, time):
        if not self.__buffer:
            return True
        for it in range(self.__cursize):
            if self.__buffer[it] <= time:
                del self.__buffer[it]
                self.__cursize -= 1
            else:
                break

        if self.__cursize < self.__size:
            return True
        return False

    def __push(self, time, duration):
        if self.__buffer:
            self.log.append(max(time, self.__buffer[-1]))
        else:
            self.log.append(max(time, self.__proc))
        self.__buffer.append(self.log[-1] + duration)


size, n = map(int, input().split())
buffer = Buffer(size)
for i in range(n):
    time, duration = map(int, input().split())
    buffer.add_package(time, duration)
for elem in buffer.log:
    print(elem)
