from rest_framework.test import APITestCase
from rest_framework import status

class OrderCreationTest(APITestCase):
    def test_create_order_success(self):
        payload = {
            "user_id": 1,
            "items": [
                {"product_id": 1, "quantity": 2, "price": 100.0},
                {"product_id": 2, "quantity": 1, "price": 50.0}
            ]
        }
        response = self.client.post("/api/orders/create/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("order_id", response.data)
