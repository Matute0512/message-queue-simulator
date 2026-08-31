"""Message entity definition."""

from collections.abc import Mapping
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4

from message_queue_simulator.priority import Priority


@dataclass(frozen=True)
class Message:
    """Represents an immutable message to be processed in the queue.

    Attributes:
    - payload (Mapping[str, Any]): The actual data or task description of the message.
    - priority (Priority): The urgency level of the message. Defaults to MEDIUM.
    - id (UUID): A unique identifier for the message, auto-generated.
    - created_at (datetime): The exact time the message was created, auto-generated.
    """

    payload: Mapping[str, Any]
    priority: Priority = Priority.MEDIUM
    # Use default_factory to generate unique values for each instance
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc))
