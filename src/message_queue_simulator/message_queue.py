from queue import PriorityQueue
from typing import Optional

from message_queue_simulator.exceptions import QueueEmptyError, QueueFullError


class MessageQueue:

    def __init__(self, max_size: Optional[int] = None) -> None:
        self._queue = PriorityQueue()
        self._sequence_number = 0
        self._max_size = max_size

    def enqueue(self, message):
        if self._max_size is not None and self.size() >= self._max_size:
            raise QueueFullError

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
