import time

from message_queue_simulator.message import Message
from message_queue_simulator.message_queue import MessageQueue
from message_queue_simulator.producer import Producer

# ==========================================
# 1. TESTS
# ==========================================


def test_producer_enqueues_generated_message() -> None:
    queue = MessageQueue()

    producer = Producer(queue=queue, message_factory=_create_message)

    producer.produce()
    assert queue.size() == 1


def test_producer_uses_message_factory() -> None:
    queue = MessageQueue()

    expected_message = Message(payload={"task": "custom"})

    def create_custom_message() -> Message:
        return expected_message

    producer = Producer(queue=queue, message_factory=create_custom_message)

    producer.produce()

    message = queue.dequeue()

    assert message == expected_message


def test_producer_starts_running() -> None:
    queue = MessageQueue()

    producer = Producer(queue=queue, message_factory=_create_message)
    producer.start()

    assert producer.is_running() is True


def test_producer_stops_running() -> None:
    queue = MessageQueue()

    producer = Producer(queue=queue, message_factory=_create_message)
    producer.start()
    producer.stop()

    assert producer.is_running() is False


def test_producer_generates_messages_while_running() -> None:
    queue = MessageQueue()

    producer = Producer(queue=queue, message_factory=_create_message)

    producer.start()
    time.sleep(0.1)
    producer.stop()

    assert queue.size() > 0


def test_producer_counts_produced_messages() -> None:
    queue = MessageQueue()

    producer = Producer(queue=queue, message_factory=_create_message)

    assert producer.produced_count() == 0

    producer.produce()
    producer.produce()

    assert producer.produced_count() == 2


def test_producer_handles_queue_full_error_grecefully() -> None:
    queue = MessageQueue(max_size=1)

    queue.enqueue(Message(payload={"task": "initial"}))

    producer = Producer(queue=queue, message_factory=_create_message)
    producer.start()

    time.sleep(0.05)

    producer.stop()

    assert queue.size() == 1

    assert producer.produced_count() == 0


# ==========================================
# 2. AUXILIARY FUNCTIONS
# ==========================================


def _create_message() -> Message:
    """Función auxiliar privada para generar un mensaje genérico."""
    return Message(payload={"task": "email"})
