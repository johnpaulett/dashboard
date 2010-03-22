from celery.decorators import task
from celery.registry import tasks
from celery.task import PeriodicTask
from datetime import timedelta
from dashboard.models import RemoteImage

class LaunchRemoteImageUpdatesTask(PeriodicTask):
    run_every = timedelta(minutes=15)

    def run(self, **kwargs):
        logger = self.get_logger(**kwargs)
        logger.info("Running periodic task!")
        # spin of celery tasks for each image
        for image in RemoteImage.objects.filter(active=True):
            update_image.delay(image)
            
tasks.register(LaunchRemoteImageUpdatesTask)

@task
def update_image(image, **kwargs):
    image.update()
