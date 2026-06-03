"""Priority enum for message classification."""

from enum import IntEnum


class Priority(IntEnum):
    """Defines the priority levels for message in the queue.

    Lower integer values represent higher priority
    (e.g.,HIGH = 0 is processed before MEDIUM = 1).
    """

    HIGH = 0
    MEDIUM = 1
    LOW = 2
