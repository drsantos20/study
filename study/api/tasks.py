import json

import requests

from celery.decorators import task
from celery.utils.log import get_task_logger
from django.contrib.auth.models import User

from study.api.emails import send_subscription_email, send_order_payment_confirmation_email
from study.api.models import Membership, UserMembership, Subscription, Order
from study.api.models.membership import PREMIUM
from study.api.models.order import SUCCESS
from study.api.utils.payment_response import PaymentResponse
from study.settings import PAYMENT_GATEWAY_URL

logger = get_task_logger(__name__)


@task(name="create_user_membership")
def create_user_membership(user_id):

    logger.info('Message arrived with the following body {}'.format(user_id))
    user = User.objects.get(id=user_id)
    membership = Membership.objects.create()
    user_membership = UserMembership.objects.create(membership=membership, user=user)
    Subscription.objects.create(user_membership=user_membership, active=True)

    logger.info("Sent subscription email")
    """sends an email when user membership is created successfully"""
    return send_subscription_email(first_name=user.first_name, account_type=membership.membership_type)


@task(autoretry_for=(Exception, ConnectionError,), retry_kwargs={'max_retries': 5})
def request_order_payment(order_id):
    logger.info('Message arrived with the following body {}'.format(order_id))

    try:
        payment_request = requests.post(PAYMENT_GATEWAY_URL, headers={'Content-Type': 'application/json'})

        if payment_request.status_code == 408:
            raise ConnectionError()

        if payment_request.status_code == 200:
            response_data = json.loads(payment_request.content)
            payment_response_data = PaymentResponse(**response_data)

            if payment_response_data.payment_status == 'accepted':
                order = Order.objects.get(id=order_id)
                order.order_status = SUCCESS
                order.save()

                update_user_membership.delay(user_id=order.user.id)
                """sends an email when user membership is created successfully"""
                return send_order_payment_confirmation_email(email=order.user.email)

    except (ConnectionError, Exception):
        logger.error('exception raised, it would be retry after 5 seconds')
        pass

@task(name="update_user_membership")
def update_user_membership(user_id):
    user = User.objects.get(id=user_id)
    user_membership = UserMembership.objects.get(user=user)
    membership = user_membership.membership
    membership.membership_type = PREMIUM
    membership.save()

    return send_subscription_email(first_name=user.first_name, account_type=membership.membership_type)
