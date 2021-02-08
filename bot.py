import discord 
from news import News 
from news.themes import ai 
from roles import Roler

intents = discord.Intents().all()
client = discord.Client(intents=intents)
TOKEN = 'NzcxNDk1NDY5MjEyODkzMjA1.X5s9JQ.GOJ9sBv6RfV_5HwX-KR0QgHzdho'

roler = Roler()
client.event(roler.on_reaction_add)
client.event(roler.on_raw_reaction_remove) 

@client.event 
async def on_ready(): 
    roler.init(client)
    news = News(client)
    await roler.construct_gamer_message()


@client.event 
async def on_message(message): 
    pass 

client.run(TOKEN)