from message_queue_simulator.message import Message
from message_queue_simulator.message_queue import MessageQueue
from typing import Callable


class Producer:
    def __init__(
        self,
        queue: MessageQueue,
        message_factory: Callable[[], Message]
    ) -> None:
        self._queue = queue
        self._message_factory = message_factory

    def produce(self) -> None:
        message = self._message_factory()
        self._queue.enqueue(message)
