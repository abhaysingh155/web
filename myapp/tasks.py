from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
import time
from .views import india_home, home, home_global

logger = get_task_logger(__name__)

@periodic_task(run_every=(crontab(minute='*/30')), name="get_api_data", ignore_result=True)
def get_api_data():
	"""
    Call rest API for the data
    """
	home_global()
	print("World Data has taken from API")
	logger.info("World Data has taken from API")
	india_home()
	print("India Data has taken from API")
	logger.info("India Data has taken from API")
	time.sleep(180)
	home()
	print("All Countries Data has taken from API")
	logger.info("All Countries Data has taken from API")

