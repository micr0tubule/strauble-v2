from .theme import Theme 
import requests
from bs4 import BeautifulSoup 

from typing import List 
from news.get import get_hacker_news 
from news.get import get_the_verge
from news.get import get_timeline

class Tesla(Theme): 
    def __init__(self): 
        super().__init__('tesla', keywords=['autopilot', 'tesla', 'elon musk'])
    
    def fetch_hacker_news(self): 
        return list(map(lambda x: x, filter(self.tesla_related, get_hacker_news(0))))  

    def tesla_related(self, string:str) -> bool: 
        for keyword in self.keywords:  
            if keyword in string.lower(): 
                return True
        return False 

    def filter(self, articles): 
        return map(lambda x: x, filter(self.tesla_related, articles))

    def fetch(self): 
        content = []
        content.extend(get_the_verge(self.name))
        content.extend(self.filter(get_hacker_news())) 
        content.extend(get_timeline('elonmusk', 5))
        return content
    
