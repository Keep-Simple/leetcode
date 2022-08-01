from grokking.two_heaps.utils import MaxHeap, MinHeap


class MedianOfAStream:
    """
    Design a class to calculate the median of a number stream
    """

    def __init__(self):
        self.left = MaxHeap()
        self.right = MinHeap()

    def insert_num(self, num):
        if len(self.left) == 0 or self.left.top() >= num:
            self.left.push(num)
        else:
            self.right.push(num)

        len_diff = len(self.left) - len(self.right)

        if len_diff == 2:
            self.right.push(self.left.pop())
        # if count of nums is odd, left will hold 1 more than right
        elif len_diff == -1:
            self.left.push(self.right.pop())

    def find_median(self):
        if len(self.left) - len(self.right) == 0:
            return (self.left.top() + self.right.top()) / 2
        return self.left.top()


def test():
    median_of_a_stream = MedianOfAStream()
    median_of_a_stream.insert_num(3)
    median_of_a_stream.insert_num(1)
    assert median_of_a_stream.find_median() == 2
    median_of_a_stream.insert_num(5)
    assert median_of_a_stream.find_median() == 3
    median_of_a_stream.insert_num(4)
    assert median_of_a_stream.find_median() == 3.5
