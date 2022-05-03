import unittest
from models import Sources, Articles


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
              
        
   
   