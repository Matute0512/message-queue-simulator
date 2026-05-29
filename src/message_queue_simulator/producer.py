import time
from threading import Thread
from typing import Callable, Optional

from message_queue_simulator.message import Message
from message_queue_simulator.message_queue import MessageQueue


class Producer:
    def __init__(
        self,
        queue: MessageQueue,
        message_factory: Callable[[], Message],
    ) -> None:
        self._queue = queue
        self._message_factory = message_factory

        self._thread: Optional[Thread] = None
        self._running = False
        self._thread = None

        self._interval = 0.01

    def produce(self) -> None:
        message = self._message_factory()
        self._queue.enqueue(message)

    def start(self) -> None:
        self._running = True

        self._thread = Thread(target=self._run)
        self._thread.start()

    def stop(self) -> None:
        self._running = False

        if self._thread is not None:
            self._thread.join()

    def is_running(self) -> bool:
        return self._running

    def _run(self) -> None:
        while self.is_running():
            self.produce()
            time.sleep(self._interval)
