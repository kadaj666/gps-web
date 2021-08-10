from celery import shared_task
from celery.decorators import task
from django.apps import apps
import warnings
from .models import MarketApk, ApkReview
from google_play_scraper import app, Sort, reviews
warnings.filterwarnings('ignore', message='Unverified HTTPS request')
from datetime import datetime


@shared_task(queue="parse_market", default_retry_delay=30, max_retries=3)
def get_unparsed_apk():
    new_apk = MarketApk.objects.all()
    for apk in new_apk:
        sync_apk_market.delay(apk.id)
        # sync_apk_reviews.delay(apk.id)
    return ("Done Parsing")





@shared_task(queue="parse_market", default_retry_delay=30, max_retries=3)
def sync_apk_market(apk):
    apk_instance = MarketApk.objects.get(id=apk)
    result = app(apk_instance.apk, lang='en', country='us')
    apk_instance.title=result['title']
    apk_instance.url=result['url']
    apk_instance.descriptionHTML=result['descriptionHTML']
    apk_instance.summary=result['summary']
    apk_instance.installs=result['installs']
    apk_instance.score=result['score']
    apk_instance.ratings=result['ratings']
    apk_instance.reviews=result['reviews']
    apk_instance.size=result['size']
    apk_instance.androidVersionText=result['androidVersionText']
    apk_instance.developer=result['developer']
    apk_instance.developerid=result['developerId']
    apk_instance.developerEmail=result['developerEmail']
    apk_instance.developerWebsite=result['developerWebsite']
    apk_instance.developerInternalID=result['developerInternalID']
    apk_instance.genre=result['genre']
    apk_instance.icon=result['icon']
    apk_instance.screenshots=result['screenshots']
    apk_instance.contentRating=result['contentRating']
    apk_instance.released=result['released']
    apk_instance.updated=result['updated']
    apk_instance.version=result['version']
    apk_instance.synced = True
    apk_instance.last_sync=datetime.now()
    apk_instance.apk=apk_instance.apk
    apk_instance.save()


# @shared_task(queue="parse_market", default_retry_delay=30, max_retries=3)
# def sync_apk_reviews(apk):
#     review_instance = MarketApk.objects.get(id=apk)
#     result = reviews(review_instance.apk, lang='en', country='us', sort=Sort.MOST_RELEVANT, count=100)
#     for review in result:
#         apk_instance.title=result['title']
