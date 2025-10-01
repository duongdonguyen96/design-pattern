from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class OrderItem:
    product_id: int
    quantity: int
    price: float

@dataclass
class Order:
    user_id: int
    items: List[OrderItem]
    status: str = field(default="NEW")
    created_at: datetime = field(default_factory=datetime.utcnow)
