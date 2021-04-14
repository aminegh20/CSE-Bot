import discord
import random
from discord import colour
from discord import message
from discord.embeds import EmptyEmbed
from discord.ext import commands
from discord.ext.commands.errors import MemberNotFound

class Action(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        description = f'{ctx.message.author.name} slaps {member.display_name}!'
        slap_gifs = open('C:\\Users\\PC\\Desktop\\Discord\\CSE Bot\\cogs\\slap.txt', 'r').read().split('\n')

        if (ctx.message.author.id == member.id):
            description = "Don't slap yourself... I'll slap you instead!"

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_author(name=description, icon_url=ctx.message.author.avatar_url)
        embed.set_image(url=random.choice(slap_gifs))
        await ctx.send(embed=embed)
    
    @commands.command()
    async def spank(self, ctx, member: discord.Member):
        description = f'{ctx.message.author.name} spanks {member.display_name}!, uWu!!'
        spank_gifs = open('C:\\Users\\PC\\Desktop\\Discord\\CSE Bot\\cogs\\spank.txt', 'r').read().split('\n')

        if (ctx.message.author.id == member.id):
            description = "Man, I think it's better if you see a doctor..."

        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name=description, icon_url=ctx.message.author.avatar_url)
        embed.set_image(url=random.choice(spank_gifs))
        await ctx.send(embed=embed)

    @commands.command()
    async def kill(self, ctx, member: discord.Member):
        description = f'{ctx.message.author.name} kills {member.display_name}!, RIP!!'
        kill_gifs = open('C:\\Users\\PC\\Desktop\\Discord\\CSE Bot\\cogs\\kill.txt', 'r').read().split('\n')
        
        if (ctx.message.author.id == member.id):
            description = "Nuu don't kill yourself..."

        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(author=description, icon_url=ctx.message.author.avatar_url)
        embed.set_image(url=random.choice(kill_gifs))
        await ctx.send(embed=embed)
    
    @commands.command()
    async def bully(self, ctx, member: discord.Member):
        description = f'{ctx.message.author.name} bullies {member.display_name}!, LMAO!!'
        bully_gifs = open('C:\\Users\\PC\\Desktop\\Discord\\CSE Bot\\cogs\\bully.txt', 'r').read().split('\n')

        if (ctx.message.author.id == member.id):
            description = "Honestly, I've never seen someone bully themselves..."

        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name=description, icon_url=ctx.message.author.avatar_url)
        embed.set_image(url=random.choice(bully_gifs))
        await ctx.send(embed=embed)

    @commands.command()
    async def whip(self, ctx, member: discord.Member):
        description = f'{ctx.message.author.name} whips {member.display_name}!, ouchh!!'
        whip_gifs = open('C:\\Users\\PC\\Desktop\\Discord\\CSE Bot\\cogs\\bully.txt', 'r').read().split('\n')
        is_aziz = True

        if (ctx.message.author.id == member.id):
            description = "Honestly, I've never seen someone whip themselves..."
        
        if (ctx.message.author.id != 186542557432512513):
            description = f'Sorry, only {ctx.message.author.name} possesses this sacred power.'
            is_aziz = False

        if is_aziz:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_author(name=description, icon_url=ctx.message.author.avatar_url)
            embed.set_image(url='https://media1.tenor.com/images/bcb5a1c9b343a27c440b962d3e867d9f/tenor.gif?itemid=15788990')
            await ctx.send(embed=embed)
        else:
            await ctx.send(description, delete_after=15)

    @slap.error
    async def slap_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'{ctx.message.author.mention}, are you trying to slap air or something?', delete_after=20)
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(f'Unfortunately, you are trying to slap something or someone that might not have a discord account :(', delete_after=20)
    
    @spank.error
    async def spank_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'{ctx.message.author.mention}, I mean I get that you\'re into spanking but at least try to spank something', delete_after=20)
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(f'Unfortunately, you are trying to spank something or someone that might not have a discord account :(', delete_after=20)
    
    @kill.error
    async def kill_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'{ctx.message.author.mention}, you need to kill something man :/', delete_after=20)
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(f'Unfortunately, you are trying to kill something or someone that might not have a discord account :(', delete_after=20)
    
    @bully.error
    async def bully_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'{ctx.message.author.mention}, you need to bully something man :/', delete_after=20)
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(f'Unfortunately, you are trying to bully something or someone that might not have a discord account :(', delete_after=20)

def setup(client):
    client.add_cog(Action(client))