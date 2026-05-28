from dataclasses import FrozenInstanceError
from datetime import datetime
from uuid import UUID

import pytest

from message_queue_simulator.message import Message
from message_queue_simulator.priority import Priority


def test_message_creation() -> None:
    payload = {"task": "send_email"}

    message = Message(
        payload=payload,
        priority=Priority.HIGH,
    )

    assert isinstance(message.id, UUID)
    assert isinstance(message.created_at, datetime)

    assert message.payload == payload
    assert message.priority == Priority.HIGH


def test_message_generates_unique_uuid() -> None:
    message_1 = Message(payload={"task": "email"})
    message_2 = Message(payload={"task": "email"})

    assert message_1.id != message_2.id


def test_message_is_immutable() -> None:
    message = Message(payload={"task": "email"})

    with pytest.raises(FrozenInstanceError):
        message.priority = 999
