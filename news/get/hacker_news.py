from bs4 import BeautifulSoup 
import os
import requests 
from functools import lru_cache
from itertools import count 


@lru_cache(maxsize=1)
def get_hacker_news(num_pages:int=1): 

    def get_page(num): 
        res = requests.get(f'https://news.ycombinator.com/news?p={num}')
        if res.status_code != 200: 
            raise Exception
        html = res.content
        soup = BeautifulSoup(html, 'html.parser')
        links = list(map(lambda x: x['href'], soup.findAll('a', {'class': 'storylink'})))
        return links 

    total_links = []

    if num_pages == 0: 
        c = count()
        while True: 
            try: 
                total_links.extend(get_page(next(c)+1)) 
            except Exception as e:
                print(e) 
                break 
    else: 
        for i in range(num_pages): 
            try: 
                total_links.extend(get_page(i+1))
            except:
                break

    return total_links 