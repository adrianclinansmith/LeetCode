
"""
a?bcd?a?
"""

# 0 -> 1, 1 -> 3, 2 -> 5, -> 3 -> 7, 4 -> 9


class MinHeap:
    def __init__(self):
        self.list = list()
    def add(self, entry):
        self.list[2 * len(self.list) + 1] = entry
minHeap = list()
