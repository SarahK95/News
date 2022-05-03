from app import app
import urllib.request,json
from .models import Sources, Articles


# Getting api key
api_key = None

# Getting the source base url
base_url = None

#Getting article url
article_url = None

def configure_request(app):
    global api_key,base_url,article_url
    api_key =app.config['NEWS_API_KEY']
    base_url=app.config['NEWS_SOURCES_BASE_URL']
    article_url=app.config['NEWS_ARTICLES_BASE_URL']

