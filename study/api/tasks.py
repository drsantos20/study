from celery.decorators import task
from celery.utils.log import get_task_logger
from django.contrib.auth.models import User

from study.api.emails import send_subscription_email
from study.api.models import Membership, UserMembership, Subscription

logger = get_task_logger(__name__)


@task(name="create_user_membership")
def create_user_membership(user_id):
    """sends an email when user membership is created successfully"""

    user = User.objects.get(id=user_id)
    membership = Membership.objects.create()
    user_membership = UserMembership.objects.create(membership=membership, user=user)
    Subscription.objects.create(user_membership=user_membership, active=True)

    logger.info("Sent subscription email")
    return send_subscription_email(first_name=user.first_name, email=user.email)
