"""Thread-safe priority message queue implementation."""

from queue import PriorityQueue
from typing import Optional

from message_queue_simulator.exceptions import QueueEmptyError, QueueFullError


class MessageQueue:
    """A priority-based, thread-safe queue for managing messages.

    Messages with higher priority (lower enum values) are dequeued first.
    If messages share the same priority, they are processed in a FIFO
    (First-In-First-Out) order.
    """

    def __init__(self, max_size: Optional[int] = None) -> None:
        """Initializes the message queue.

        Args:
            - max_size (int, optional): The maximum number of messages the queue
                can hold. If None, the queue has infinite capacity.
        """
        self._queue = PriorityQueue()
        self._sequence_number = 0
        self._max_size = max_size

    def enqueue(self, message):
        """Adds a message to the queue based on its priority.

        Args:
            - message (Message): The message to be added.

        Raises:
            - QueueFullError: If the queue has reached its max_size limit.
        """

        if self._max_size is not None and self.size() >= self._max_size:
            raise QueueFullError

        # Tuple structure: (priority, sequence_number, message)
        # Sequence number ensures FIFO order for identical priorities
        self._queue.put((message.priority, self._sequence_number, message))
        self._sequence_number += 1

    def dequeue(self):
        """Removes and returns the highest priority message from the queue.

        Returns:
            - Message: The retrieved message.

        Raises:
            - QueueEmptyError: If the queue has no messages.
        """
        if self.is_empty():
            raise QueueEmptyError()

        _, _, message = self._queue.get()
        return message

    def size(self):
        """Returns the current number of messages in the queue."""
        return self._queue.qsize()

    def is_empty(self):
        """Checks if the queue contains no messages."""
        return self.size() == 0
