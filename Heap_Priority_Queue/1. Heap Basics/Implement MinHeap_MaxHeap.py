class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = self.parent(index)

            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = (
                    self.heap[parent_index],
                    self.heap[index],
                )
                index = parent_index
            else:
                break

    def extract_min(self):
        if not self.heap:
            raise IndexError("Heap is empty")

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return minimum

    def _heapify_down(self, index):
        size = len(self.heap)

        while True:
            smallest = index
            left = self.left_child(index)
            right = self.right_child(index)

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index],
                )
                index = smallest
            else:
                break

    def peek(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0


class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = self.parent(index)

            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = (
                    self.heap[parent_index],
                    self.heap[index],
                )
                index = parent_index
            else:
                break

    def extract_max(self):
        if not self.heap:
            raise IndexError("Heap is empty")

        if len(self.heap) == 1:
            return self.heap.pop()

        maximum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return maximum

    def _heapify_down(self, index):
        size = len(self.heap)

        while True:
            largest = index
            left = self.left_child(index)
            right = self.right_child(index)

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left

            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = (
                    self.heap[largest],
                    self.heap[index],
                )
                index = largest
            else:
                break

    def peek(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0