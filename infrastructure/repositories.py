from infrastructure.models import Order as OrderModel, OrderItem as OrderItemModel

class OrderRepository:
    @staticmethod
    def save(order):
        order_model = OrderModel.objects.create(
            user_id=order.user_id,
            status=order.status,
            created_at=order.created_at
        )
        for item in order.items:
            OrderItemModel.objects.create(
                order=order_model,
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.price
            )
