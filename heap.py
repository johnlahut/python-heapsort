"""
:author:
    John Lahut
:description:
    Implements a max-heap as per described in Cormen et. al
"""

from copy import deepcopy

class Heap:
    """
    Represents a heap data structure with the appropriate methods
    """

    def __init__(self, arr: list):
        """
        Constructs a heap given an array

        :param arr: Array to construct heap from
        """
        self.arr = arr
        self._build_heap()

    def parent(self, i: int):
        """
        Determines the parent of the current index

        :param i: current index
        :return:  parent index of current index
        """
        return i//2

    def left(self, i: int):
        """
        returns the left node of the current index

        :param i: current index
        :return:  the left node of the current index
        """
        return 2*i + 1

    def right(self, i: int):
        """
        returns the right node of the current index

        :param i: current index
        :return:  the right node of the current index
        """
        return 2*i + 2

    def _heapify(self, i: int):
        """
        maintains the heap property of the array

        :param i: current index to heapify
        :return:  None
        """
        l = self.left(i)
        r = self.right(i)

        if l <= len(self.arr) - 1 and self.arr[l] > self.arr[i]:
            largest = l
        else: largest = i

        if r <= len(self.arr) - 1 and self.arr[r] > self.arr[largest]:
            largest = r

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            return self._heapify(largest)

    def _build_heap(self):
        """
        constructs a heap from an array

        :return: None
        """
        for i in range(len(self.arr)//2, 0, -1):
            self._heapify(i-1)

    def look(self):
        """
        prints the current contents of the heap

        :return: None
        """
        [print(i, end=' ') for i in self.arr]; print()

    def sort(self):
        """
        sorts the current heap

        note that this uses a deepcopy to restore the heap after sorting is done

        :return: the sorted heap as an array
        """
        tmp = deepcopy(self.arr)
        sorted = []

        for i in range(len(self.arr), 1, -1):
            self.arr[0], self.arr[i - 1] = self.arr[i - 1], self.arr[0]
            sorted.append(self.arr.pop())
            self._heapify(0)
        sorted.append(self.arr.pop())
        self.arr = tmp
        return sorted


if __name__ == '__main__()':

    # construct a new heap with an array of values
    heap = Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])

    # print the heap contents
    heap.look()

    # sort the heap and print the sorted values
    print(heap.sort())

    # display that the original heap remains unchanged, rather a copy is returned
    heap.look()

