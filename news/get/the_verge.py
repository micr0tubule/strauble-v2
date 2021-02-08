from bs4 import BeautifulSoup 
import requests

def get_the_verge(theme):     
    html = requests.get(f'https://www.theverge.com/{theme}').content
    soup = BeautifulSoup(html, 'html.parser')
    return list(map(lambda x: x['href'], soup.find_all(attrs={'data-analytics-link': 'article'}))) 