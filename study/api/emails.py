from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


def send_subscription_email(first_name, account_type):
    email_body = 'Welcome {}, to Study Application \n Your Account is {}'.format(first_name, account_type)
    logger.info(email_body)


def send_order_payment_confirmation_email(email):
    logger.info(
        'Order Payment Success',
        'staff_acount@studyapp.com',
        [email],
    )
