"""Producer component for the message queue system."""

import time
from threading import Thread
from typing import Callable, Optional

from message_queue_simulator.exceptions import QueueFullError
from message_queue_simulator.message import Message
from message_queue_simulator.message_queue import MessageQueue


class Producer:
    """Generates messages and enqueues them into the MessageQueue.

    Runs on its own thread to simulate concurrent message production.
    Implements backpressure by pausing if the queue is full.
    """

    def __init__(
        self,
        queue: MessageQueue,
        message_factory: Callable[[], Message],
    ) -> None:
        """Initializes the producer.

        Args:
            queue (MessageQueue): The target queue to enqueue messages to.
            message_factory (Callable): A function that returns a new Message instance.
        """
        self._queue = queue
        self._message_factory = message_factory

        self._thread: Optional[Thread] = None
        self._running = False
        self._thread = None

        self._interval = 0.01

        self._produced_count = 0

    def produce(self) -> None:
        """Generates a single message and attempts to enqueue it."""
        message = self._message_factory()
        self._queue.enqueue(message)
        self._produced_count += 1

    def produced_count(self) -> int:
        """Returns the total number of successfully enqueued messages."""
        return self._produced_count

    def start(self) -> None:
        """Starts the producer's background thread."""
        self._running = True

        self._thread = Thread(target=self._run)
        self._thread.start()

    def stop(self) -> None:
        """Stops the producer's background thread and waits for it to finish."""
        self._running = False

        if self._thread is not None:
            self._thread.join()

    def is_running(self) -> bool:
        """Checks if the producer thread is currently active."""
        return self._running

    def _run(self) -> None:
        """The main loop executed by the background thread.

        Continuously produces messages. If the queue is full (QueueFullError),
        it ignores the error and waits for the next cycle (Backpressure).
        """
        while self.is_running():
            try:
                self.produce()
            except QueueFullError:
                # Backpressure: wait for consumers to clear the queue
                pass
            time.sleep(self._interval)
