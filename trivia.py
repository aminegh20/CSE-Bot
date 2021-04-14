import asyncio
import discord
import random
from discord import message
from discord.ext import commands
from asyncio.tasks import wait_for

class Trivia(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def trivia(self, ctx):

        #prompt user to enter a trivia theme
        tutorial = discord.Embed(title="Trivia tutorial", description=f'Welcome {ctx.message.author.mention} to CSE Trivia. To start playing, please select a theme:\nCSE')
        await ctx.send(embed=tutorial)

        #current possible themes
        themes = ["CSE"]

        def check(m): # m = discord.Message
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id and m.content.upper() in themes

        try:
            #wait for user to enter a theme
            msg = await self.client.wait_for("message", check=check, timeout=60)

        #if timed out, abort session
        except asyncio.TimeoutError:
            await ctx.send(f'**Sorry {ctx.message.author.name}, you have timed out :(**', delete_after=15)
            return

        else:
            #otherwise send the user the guidelines
            guidelines = discord.Embed(title="**Trivia Guidelines**", description = open('C:\\Users\\PC\\Desktop\\Discord\\CSE Bot\\cogs\\guidelines.txt', 'r').read(), colour=discord.Colour.green())
            await ctx.send(embed=guidelines)

            def confirm(m): # m = discord.Message
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id and m.content.upper() in ['YES', 'CANCEL', 'QUIT']
            
            try:
                #wait for confirmation
                msg2 = await self.client.wait_for("message", check=confirm, timeout=60)
            
            #if timed out, abort session
            except asyncio.TimeoutError:
                await ctx.send(f'**Sorry {ctx.message.author.name}, you have timed out :(**', delete_after=15)
                return
            else:
                #if user wants to quit, abort session
                if msg2.content.upper() in ['CANCEL', 'QUIT']:
                    await ctx.send("Trivia session was aborted!", delete_after=10)
                    return
                else:
                    #otherwise, start trivia after 5 seconds
                    await ctx.send(f'{ctx.message.author.mention}, trivia will begin in 5 seconds, be ready!', delete_after=5)
                    await asyncio.sleep(4)

                    #to store trivia content
                    content = []

                    #quiz is a list of lists where each inner list represents a question
                    quiz = []

                    #read trivia content as a list from a file
                    with open('C:\\Users\\PC\\Desktop\\Discord\\CSE Bot\\trivia\\cse.txt') as file:
                        content = [line.strip('\n') for line in file]

                    #separate content into blocks of 6 each containing a question, the possible answers and the answer itself
                    for i in range(0, len(content) - 5, 6):
                        question = []
                        question.append(content[i])
                        question.append(content[i+1])
                        question.append(content[i+2])
                        question.append(content[i+3])
                        question.append(content[i+4])
                        question.append(content[i+5])
                        quiz.append(question)
                    
                    #store user score
                    score = 0

                    #loop over the questions
                    for i in range(1, 11):
                        await asyncio.sleep(1)    #wait for a second
                        wants_to_quit = False     #keep track if user wants to quit

                        question = discord.Embed(description=quiz[i-1][0])    #create question embed
                        question.set_author(name=f'Question #{i}', icon_url=ctx.message.author.avatar_url)    #set author and avatar url
                        question.add_field(name=f'A) {quiz[i-1][1]}', value='\u2800', inline=False)   #add option A
                        question.add_field(name=f'B) {quiz[i-1][2]}', value='\u2800', inline=False)   #add option B
                        question.add_field(name=f'C) {quiz[i-1][3]}', value='\u2800', inline=False)   #add option C
                        question.add_field(name=f'D) {quiz[i-1][4]}', value='\u2800', inline=False)   #add option D
                        question.set_footer(text=f'{ctx.message.author.name}\'s trivia session\nCategory: {msg.content.upper()}')  #set footer
                        await ctx.send(embed=question)                                                

                        def check_answer(m): # m = discord.Message
                            return m.author.id == ctx.message.author.id and m.channel.id == ctx.channel.id \
                            and m.content.upper() in ['A', 'B', 'C', 'D', 'CANCEL', 'QUIT', 'ABORT']
                        
                        def check_cancel(m): # m = discord.Message
                            return m.author.id == ctx.message.author.id and m.channel.id == ctx.channel.id and \
                            m.content.upper() in ['YES', 'NO']
                        
                        try:
                            #wait for answer
                            answer = await self.client.wait_for('message', check=check_answer, timeout=60)

                            #correct answer
                            if answer.content.upper() == quiz[i-1][5]:
                                score += 1
                            
                            #user wants to quit
                            elif answer.content.upper() in ['CANCEL', 'QUIT', 'ABORT']:
                                wants_to_quit = True
            
                                try:
                                    #ask user for confirmation
                                    await ctx.send(f'{ctx.message.author.mention}, are you sure you want to abort the current session?')

                                    #wait for quitting confirmation
                                    reply = await self.client.wait_for("message", check=check_cancel, timeout=20)

                                    #if confirmed, break the loop
                                    if reply.content.upper() == 'YES':
                                        await ctx.send(f'{ctx.message.author.mention}, you have aborted the trivia session!')
                                        break
                                    
                                    #otherwise resume session
                                    else:
                                        wants_to_quit = False
                                        await ctx.send(f'Resuming Trivia session!')
                                        await asyncio.sleep(1)

                                #if timed out, abort session
                                except asyncio.TimeoutError:
                                    await ctx.send(f'{ctx.message.author.mention}, you have aborted the trivia session!')
                                    break
                        
                        #if question timed out, try to move to next question
                        except asyncio.TimeoutError:

                            #user wants to quit
                            if wants_to_quit:
                                try:
                                    #ask user for confirmation
                                    await ctx.send(f'{ctx.message.author.mention}, are you sure you want to abort the current session?')

                                    #wait for quitting confirmation
                                    reply = await self.client.wait_for("message", check=check_cancel, timeout=20)

                                    #if confirmed, break the loop
                                    if reply.content.upper() == 'YES':
                                        await ctx.send(f'{ctx.message.author.mention}, you have aborted the trivia session!')
                                        break
                                    
                                    #otherwise, resume session
                                    else:
                                        wants_to_quit = False
                                        await ctx.send(f'Resuming Trivia session....')
                                        await asyncio.sleep(1)

                                #if timed out, abort session
                                except asyncio.TimeoutError:
                                    await ctx.send(f'{ctx.message.author.mention}, you have aborted the trivia session!')
                                    break
                            
                            #if user doesn't want to quit, continue normally
                            if not wants_to_quit:
                                continue
                    
                    #send user score
                    await ctx.send(f'{ctx.message.author.mention}, you have scored {score} / 10!')
                    return

def setup(client):
    client.add_cog(Trivia(client))