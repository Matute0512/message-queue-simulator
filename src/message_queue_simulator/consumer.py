from typing import Callable, Optional
from threading import Thread
from message_queue_simulator.exceptions import QueueEmptyError
from message_queue_simulator.message import Message
from message_queue_simulator.message_queue import MessageQueue

import time


class Consumer:

    def __init__(
        self,
        queue: MessageQueue,
        message_handler: Callable[[Message], None]
    ) -> None:
        self._queue = queue
        self._message_handler = message_handler
        self._running = False
        self._thread: Optional[Thread] = None
        self._interval = 0.01

    def start(self) -> None:
        self._running = True

        self._thread = Thread(
            target=self._run
        )

        self._thread.start()

    def stop(self) -> None:
        self._running = False

        if self._thread is not None:
            self._thread.join()

    def is_running(self) -> bool:
        return self._running

    def _run(self) -> None:
        while self.is_running():
            try:
                message = self._queue.dequeue()
                self._message_handler(message)

            except QueueEmptyError:
                time.sleep(self._interval)
