from domain.entities import Order, OrderItem
from infrastructure.repositories import OrderRepository

class OrderService:
    @staticmethod
    def create_order(user_id: int, items: list):
        order_items = [OrderItem(**item) for item in items]
        order = Order(user_id=user_id, items=order_items)
        OrderRepository.save(order)
        return order
