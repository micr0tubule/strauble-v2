from news.themes import apple 
from news.themes import tesla  
from news.themes import ai 
from news.themes import Theme 
from news.track import not_sent 

from typing import Dict 

def get_packet(themes) -> Dict:
    packet = {}
    for theme in themes: 
        content = packet[theme] = list(filter(not_sent, theme.fetch())) 
    return packet 


    