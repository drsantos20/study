from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


def send_subscription_email(first_name, account_type):
    email_body = 'Welcome {}, to Study Application \n Your Account now is {}'.format(first_name, account_type)
    logger.info(email_body)


def send_order_payment_status_email(email, order_status):
    email_body = 'Order Status \n hello {} Your Payment status is {}'.format(email, order_status)
    logger.info(email_body)
