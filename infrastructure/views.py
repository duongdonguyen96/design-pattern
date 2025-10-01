from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from application.services import OrderService

class CreateOrderView(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        items = request.data.get("items")
        if not user_id or not items:
            return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)
        
        order = OrderService.create_order(user_id, items)
        return Response({
            "order_id": order.id,
            "user_id": order.user_id,
            "status": order.status,
            "created_at": order.created_at,
            "items": [
                {"product_id": item.product_id, "quantity": item.quantity, "price": item.price}
                for item in order.items
            ]
        }, status=status.HTTP_201_CREATED)
