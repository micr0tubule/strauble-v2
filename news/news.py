from news.packer import get_packet
from news.themes import apple, tesla, ai 

import discord 
import random 

class News: 
    def __init__(self, client_reference): 
        self.channels = {
            apple: discord.utils.get(client_reference.guilds[0].channels, id=807817644010242090),
            tesla: discord.utils.get(client_reference.guilds[0].channels, id=807818293146419201), 
            ai: discord.utils.get(client_reference.guilds[0].channels, id=807888261615190017) 
        }
        self.client_reference = client_reference


    async def send(self, themes=None) -> None: 
        news = get_packet(themes) if themes else get_packet(self.channels.keys()) 
        for theme, articles in news.items(): 
            random.shuffle(articles)
            for article in articles: 
                await self.channels[theme].send(article)

