"""Consumer component for the message queue system."""

import time
from threading import Thread
from typing import Callable, Optional

from message_queue_simulator.exceptions import QueueEmptyError
from message_queue_simulator.message import Message
from message_queue_simulator.message_queue import MessageQueue


class Consumer:
    """Retrieves messages from the MessageQueue and processes them.

    Runs on its own thread to simulate concurrent message consumption.
    Idles safely if the queue is empty.
    """

    def __init__(
        self, queue: MessageQueue, message_handler: Callable[[Message], None]
    ) -> None:
        """Initializes the consumer.

        Args:
            - queue (MessageQueue): The source queue to retrieve messages from.
            - message_handler (Callable): A function that processes a single Message.
        """
        self._queue = queue
        self._message_handler = message_handler

        self._running = False
        self._thread: Optional[Thread] = None

        self._interval = 0.01

        self._processed_count = 0

    def processed_count(self) -> int:
        """Returns the total number of successfully processed messages."""
        return self._processed_count

    def start(self) -> None:
        """Starts the consumer's background thread."""
        self._running = True

        self._thread = Thread(target=self._run)

        self._thread.start()

    def stop(self) -> None:
        """Stops the consumer's background thread and waits for it to finish."""
        self._running = False

        if self._thread is not None:
            self._thread.join()

    def is_running(self) -> bool:
        """Checks if the consumer thread is currently active."""
        return self._running

    def _run(self) -> None:
        """The main loop executed by the background thread.

        Continuously attempts to dequeue and process messages. If the queue
        is empty (QueueEmptyError), it idles and tries again in the next cycle.
        """
        while self.is_running():
            try:
                message = self._queue.dequeue()
                self._message_handler(message)
                self._processed_count += 1
            except QueueEmptyError:
                # Queue is empty: wait for producers to enqueue new messages
                pass
                time.sleep(self._interval)
