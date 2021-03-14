from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


def send_subscription_email(first_name, email):
    logger.info(
        'Welcome ' + first_name + ' to Study Application',
        'Your Account is Free',
        'staff_acount@studyapp.com',
        [email],
    )
