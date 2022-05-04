from flask import render_template,request,redirect,url_for
from app import app
from .request import get_sources, get_articles
from .models import Sources


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    
    new_general = get_sources('general')
    new_tech = get_sources('technology')
    new_sports = get_sources('sports')
    new_entertainment = get_sources('entertainment')
    new_business = get_sources('business')
    new_health = get_sources('health')
    new_beauty = get_sources('beauty')

    title = 'Home - Best News!'
    search_news = request.args.get('news_query')
    
    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:    
        
       return render_template('index.html', title = title, new_general =new_general, new_tech = new_tech, new_sports=new_sports,new_entertainment=new_entertainment,new_business=new_business,new_health=new_health, new_beauty=new_beauty)


@app.route('/articles/<id>')
def articles(id):
    
    '''
    View news page function that returns the news details page and its data
    '''
    
    print('test')
    print(id)
    articles = get_articles(id)
    # print(articles)
    title = f'NH | {id}'
    return render_template('articles.html',title=title, articles=articles)