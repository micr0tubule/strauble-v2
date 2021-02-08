import discord 
from discord.utils import get 
from functools import partial 
from collections import defaultdict

LEAGUE_OF_LEGENDS = 1
STRONGHOLD_CRUSADER = 2 
OVERWATCH = 3 
AGE_OF_EMPIRES = 4

class Roler: 
    def init(self, client_reference): 
        self.client_reference = client_reference 
        self.channel = get(client_reference.guilds[0].channels, id=808127200175587378)

        self.emotes = {
            LEAGUE_OF_LEGENDS: 808028912025862225, 
            STRONGHOLD_CRUSADER: 808030214671695893, 
            OVERWATCH: 808029169958518804, 
            AGE_OF_EMPIRES: 808029955870556190
        }
        self.roles = { 
            LEAGUE_OF_LEGENDS: 806849998755069982,   
            STRONGHOLD_CRUSADER: 803599774610620466,
            OVERWATCH: 807770425114886155, 
            AGE_OF_EMPIRES: 807770557084074044
        }

    def get_emoji_name(self, id): 
        return dict(map(reversed, self.emotes.items()))[id]

    def get_role_name(self, id): 
        return dict(map(reversed, self.roles.items()))[id]

    def get_emoji(self, name): 
        id = self.emotes.get(name, None)
        return self.client_reference.get_emoji(id) 

    def get_role(self, name): 
        id = self.roles.get(name, None)
        return get(self.client_reference.guilds[0].roles, id=id)


    async def on_reaction_add(self, reaction, user):
        role = self.get_role(self.get_emoji_name(reaction.emoji.id))
        if not role or reaction.message.channel != self.channel or user.bot:
            return  
        await user.add_roles(role)         


    async def on_raw_reaction_remove(self, reaction): 
        user = self.client_reference.guilds[0].get_member(reaction.user_id)
        channel = get(self.client_reference.guilds[0].channels, id=reaction.channel_id)
        name = self.get_emoji_name(reaction.emoji.id)
        role = self.get_role(name)
        if not self.channel == channel or user.bot and not role == None:
            return 
        await user.remove_roles(role)

    
    async def construct_gamer_message(self): 
        self.gamer_message = await self.channel.send('bist du ein gamer?')
        for name in self.emotes.keys(): 
            await self.gamer_message.add_reaction(self.get_emoji(name))
    

    async def handle_reactions(self):
        while True:   
            reaction = await self.client_reference.wait_for_reaction(self.league_of_legends)


