from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel
from study.api.models import Membership


PENDING = 'Pending'
SUCCESS = 'Success'
DECLINED = 'Declined'
INSUFFICIENT_FOUNDS = 'Insufficient Founds'


class Order(TimeStampedModel):
    ORDER_STATUS = (
        (PENDING, 'pending'),
        (SUCCESS, 'success'),
        (DECLINED, 'declined'),
        (INSUFFICIENT_FOUNDS, 'Insufficient Founds')
    )

    order_status = models.CharField(
        choices=ORDER_STATUS, default='Pending',
        max_length=30,
    )

    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)

    @property
    def total_price(self):
        membership_price = self.membership.price
        return membership_price

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_order', on_delete=models.CASCADE)

