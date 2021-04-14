import discord
import random
from discord.ext import commands

class Fun(commands.Cog):
    
    def __init__(self, client):
        self.client = client
  
    @commands.command()
    async def ping(self, ctx):
        responses = ['Milia with us?', 'Pong!']
        await ctx.send(f'{random.choice(responses)} {round(self.client.latency * 1000)}ms')
    
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = open('C:\\Users\\PC\\Desktop\\Discord\\CSE Bot\\cogs\\8ball.txt', 'r').read().split('\n')
        await ctx.send(f'**Question**: {question}\n**Answer**: {random.choice(responses)}')

def setup(client):
  client.add_cog(Fun(client))