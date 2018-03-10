import logging.config
import schedule
import time
import tns.job.notification_job as notification_job

logger = logging.getLogger(__name__)


def run():
    """
    This is the method that starts the scheduler which will run a job periodically
    """

    print("Starting the scheduler")

    schedule.every(10).seconds.do(notification_job.notify_everyone)

    while 1:
        schedule.run_pending()
        time.sleep(1)