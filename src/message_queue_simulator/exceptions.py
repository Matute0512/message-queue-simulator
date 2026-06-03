class QueueEmptyError(Exception):
    "Raised when attempting to dequeue from an empty queue."


class QueueFullError(Exception):
    "Raised when attempting to enqueue to a full queue."
