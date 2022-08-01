import heapq


class MaxHeap:
    def __init__(self, data=None):
        if data is None:
            data = []
        heapq.heapify(data)
        self.data = data

    def top(self):
        return -self.data[0]

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)

    def remove(self, val):
        self.data[self.data.index(-val)] = self.data[-1]
        self.data.pop()
        heapq.heapify(self.data)

    def __len__(self):
        return len(self.data)


class MinHeap:
    def __init__(self, data=None):
        if data is None:
            data = []
        heapq.heapify(data)
        self.data = data

    def top(self):
        return self.data[0]

    def push(self, val):
        heapq.heappush(self.data, val)

    def pop(self):
        return heapq.heappop(self.data)

    def remove(self, val):
        self.data[self.data.index(val)] = self.data[-1]
        self.data.pop()
        heapq.heapify(self.data)

    def __len__(self):
        return len(self.data)
