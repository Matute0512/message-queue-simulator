from queue import PriorityQueue


class MessageQueue():

    def __init__(self) -> None:
        self._queue = PriorityQueue()

    def enqueue(self, message):
        priority = message.priority
        self._queue.put(
            (message.priority, message)
        )
        pass

    def dequeue(self):
        priority, message = self._queue.get()
        return message

    def size(self):
        return self._queue.qsize()

    def is_empty(self):
        return self.size() == 0
