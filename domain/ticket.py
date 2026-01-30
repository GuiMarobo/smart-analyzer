from dataclasses import dataclass

@dataclass
class Ticket:
    id: int
    description: str
    category: str
    priority: str
    resolution_time_hours: int
