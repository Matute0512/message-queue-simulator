import pytest

from message_queue_simulator.exceptions import QueueEmptyError
from message_queue_simulator.message import Message
from message_queue_simulator.message_queue import MessageQueue
from message_queue_simulator.priority import Priority


def test_queue_is_empty_when_created() -> None:
    queue = MessageQueue()

    assert queue.is_empty()

    assert queue.size() == 0


def test_enqueue_adds_message_to_queue() -> None:
    queue = MessageQueue()

    message = Message(payload={"task": "send_email"})

    queue.enqueue(message)

    assert not queue.is_empty()

    assert queue.size() == 1


def test_dequeue_returns_enqueued_message() -> None:
    queue = MessageQueue()
    message = Message(payload={"task": "send_mail"})

    queue.enqueue(message)

    returned_message = queue.dequeue()

    assert returned_message == message


def test_dequeue_returns_highest_priority_message_first() -> None:
    low_message = Message(payload={"task": "low"}, priority=Priority.LOW)

    high_message = Message(payload={"task": "high"}, priority=Priority.HIGH)

    medium_message = Message(payload={"task": "medium"}, priority=Priority.MEDIUM)

    queue = MessageQueue()

    queue.enqueue(low_message)
    queue.enqueue(high_message)
    queue.enqueue(medium_message)

    assert queue.dequeue() == high_message

    assert queue.dequeue() == medium_message

    assert queue.dequeue() == low_message


def test_dequeue_from_empty_queue_raises_exception() -> None:
    queue = MessageQueue()

    with pytest.raises(QueueEmptyError):
        queue.dequeue()


def test_messages_with_same_priority_are_processed_fifo():
    queue = MessageQueue()

    first_message = Message(payload={"task": "first"}, priority=Priority.HIGH)

    second_message = Message(payload={"task": "second"}, priority=Priority.HIGH)

    queue.enqueue(first_message)
    queue.enqueue(second_message)

    assert queue.dequeue() == first_message
    assert queue.dequeue() == second_message
