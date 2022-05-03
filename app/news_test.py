import unittest
from app.models import Sources, Articles


class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''
    
    def setUp(self):
        '''
         Set up method that will run before every Test
         '''
        self.new_source = Sources('dnews', 'Daily News', 'Hourly and timely news on the daily', 'https://google.com', 'sports', 'ke')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))
        
    def test_to_check_instance_variables(self):
        '''
        Test function to check instance variables
        '''
        self.assertEquals(self.new_source.id,'dnews')
        self.assertEquals(self.new_source.name,'Daily News')
        self.assertEquals(self.new_source.description,'Hourly and timely news on the daily')
        self.assertEquals(self.new_source.url,'https://google.com')
        self.assertEquals(self.new_source.category,'sports')
        self.assertEquals(self.new_source.country,'ke')
        
        
class TestArticles(unittest.TestCase):
    '''
    Test class to test the behavior of the articles class
    '''
    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_article = Articles('Rose','Musk does it again','News of Elon Musk buying twitter surprising many','https://google.com','https://google.com/images','2022-05-12T13:31:03Z')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
    
    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.author,'evelyne')
        self.assertEquals(self.new_article.title,'Musk does it again')
        self.assertEquals(self.new_article.description,'News of Elon Musk buying twitter surprising many')
        self.assertEquals(self.new_article.url,'https://google.com')
        self.assertEquals(self.new_article.urlToImage,'https://google.com/images')
        self.assertEquals(self.new_article.publishedAt,'2022-05-12T13:31:03Z')        
        
        
        
        
              
        
   
   