from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

from message_queue_simulator.priority import Priority


@dataclass(frozen=True)
class Message:
    payload: dict
    priority: Priority = Priority.MEDIUM
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=datetime.now)
