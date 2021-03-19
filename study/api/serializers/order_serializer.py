from rest_framework import serializers

from study.api.models import UserMembership
from study.api.models.order import Order

from study.api.tasks import request_order_payment


class OrderCreateSerializer(serializers.ModelSerializer):
    order_status = serializers.ChoiceField(choices=Order.ORDER_STATUS, read_only=True)
    total_price = serializers.DecimalField(decimal_places=2, max_digits=5, read_only=True)

    @property
    def get_user(self):
        return self.context['request'].user

    def create(self, validated_data):
        user_membership = UserMembership.objects.get(user=self.get_user)
        order = Order.objects.create(user=self.get_user, membership=user_membership.membership)
        request_order_payment.delay(order_id=order.id)
        return order

    class Meta:
        model = Order
        fields = ['order_status', 'total_price']


class OrderReadSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return {
            'order_status': instance.order_status,
            'total_price': instance.total_price,
        }
