from message_queue_simulator.message_queue import MessageQueue
from message_queue_simulator.message import Message
from message_queue_simulator.producer import Producer


def test_producer_enqueues_generated_message() -> None:
    queue = MessageQueue()

    def create_message() -> Message:
        return Message(
            payload={"task": "email"}
        )

    producer = Producer(
        queue=queue,
        message_factory=create_message
    )

    producer.produce()
    assert queue.size() == 1


def test_producer_uses_message_factory() -> None:
    queue = MessageQueue()

    expected_message = Message(
        payload={"task": "custom"}
    )

    def create_message() -> Message:
        return expected_message

    producer = Producer(
        queue=queue,
        message_factory=create_message
    )

    producer.produce()

    message = queue.dequeue()

    assert message == expected_message
