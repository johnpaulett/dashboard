from celery.decorators import task
from celery.registry import tasks
from celery.task import PeriodicTask
from datetime import timedelta
from stream.models import Feed

class LaunchFeedUpdatesTask(PeriodicTask):
    run_every = timedelta(minutes=30)

    def run(self, **kwargs):
        logger = self.get_logger(**kwargs)
        logger.info("Running periodic task!")
        # spin of celery tasks for each feed
        for feed in Feed.objects.all():
            #feed.check()
            check_feed.delay(feed)
            
tasks.register(LaunchFeedUpdatesTask)

@task
def check_feed(feed, **kwargs):
    feed.check()
