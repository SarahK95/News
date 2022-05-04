
import urllib.request,json
from .models import Sources, Articles


# Getting api key
api_key = None

# Getting the source base url
base_url = None

#Getting article url
articles_url = None

def configure_request(app):
    global api_key,base_url,articles_url
    api_key =app.config['NEWS_API_KEY']
    base_url=app.config['NEWS_SOURCES_BASE_URL']
    articles_url=app.config['NEWS_ARTICLES_BASE_URL']
    
    

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)


    return sources_results

def process_sources(sources_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')
      

        
        source_object = Sources(id,name,description,url,category,country)
        sources_results.append(source_object)

    return sources_results


def get_articles(id):
    '''
    Function that gets the article based on id
    '''
    get_articles_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)


    return articles_results


def process_articles(articles_list):
    '''
    Function that process json for articles
    '''
    articles_results = []
    
    for article_item in articles_list:
        id= article_item.get('id')
        
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')
        if urlToImage:
            
            articles_result = Articles(id,author,title,description,url,urlToImage,publishedAt,content)
            articles_results.append(articles_result)
            
    return articles_results
        
        

