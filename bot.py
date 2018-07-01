import discord
import asyncio
import requests
import os
from discord.ext.commands import Bot
from discord.ext import commands
import random

Client = discord.Client()
bot_prefix='!!'
client = commands.Bot(command_prefix=bot_prefix)
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot Online")
    print("Name: (Diamond4Bot)".format(client.user.name))
    print("ID: ()".format(client.user,id))
    await client.change_presence(game=discord.Game(name='type !!help')                              

@client.command(pass_context=True)
async def power(ctx):
    power = open('power.txt').read().splitlines()
    power2 = random.choice(power)
    if ctx.message.author.id == "206027308149112832":
        await client.say("<@!206027308149112832> You can fly!")
    else:
        await client.say('%s Your hidden power is: %s' % (ctx.message.author.mention, power2))
                    
@client.command(pass_context=True)
async def logs(ctx):
    embed = discord.Embed(title="All the changelogs here!", color=0xE90FF)
    embed.add_field(name="New Command!", value="Do !!hero to see other's secret hero skills! Added in 16/3/2018.")
    embed.add_field(name="New Command!", value="Do !!waud to see what other memebrs are doing. Added in 26/2/2018.")
    embed.add_field(name="Minor Update!", value="Every embed should have colours now! Updated in 13/1/2018.")
    embed.add_field(name="Updated Command!", value="Updated the !!help command. This time, it's an embed! Updated in 13/1/2018.")
    embed.add_field(name="New Command!", value="Do !!suggest to suggest me something. Added in 13/1/2018.")
    embed.add_field(name="New Command!",value="Do !!yon to play a game of Yes or No! Added in 13/1/2018.")
    embed.add_field(name="New Command!",value="Do !!changelog to see all the changes made to this bot! Added in 13/1/2018.")
    embed.add_field(name="New Command!",value="Do !!wyr to play a game of Would You Rather! Do !!wyr add (line) to add your own Would You Rather! Added in 8/1/2018.")
    await client.say(embed=embed)

@client.group(pass_context=True, invoke_without_command=True)
async def yon(ctx):
    yesornolist = open('yesorno.txt').read().splitlines()
    yesornolist2 = random.choice(yesornolist)
    yon = await client.say(" {} Choose Y or N .".format(yesornolist2))
    await client.add_reaction(yon,'\U0001f1fe')
    await client.add_reaction(yon,'\U0001f1f3')
    
@yon.command(pass_context=True)
async def add(ctx,*, string):
    yonopen = open("yesorno.txt", "a")
    yonopen.write("\n{}".format(string))
    yonopen.close()
    await client.say("Added!")
    
@client.group(pass_context=True, invoke_without_command=True)
async def wyr(ctx):
    wyrlist = open('wyr.txt').read().splitlines()
    wyrlist2 = random.choice(wyrlist)
    wyr = await client.say("Would you rather {}? Choose A or B.".format(wyrlist2))
    await client.add_reaction(wyr,'\U0001f170')
    await client.add_reaction(wyr,'\U0001f171')
    
@wyr.command(pass_context=True)
async def add(ctx,*, string):
    wyropen = open("wyr.txt", "a")
    wyropen.write("\n{}".format(string))
    wyropen.close()
    await client.say("Added!")
    
@client.command(pass_context=True)
async def kill(ctx):
    kill = open('Deaths.txt').read().splitlines()
    death = random.choice(kill)
    victim = random.choice([x for x in ctx.message.server.members if not x.bot])
    killer = random.choice([x for x in ctx.message.server.members if not x.bot])
    embed = discord.Embed(title='A crime has been commited!', description = '{} killed {} {}!'.format(victim.display_name, killer.display_name, death))
    await client.say(embed=embed)

@client.command(pass_context=True)
async def game(ctx):
    game = open('Games.txt').read().splitlines()
    games = random.choice(game)
    if ctx.message.author.id == "206027308149112832":
        await client.say("<@!206027308149112832> you like to play Clash Royale!")
    else:
        await client.say('%s you like to play %s' % (ctx.message.author.mention, games))

@client.command(pass_context=True)
async def job(ctx):
    job = open('jobs.txt').read().splitlines()
    jobs = random.choice(job)
    if ctx.message.author.id == "206027308149112832":
        await client.say("<@!206027308149112832> you work as a: Chef")
    else:
        await client.say('%s you work as a: %s' % (ctx.message.author.mention, jobs))
        
@client.command(pass_context=True)
async def moti(ctx): 
    moti = open('moti.txt').read().splitlines()
    motivation = random.choice(moti)
    embed = discord.Embed(title="%s", description='%s'(ctx.message.author.mention, motivation)
    embed.set_image(url='https://cdn.discordapp.com/attachments/385416830229151746/462809050053345322/images.jpg)
    await client.say(embed=embed)
                    
@client.command(pass_context=True)
async def love(ctx):
    love = random.choice([x for x in ctx.message.server.members if not x.bot])
    love2 = random.choice([x for x in ctx.message.server.members if not x.bot])
    embed = discord.Embed(title="Two humans in love", description = '**{}** is in love with **{}**!'.format(love.display_name, love2.display_name),color=0xE90FF)
    embed.set_image(url='https://cdn.discordapp.com/attachments/385419071727992834/395219142325698562/love.jpg')
    await client.say(embed=embed)

@client.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title='EMBED PLZ WORK', description='PLEASE MAKE THIS WORK')
    embed.set_image(url='https://cdn.discordapp.com/attachments/385419071727992834/393317821381345280/Wrong.png')
    await client.say(embed=embed)

@client.command(pass_context=True)
async def waud(ctx):
    waud = open('WAUD.txt').read().splitlines()
    wauds = random.choice(waud)
    waudper = random.randint(0, 100)
    waudhum = random.choice([x for x in ctx.message.server.members if not x.bot])
    await client.say(' {}, you are {}. If I had to guess, the chance of you doing that right now is {}%.'.format(waudhum.display_name,wauds,waudper))
    
@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")

@client.command(pass_context=True)
async def flip(ctx):
    flip = random.choice(["Heads","Tails","DA MIDDLE"])
    await client.say(flip)

@client.command(pass_context=True)
async def amIgay(ctx):
    Areyougay = random.choice(["Maybe","YES,DUH","NOPE"])
    await client.say(Areyougay)

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Every command in one place!",color=0xE90FF)
    embed.add_field(name="Games!", value="``howIkms``,``amIgay``,``wyr``,``wyr add``,``yon``,``yon add``")
    embed.add_field(name="Real Life Related! _not real_",value="``waud`` ``chance``,``ask``,``future``,``number``,``badnumber``,``love``,``job``,``game``,``kill``,``flip``")
    embed.add_field(name="Bot Stuff!", value="``ping``,``logs``,``suggest``")
    await client.say(embed=embed)
    
@client.command(pass_context=True)
async def howIkms(ctx):
    kms = random.choice (["Jumping off from Trump's wall","Eating too much KFC","Assassinated by Kim Jong Un","Be surrounded by gay people","Killed by a goddamn clown","Having Ebola, Cancer and Depression at the same time","Be surrounded by creepers","Meeting Herobrine for the first time","Attempting to kill hackers","Being as old as 9999 years old","People calling you cringy/idiot"])
    await client.say(kms)

@client.command(pass_context=True)
async def pong(ctx):
    await client.say("Ping!")

@client.command(pass_context=True)
async def pingpong(ctx):
    await client.say("Pong Ping!")

@client.command(pass_context=True)
async def pongping(ctx):
    await client.say("Ping Pong Pung!")

@client.command(pass_context=True)
async def pung(ctx):
    await client.say("What do you expect me to say, huh? PINGPONGPUNGPUN?!")

@client.command(pass_context=True)
async def ask(ctx,*, string):
    ask = random.choice([x for x in ctx.message.server.members if not x.bot])
    await client.say("The winner of ``%s`` is ``%s``" % (string, ask.display_name))

@client.command(pass_context=True)
async def chance(ctx):
    luck = random.choice(["Try again later","Maybe","NOPE","50% chance","Definitely not","Yes, definitely","It depends on your fate","Dunno, maybe ask the owner of this bot?"])
    await client.say(luck)

@client.command(pass_context=True)
async def future(ctx):
    future = random.choice (["In the future, you may die early.","In the future,you may find a cute girl but didn't have a stable family.","In the future, you may found a rich girl, but she kept arguing with you. A few days later, you divorced her, and got depression until you got another relationship.","In the future, you found a braniac girl, but she is loyal to you and you got married happily. You got a good family and died in the age of 100.","In the future, you got your dream job, got a good wife, and got 2 good kids. You died in the age of 120.","In the future, you got your dream job, but your boss wants to fire you asap, so after working for a year, you got fired for no reason.","In the future, you didn't got your dream job, but the salary is high and your co-workers and your boss treats you like a family. You found love there too, and died in the age of 90 with happiness.","In the future,you won the lottery, and you earned 1$.","In the future, you won the lottery of 1 million dollars.","In the future, you bought a ticket for the lottery, but unluckily you lost.","In the future, you were forced to be in war. You died in the battlefield, but hey at least your name will be famous...","In the future, you died pretty early because you fell from a mountain.","`In the future, you met some famous youtubers, and they chose you as their sidekick.","In the future, you got what normal people do.A normal job, a normal family and a normal life. You died because of being too normal.","In the future, you became a millionaire and because of that, you donated a heck ton of money to the needy. In fact, you donated A LOT until you became famous and loved by everyone.",])                               
    await client.say(future)
    
@client.command(pass_context=True)
async def number(ctx):
    luck = random.randint(0, 100)
    await client.say('Your lucky number for today is ``{0}``! Go use that number and win good stuff!'.format(luck))

@client.command(pass_context=True)
async def badnumber(ctx):
    badnumber = random.randint(0,100)
    await client.say('Your unlucky number for today is ``{0}``! Try not to use this number or you will face the consequences...'.format(badnumber))

client.run(str(os.environ.get('BOT_TOKEN')))



