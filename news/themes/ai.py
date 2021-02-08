
from news.themes.theme import Theme 
import requests
from bs4 import BeautifulSoup 

from typing import List 
from news.get import get_hacker_news 
from news.get import get_the_verge
from news.get import get_timeline

class AI(Theme): 
    def __init__(self): 
        super().__init__('ai', keywords=['autopilot', 'artificial', 'artificial intelligence', 'artificial-intelligence', 'machine learning', 'openai', 'deepmind', 'datascience', 'reinforcement learning', 'deeplearning'])
    
    
    def fetch_hacker_news(self): 
        return list(map(lambda x: x, filter(self.tesla_related, get_hacker_news(0))))  

    def ai_related(self, string:str) -> bool: 
        for keyword in self.keywords:  
            if keyword in string.lower(): 
                return True
        return False 

    def filter(self, articles):
        return map(lambda x: x, filter(self.ai_related, articles))
        
    def fetch(self): 
        content = []
        content.extend(get_the_verge('ai-artificial-intelligence'))
        content.extend(self.filter(get_hacker_news())) 
        return content
    
