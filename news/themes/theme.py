from bs4 import BeautifulSoup

class Theme: 
    def __init__(self, name:str, keywords:str=[]):
        self.name = name 
        self.keywords = keywords 

