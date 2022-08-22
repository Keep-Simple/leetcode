import heapq


class FrequencyStack:
    """
    Design a class that simulates a Stack data structure,
    implementing the following two operations:

    -push(int num): Pushes the number ‘num’ on the stack.
    -pop(): Returns the most frequent number in the stack.
            If there is a tie, return the number which was pushed later.
    """

    def __init__(self):
        self.max_heap = []
        self.freq_map = {}
        self.sequence_num = 0

    def push(self, num):
        self.freq_map[num] = self.freq_map.get(num, 0) + 1
        heapq.heappush(
            self.max_heap,
            (
                (
                    -self.freq_map[num],
                    -self.sequence_num,
                    num,
                )
            ),
        )
        self.sequence_num += 1

    def pop(self):
        _, _, num = heapq.heappop(self.max_heap)
        if self.freq_map[num] > 1:
            self.freq_map[num] -= 1
        else:
            del self.freq_map[num]
        return num


def test():
    frequency_stack = FrequencyStack()
    frequency_stack.push(1)
    frequency_stack.push(2)
    frequency_stack.push(3)
    frequency_stack.push(2)
    frequency_stack.push(1)
    frequency_stack.push(2)
    frequency_stack.push(5)
    assert frequency_stack.pop() == 2
    assert frequency_stack.pop() == 1
    assert frequency_stack.pop() == 2
    assert frequency_stack.pop() == 5
