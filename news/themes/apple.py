import requests 
import os 
import time
from typing import List 
from bs4 import BeautifulSoup 
from news.get import get_hacker_news
from news.get import get_timeline
from news.get import get_the_verge
from news.themes.theme import Theme

class Apple(Theme): 

    def __init__(self): 
        super().__init__('apple', keywords=['apple', 'tim cook', 'steve jobs', 'mac', 'iphone', 'ios', 'm1'])
            
    def apple_related(self, string: str) -> bool:
        for keyword in self.keywords:  
            if keyword in string.lower(): 
                return True
        return False 

    def filter(self, articles) -> List[str]: 
        return map(lambda x: x, filter(self.apple_related, articles))

    def fetch(self) -> List[str]: 
        content = []
        content.extend(get_the_verge(self.name))
        content.extend(self.filter(get_hacker_news())) 
        content.extend(get_timeline('markgurman', 5))
        return content 

