from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from study.api.models import Order
from study.api.serializers.order_serializer import OrderCreateSerializer, OrderReadSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    @action(methods=['get'], detail=True, serializer_class=OrderReadSerializer)
    def get_order_detail(self, request, version, pk=None):
        order = get_object_or_404(Order.objects.filter(id=pk, user=self.request.user))
        serializer = self.get_serializer(order, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
