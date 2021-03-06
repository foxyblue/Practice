class Stack:
    def __init__(self):
        self._list = []

    def push(self, item):
        self._list.append(item)

    def pop(self):
        try:
            return self._list.pop()
        except IndexError:
            return None

    def __len__(self):
        return len(self._list) >= 1


class Queue:
    def __init__(self):
        self._in = Stack()
        self._out = Stack()

    def enqueue(self, item):
        """ O(1)
        """
        self._in.push(item)

    def dequeue(self):
        """
        Time: O(1) <- Amortized
        Worst case: O(n)
        """
        if self._out:
            return self._out.pop()

        while self._in:
            item = self._in.pop()
            self._out.push(item)

        if self._out:
            return self._out.pop()

        return None


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    print(f"Get {stack.pop()} expected: 1")
    assert not stack

    stack.push(2)
    stack.push(3)
    assert stack

    print(f"Get {stack.pop()} expected: 3")
    print(f"Get {stack.pop()} expected: 2")

    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(f"Got: {queue.dequeue()} expected: 1")

    queue.enqueue(5)
    queue.enqueue(6)
    print(f"Got: {queue.dequeue()} expected: 2")
    print(f"Got: {queue.dequeue()} expected: 3")
    print(f"Got: {queue.dequeue()} expected: 4")
    print(f"Got: {queue.dequeue()} expected: 5")
    print(f"Got: {queue.dequeue()} expected: 6")
    print(f"Got: {queue.dequeue()} expected: None")
