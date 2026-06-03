import time

from message_queue_simulator.consumer import Consumer
from message_queue_simulator.message import Message
from message_queue_simulator.message_queue import MessageQueue


def test_consumer_starts_running() -> None:
    queue = MessageQueue()

    def handle_message(message: Message) -> None:
        pass

    consumer = Consumer(
        queue=queue,
        message_handler=handle_message
    )

    consumer.start()

    assert consumer.is_running() is True


def test_consumer_stops_running() -> None:
    queue = MessageQueue()

    def handle_message(message: Message) -> None:
        pass

    consumer = Consumer(
        queue=queue,
        message_handler=handle_message
    )

    consumer.start()
    consumer.stop()

    assert consumer.is_running() is False


def test_consumer_processes_messages_while_running() -> None:
    queue = MessageQueue()
    processed_messages = []

    def handle_message(message: Message) -> None:
        processed_messages.append(message)

    message = Message(
        payload={"task": "email"}
    )

    queue.enqueue(message)

    consumer = Consumer(
        queue=queue,
        message_handler=handle_message
    )

    consumer.start()

    time.sleep(0.1)

    consumer.stop()

    assert len(processed_messages) == 1
    assert processed_messages[0] == message
