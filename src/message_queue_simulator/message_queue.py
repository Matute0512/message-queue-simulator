from queue import PriorityQueue

from message_queue_simulator.exceptions import QueueEmptyError


class MessageQueue:

    def __init__(self) -> None:
        self._queue = PriorityQueue()
        self._sequence_number = 0

    def enqueue(self, message):
        self._queue.put((message.priority, self._sequence_number, message))
        self._sequence_number += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyError()

        _, _, message = self._queue.get()
        return message

    def size(self):
        return self._queue.qsize()

    def is_empty(self):
        return self.size() == 0
