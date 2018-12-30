import discord
import asyncio
import datetime
import random
import os
import sys
import time
import shlex
import shutil
import random
import inspect
import logging
import asyncio
import pathlib
import traceback
import math
import re
import chalk
import requests
import youtube_dl
import json

logging.basicConfig(level=logging.WARNING)

from youtube_dl import YoutubeDL
from discord.voice_client import VoiceClient
from discord.ext import commands
from discord.ext.commands import bot

ydl_options = {
    "format": "bestaudio/best",
    "extractaudio": True,
    "nocheckcertificate": True,
    "ignoreerrors": True,
    "no_warnings": True,
    "verbose": False,
    "skip_download": True
}

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='logging.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(levelname)s: %(name)s: %(message)s. LOGGED AT: %(asctime)s'))
logger.addHandler(handler)

client = discord.Client()

official_prefix = "ty-"
official_prefix_uppercased = "Ty-"
second_prefix = "ti-"
second_prefix_uppercased = "Ti-"
third_prefix = "tcec "
third_prefix_uppercased = "Tcec "
prefix4 = "tb-"
prefix5 = "tech-"
prefix6 = "t-"

bot = commands.Bot(command_prefix=[official_prefix, official_prefix_uppercased, second_prefix, second_prefix_uppercased, third_prefix, third_prefix_uppercased, prefix4, prefix5, prefix6])

os.chdir('C:\Bots\TyBot\TyBot Official\data')

bot.remove_command("help")

owner_id = (["486839970271723521", "389091765686239232"])

version = "Version 9.1"
python_ver = "Python 3.6.6"
discord.py_type = "Rewrite"

print('You have started the following bot:')
print('TechBot')
print("Loading bot... Please be patient.")

#@bot.event use

@bot.event
async def status_task():
    while True:
        activity = discord.Game(name="ty-help - {}".format(version))
        await bot.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(120)
        activity = discord.Game(name="Creators: TYX_YT/TCEC109")
        await bot.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(120)
        activity = discord.Game(name="on {0}, {1}".format(version, discord.py_type))
        await bot.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(120)
        activity = discord.Game(name="on {}".format(python_ver))
        await bot.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(120)
        activity = discord.Game(name="with "f"{len(bot.guilds)}"" server(s)")
        await bot.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(30)
        activity = discord.Game(name="with "f"{len(bot.guilds)}"" server(s)")
        await bot.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(30)
        activity = discord.Game(name="with "f"{len(bot.guilds)}"" server(s)")
        await bot.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(30)
        activity = discord.Game(name="with "f"{len(bot.guilds)}"" server(s)")
        await bot.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(30)

@bot.event
async def on_guild_join(g):
    success = False
    i = 0
    while not success:
        try:
            await g.channels[i].send(f"Hello! Thanks for inviting me to your server. To get more commands, type ty-help.")
        except (discord.Forbidden, AttributeError):
            i += 1
        except IndexError:
            pass
        else:
            success = True

    url = f"https://discordbots.org/api/bots/{bot.user.id}/stats"
    headers = {
        'Authorization': dbltoken,
        'content-type': 'application/json'
    }
    payload = {
        'server_count': len(bot.guilds)
    }

    activity = discord.Game(name="Joined new server! Now on "f"{len(bot.guilds)}"" server(s)")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    await asyncio.sleep(30)
    activity = discord.Game(name="with "f"{len(bot.guilds)}"" server(s)")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    await asyncio.sleep(30)
    activity = discord.Game(name="with "f"{len(bot.guilds)}"" server(s)")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    await asyncio.sleep(30)
    activity = discord.Game(name="with "f"{len(bot.guilds)}"" server(s)")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    await asyncio.sleep(30)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=":x: Error!", description="You just passed the wrong argument.", colour=0xEE2C2C)
        embed.add_field(name="For advanced users, here is the log:", value="```{}```".format(error), inline=False)
        await ctx.send(embed=embed)
        print("Most recent callback:")
        print(error)
        file = open('logs.log','a')
        file.write('\nMost recent callback error: {}\n'.format(error))
        file.close()
    else:
        if isinstance(error, commands.BotMissingPermissions):
                embed = discord.Embed(title="Are you sure about that?", description="The command cannot be used. But, don't worry! This is a easy error to be solved with. Just go to my role and enable the permission that is needed, or to tell your server administrator to fix it.", colour=0xFFFF00, timestamp=datetime.datetime.utcnow())
                embed.add_field(name="For advanced users, here is the log:", value="```{}```".format(error), inline=False)
                await ctx.send(embed=embed)
                print("Most recent callback:")
                print(error)
                file = open('logs.log','a')
                file.write('\nMost recent callback error: {}\n'.format(error))
                file.close()
        else:
                if isinstance(error, commands.CommandInvokeError):
                    embed = discord.Embed(title=":x: Error!", description="An error occured while trying to use the command.", colour=0xEE2C2C, timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="This might help you out, at least a bit.", value="```{}```".format(error), inline=False)
                    await ctx.send(embed=embed)
                    print("Most recent callback:")
                    print(error)
                    file = open('logs.log','a')
                    file.write('\nMost recent callback error: {}\n'.format(error))
                    file.close()
                else:
                        if isinstance(error, commands.DisabledCommand):
                            embed = discord.Embed(title=":x: Error!", description="This command is disabled.", color=0xFFFF00, timestamp=datetime.datetime.utcnow())
                            embed.add_field(name="For advanced users, here is the log:", value="```{}```".format(error), inline=False)
                            await ctx.send(embed=embed)
                            print("Most recent callback:")
                            print(error)
                            file = open('logs.log','a')
                            file.write('\nMost recent callback error: {}\n'.format(error))
                            file.close()
                        else:
                            if isinstance(error, discord.errors.Forbidden) or isinstance(error, discord.Forbidden):
                                pass

def is_owner():
    async def predicate(ctx):
        return ctx.author.id == 389091765686239232
    return commands.check(predicate)
                    
        
@bot.event
async def find_channel(guild):
    for c in guild.text_channels:
        if not c.permissions_for(guild.me).send_messages:
            continue
        return c

@bot.event
async def on_ready():
    file = open('logs.log','a')
    file.write('\nBot Status: Online\n')
    file.close()
    print('You started the following bot:')
    print(bot.user.name)
    print(bot.user.id)
    print('Status: Online')
    print("Ping (ms):")
    print(f"This took {bot.ws.latency * 1000:.0f} ms.")
    print('Discord.py Version: {}'.format(discord.__version__))
    print("This bot is on "f"{len(bot.guilds)}"" servers.")
    print('-------------------------------------------------')
    print('Other command scripts, exceptions and errors will be informed down here:')
        
    bot.loop.create_task(status_task())

#@bot.command use, non-administrator commands

@bot.command()
async def intel(ctx):
    user = ctx.message.author
    embed = discord.Embed(title="Choose a category", description="You can only choose one at a time. You have 30 seconds.", color=0x3498db)
    embed.add_field(name="Number 1", value="Intel Core i3 vs. i5 vs. i7: Which one do you really need?", inline=False)
    embed.set_author(name="Pick a number", icon_url='https://www.bhphotovideo.com/images/images2500x2500/intel_bx80673i97940x_core_i9_7940x_x_series_3_1_1361950.jpg')
    embed.set_thumbnail(url='https://www.intel.com/content/dam/products/hero/foreground/badge-9th-gen-core-i9-1x1.png.rendition.intel.web.128.128.png')
    await ctx.send(embed=embed)

    def pred(m):
        return m.author == ctx.author and m.channel == ctx.channel
    try:
        response = await bot.wait_for('message', check = pred, timeout = 30)
    except asyncio.TimeoutError:
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title="Cancelled.", description="{0}, you just reached the time limit of 30 seconds. If you wanted to cancel, just say no. If you were planning to not skip the command, but you were not replying, so I cancelled it.".format(user, ctx.message.author), color=0xFF3030, timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=embed)
    else:
        if response.clean_content.lower() == 'no':
            await ctx.channel.purge(limit=2)
            embed = discord.Embed(title="You have cancelled the command.", description="If you are planning to use this command again, please type `ty-intel` again.", inline=False)
            await ctx.send(embed=embed)
        else:
                if response.clean_content.lower() == '1':
                    await ctx.channel.purge(limit=2)
                    embed = discord.Embed(title="Page 1 - Intel Core i3 vs. i5 vs. i7: Which one do you really need?", description="So, which processor do you really need in business, gaming, or something that is strong at handling a lot of tasks, etc? Do you use it for gaming? I think this would be a great choice for a Intel Core i7, instead of i5 or i3. If you are using it for high-end tasks, a core i5 can handle it. Or, core i7. In mid-range, I should say that i5 is good enough for you. For basic tasks like browsing the web, an i3 will be good enough for it.".format(user, ctx.message.author), colour=0x3498db, timestamp=datetime.datetime.utcnow())
                    embed.set_thumbnail(url='https://static.makeuseof.com/wp-content/uploads/2016/05/intel-core-i3-i5-i7-processor-logos.png')
                    embed.add_field(name="Well... First of all.", value="A Core i7 does not mean a seven-core processor! These are just names to indicate relative performance. Typically, the Core i3 series has only dual-core processors, while the Core i5 and Core i7 series have both dual-core and quad-core processors. Quad-cores are usually better than dual-cores, but don’t worry about that just yet.", inline=False)
                    embed.add_field(name="'Families' of Intel Cores", value="Intel releases “families” of chipsets, called generations. The current one is the 9th-generation series called Cannon Lake. They are 9th generation processors. Each family, in turn, has its own line of Core i3, Core i5, and Core i7 series of processors. The generations will chsnge every single time when Intel puts a new number into its name. For example, this Intel Core i7-8700K has the number '8' in the first place, but the Intel Core i7-9800K has the number '9' in the first place, and it means that the Core i7-8700K is a 8th generation processor, and a Core i7-9800K is a 9th generation processor. It most likely changed the first number, which is the number '8' to '9'.", inline=False)
                    await user.send(embed=embed)
                    await user.send("Next page is coming up at 20 seconds. You can keep reading.")
                    await asyncio.sleep(20)
                    embed = discord.Embed(title="Page 2 - What Intel’s Model Numbers Mean: U vs. Q vs. H vs. K", description="So, which processor do you really need in business, gaming, or something that is strong at handling a lot of tasks, etc? Do you use it for gaming? I think this would be a great choice for a Intel Core i7, instead of i5 or i3. If you are using it for high-end tasks, a core i5 can handle it. Or, core i7. In mid-range, I should say that i5 is good enough for you. For basic tasks like browsing the web, an i3 will be good enough for it.".format(user, ctx.message.author), colour=0x3498db, timestamp=datetime.datetime.utcnow())
                    embed.set_thumbnail(url='https://static.makeuseof.com/wp-content/uploads/2016/05/intel-core-i3-i5-i7-processor-logos.png')
                    embed.set_image(url="https://static.makeuseof.com/wp-content/uploads/2016/05/intel-core-i3-i5-i7-product-name.jpg")
                    embed.add_field(name="U: Ultra Low Power.", value="The U rating is only for laptop processors. These draw less power and are better for the battery.", inline=False)
                    embed.add_field(name="Y: Low Power.", value="Typically found on older generation laptop and mobile processors.", inline=False)
                    embed.add_field(name="T: Power Optimized.", value="Power optimized for desktop processors.", inline=False)
                    embed.add_field(name="Q: Quad-Core.", value="The Q rating is only for processors with four physical cores.", inline=False)
                    embed.add_field(name="H: High-Performance Graphics.", value="The chipset has one of Intel’s better graphics units in it.", inline=False)
                    embed.add_field(name="G: Includes Discrete Graphics.", value="Typically found on laptops, this means there is a dedicated GPU with the processor.", inline=False)
                    embed.add_field(name="K: Unlocked.", value="This means you can overclock the processor above its rating.", inline=False)
                    embed.add_field(name="Do you understand the letters now?", value="Understanding these letters and the numbering system above will help you know what a processor offers just by looking at the model number, without needing to read the actual specifications. Of course, before making a buying decision, it’s advisable to check the details at ark.intel.com.", inline=False)
                    await user.send(embed=embed)
                    await ctx.send("Next page coming up in 15 seconds.")
                    await asyncio.sleep(15)

@bot.command()
async def help(ctx):
    myself = ctx.message.author
    await ctx.send(":white_check_mark:")
        
    
    embed = discord.Embed(title="TechBot Commands", description="Here are my commands:", colour=0x3498db)
    embed.add_field(name="Non-Admin Commands:", value="Here are the commands for everyone", inline=False)
    embed.add_field(name="ty-botinfo", value="Gives you bot info", inline=False)
    embed.add_field(name="ty-ping @mention", value="Pings someone", inline=False)
    embed.add_field(name="ty-randomnumber", value="Gives you a random number from 10 to 100", inline=False)
    embed.add_field(name="ty-servercount", value="Says how many servers there is the bot", inline=False)
    embed.add_field(name="ti-embed <message>", value="Embeds your message", inline=False)
    embed.add_field(name="ti-memberscount", value="Tells you how many people there is on the server", inline=False)
    embed.add_field(name="ti-info @mention", value="Gives you info of the member", inline=False)
    embed.add_field(name="ti-serverinfo", value="Gives you server information", inline=False)
    embed.add_field(name="ti-create_poll <message>", value="Create a poll, but you add reaction (i don't know why i made this since there is embed already...", inline=False)
    embed.add_field(name="ti-ao <message>", value="Prints your message on TiBot Shell", inline=False)
    embed.add_field(name="ti-copy <message>", value="Copies Your Message", inline=False)
    embed.add_field(name="ti-write_message <message>", value="Write your message on TiBotMessages.txt (no, i'm serious)", inline=False)
    embed.add_field(name="ti-userid <userid>", value="Gives you info of a user ID", inline=False)
    await myself.send(embed=embed)
    await asyncio.sleep(1)
    
    embed = discord.Embed(title="Administrator Commands:", description="Only administrators can use it.", colour=0x3498db)
    embed.add_field(name="ti-kick @mention <reason>", value="Kicks someone", inline=False)
    embed.add_field(name="ti-ban @mention <reason>", value="Bans someone", inline=False)
    embed.add_field(name="ti-warn @mention <reason>", value="Warns someone", inline=False)
    embed.add_field(name="ti-clear <amount>", value="Clears messages with your amount", inline=False)
    embed.add_field(name="ti-hackban <userid>", value="Hack ban someone", inline=False)
    await myself.send(embed=embed)

@bot.command()
async def membercount(ctx):
    embed = discord.Embed(title="Members count", description="These are the members that are in this server.", colour=0x3498db, timestamp=datetime.datetime.utcnow())
    humanCount = len([member for member in ctx.guild.members if not member.bot])
    botCount = len([member for member in ctx.guild.members if member.bot])
    embed.add_field(name="Members", value=humanCount, inline=False)
    embed.add_field(name="Bots", value=botCount, inline=False)
    embed.add_field(name="Total", value= (humanCount + botCount), inline=False)
    await ctx.send(embed=embed)            
    
@bot.command()
async def mention(ctx, user: discord.Member):
    myself = ctx.message.author
    embed = discord.Embed(title=":white_check_mark: I've successfully mentioned the user.", description="{0.mention} has been mentioned by {1}.".format(user, ctx.message.author), colour=0x3498db, timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Note!", value="This command cannot send what you're saying in DMs, but only to mention him. The reason of it is that they can be used on blocked people, and it is not allowed.", inline=False)
    await ctx.send(embed=embed)
    embed = discord.Embed(title="You got a mention from the following person and the server:", description="The mention is from **{0}**, and the person who mentioned was {1.mention}.".format(ctx.guild.name, ctx.message.author), colour=0x3498db, timestamp=datetime.datetime.utcnow())
    await user.send(embed=embed)    
    print("{1} mentioned {0}.".format(user, ctx.message.author))

#@bot.command, administrator commands

@bot.command()
async def kick(ctx, member: discord.User = None, *, reason = None):
    author = ctx.message.author
    if member == None or member == ctx.message.author:
        await ctx.send("You can't kick yourself!")
        return
    if reason == None:
        reason = "Unspecified reason."
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("This command is not usable unless you're an administrator.")
    else:
        await ctx.guild.kick(member)
        await ctx.send('**{0}** has been kicked by {1.mention}, with the reason "**{2}**".'.format(member, ctx.message.author, reason))
        embed = discord.Embed(title="You have a important message!", description="You were kicked out from **{0}**.".format(ctx.guild.name), color=0xFF3030, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Here is the reason:", value="```{}```".format(reason), inline=False)
        embed.add_field(name="This is the person who kicked you:", value="{0.mention}".format(ctx.message.author))
        embed.add_field(name="Note!", value="If it was just for a dull reason, I'd suggest you to chat with the server owner or the person who kicked you. Asking the person who kicked you is a easy method, since I gave you the name and tag for it. If you don't talk each other and don't have his name and tag, you should ask some people.", inline=False)
        await member.send(embed=embed)    

@bot.command()
async def ban(ctx, member: discord.User = None, *, reason = None):
    author = ctx.message.author
    if member == None or member == ctx.message.author:
        await ctx.send("You can't ban yourself!")
        return
    if reason == None:
        reason = "Unspecified reason."
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("This command is not usable unless you're an administrator.")
    else:
        await ctx.guild.ban(member)
        await ctx.send('**{0}** has been banned by {1.mention}, with the reason "**{2}**".'.format(member, ctx.message.author, reason))
        embed = discord.Embed(title="You have a important message!", description="You were banned from **{0}**.".format(ctx.guild.name), color=0xFF3030, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Here is the reason:", value="```{}```".format(reason), inline=False)
        embed.add_field(name="This is the person who banned you:", value="{0.mention}".format(ctx.message.author))
        embed.add_field(name="Note!", value="If it was just for a dull reason, I'd suggest you to chat with the server owner or the person who kicked you. Asking the person who kicked you is a easy method, since I gave you the name and tag for it. If you don't talk each other and don't have his name and tag, you should ask some people.", inline=False)
        await member.send(embed=embed)
    
@bot.command()
async def hackban(ctx, user_id):
    author = ctx.message.author
    guild = ctx.author.guild
    embed = discord.Embed(title="Ban", description="Do you want to Ban {}?".format(user_id), colour=0x3498db)
    embed.add_field(name="Reason = Not available", value="And you have 20 seconds", inline=False)
    embed.add_field(name="Reply with", value="yes or no", inline=False)
    await ctx.send(embed=embed)
    def pred(m):
        return m.author == ctx.author and m.channel == ctx.channel
    try:
        response = await bot.wait_for('message', check = pred, timeout = 20)
    except asyncio.TimeoutError:
        embed = discord.Embed(title="Cancelling", description="{} cannot be banned because 20 seconds were passed, try again!".format(user_id), colour=0xFF3030, timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=embed)
        
    else:
        if response.clean_content.lower() == 'yes':
            if ctx.author.guild_permissions.administrator:
                try:
                    fake_member = discord.Object(id=user_id)
                    await guild.ban(fake_member)
                    embed = discord.Embed(title="Success!", description="{} got banned!".format(user_id), colour=0x00C957, timestamp=datetime.datetime.utcnow())
                    await ctx.send(embed=embed)
                except discord.NotFound:
                    embed = discord.Embed(title="Cancelling", description="User cannot be found, please use a user id, or try again.", colour=0xFF3030, timestamp=datetime.datetime.utcnow())
                    await ctx.send(embed=embed)
                except discord.HTTPException:
                    embed = discord.Embed(title="Cancelling", description="An error occurred, please try again, or not.", colour=0xFF3030, timestamp=datetime.datetime.utcnow())
                    await ctx.send(embed=embed)
                except discord.Forbidden:
                    embed = discord.Embed(title="Are you sure about that?", description="Excuse me, but i need permessions to do that, please give me the permessions.", colour=0xFFFF00, timestamp=datetime.datetime.utcnow())
                    await ctx.send(embed=embed)
                    
                    

            else:
                if user.guild_permissions.administrator:
                    embed = discord.Embed(title="Cancelling", description="You cannot ban {}.".format(user_id), colour=0xEE2C2C, timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Possible reason:", value="um")
                    await ctx.send(embed=embed)

                else:
                    embed = discord.Embed(title="Cancelling", description="You are not allowed to do that!", colour=0xEE2C2C, timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Possible reason:", value="You are a member, or you are not allowed to do that!")
                    await ctx.send(embed=embed)
            if response.clean_content.lower() == 'no':
                embed = discord.Embed(title="Cancelling", description="Ok then, cancelling ban...", colour=0x3498db, timestamp=datetime.datetime.utcnow())
                await ctx.send(embed=embed)
  
#non-administrator commands 1

@bot.command()
async def randomnumber(ctx):
    guess = random.randint(10, 100)
    await ctx.send("Random number is: {}, could it be a lucky number?".format(guess))


@bot.command()
async def warn(ctx, user: discord.Member, *, args):
    if user.guild_permissions.administrator:
        embed = discord.Embed(title="Cancelling", description="You cannot warn {0}.".format(user, ctx.message.author), colour=0xEE2C2C, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Possible reason:", value="You cannot warn an administrator, or he is a owner")
        await ctx.send(embed=embed)
    else:
        if ctx.author.guild_permissions.administrator:
            embed = discord.Embed(title="Success!", description="{0} got warned!".format(user, ctx.message.author), colour=0x00C957, timestamp=datetime.datetime.utcnow())
            embed = discord.Embed(title="Uh oh.", description="Looks like you have been Warned from the following server:", timestamp=datetime.datetime.utcnow())
            embed.add_field(title=ctx.guild.name, value="This is the server.", inline=False)
            embed.add_field(name="And the following reason is:", value=args, inline=False)
            await ctx.send(embed-embed)

        else:
            embed = discord.Embed(title="Cancelling", description="You are not allowed to do that!", colour=0xEE2C2C, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Possible reason:", value="You are a member, or you are not allowed to do that!")
            await ctx.send(embed=embed)


@bot.command()
async def servercount(ctx):
    embed = discord.Embed(title="In how much servers there is the bot?", description="The bot is currently in "f"{len(bot.guilds)}"" server or servers", colour=0x3498db, timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed)


@bot.command()
async def embed(ctx, *, message):
    user = ctx.message.author
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title="{}".format(user), description=message, color=0x3498db)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def create_poll(ctx, *, args):
    user = ctx.message.author
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title="A Poll has been created by {}.".format(user), description=args, color=0x3498db, timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed)

#administrator commands 1

@bot.command()
async def clear(ctx, amount: int):
    user = ctx.message.author
    if ctx.author.guild_permissions.administrator:
        await ctx.channel.purge(limit=1)
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title="Cleared!", description="i have deleted {} messages!".format(amount), colour=0x00C957, timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=embed)
        
    else:
        if user.guild_permissions.administrator: 
           embed = discord.Embed(title="Cancelled :frowning:", description="How dare you try deleting message when you are a member", colour=0xEE2C2C, timestamp=datetime.datetime.utcnow())
           embed.add_field(name="You need to be", value="Administrators for that!", inline=False)
           await ctx.send(embed=embed)

#non-administrator commands 2

@bot.command()
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="Info", description="Here is {} info.".format(user), colour=0x3498db, timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Name:", value=user.name, inline=False)
    embed.add_field(name="ID:", value=user.id, inline=False) 
    embed.add_field(name="Status:", value=user.status, inline=False)
    embed.add_field(name="Highest Role:", value=user.top_role, inline=False)
    embed.add_field(name="Joined this server at", value=user.joined_at, inline=False)
    embed.add_field(name="Created account at", value=user.created_at, inline=False)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def id(ctx, user_id):
    await ctx.send("Okay, you want the id of a user. Please wait.")
    try:
        with ctx.channel.typing():
            user = await bot.get_user_info(user_id)
            embed = discord.Embed(title="{} 's info".format(user), description="Here is all the info i could get", colour=0x3498db, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Name:", value=user.name, inline=False)
            embed.add_field(name="ID:", value=user.id, inline=False)
            embed.add_field(name="Created account at:", value=user.created_at, inline=False)
            await ctx.send(embed=embed)  
    except discord.NotFound:
        await ctx.send("No user found under this ID.")
    except discord.HTTPException:
        await ctx.send("Error collecting user information")

@bot.command()
async def yesorno(ctx):
    channel = ctx.message.channel
    await ctx.send("So, here is a test command, yes or no?")
    def yes(m):
        return m.author == ctx.author and m.channel == ctx.channel
    if response.clean_content.lower() == 'yes':
        await ctx.send("You said yes, right?")
        await bot.wait_for('response', check=yes)
    else:
        if response.clean_content.lower() == 'no':
            await ctx.send("Did you say no?")
            
@bot.command()
async def discordpy_ver(ctx):
    await ctx.send("The discord.py version is {}.".format(discord.__version__))

@bot.command(name='botinfo')
async def botinfo(ctx):
    embed = discord.Embed(color=discord.Color.blue())
    embed.title = 'Bot Information'
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    try:
        embed.description = bot.psa + '\n[Support Server](https://discord.gg/USU6gx6)'
    except AttributeError:
        embed.description = '\n[Support Server](https://discord.gg/USU6gx6)'
    embed.add_field(name="Servers", value=len(bot.guilds))
    embed.add_field(name="Online Users", value=str(len({m.id for m in bot.get_all_members() if m.status is not discord.Status.offline})))
    embed.add_field(name='Total Users', value=len(bot.users))
    embed.add_field(name='Channels', value=f"{sum(1 for g in bot.guilds for _ in g.channels)}")
    embed.add_field(name="Library", value=f"discord.py")
    embed.add_field(name="Bot Latency", value=f"{bot.ws.latency * 1000:.0f} ms")
    embed.add_field(name="Invite", value=f"[Click Here](https://discordapp.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=268905542)")
    embed.add_field(name="Bot version", value=version)
    
    await ctx.send(embed=embed)



@bot.command()
async def add(ctx, a: int, b: int):
    embed = discord.Embed(title="Here is the answer you've got:", description=a+b, color=0x3498db, timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed)

@bot.command()
async def multiply(ctx, a: int, b: int):
    embed = discord.Embed(title="Here is the answer you've got:", description=a*b, color=0x3498db, timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed)
    
@bot.command()
async def subtract(ctx, a: int, b: int):
    embed = discord.Embed(title="Here is the answer you've got:", description=a-b, color=0x3498db, timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed)

@bot.command()
async def number_power(ctx, a: int, b: int):
    embed = discord.Embed(title="Here is the answer you've got:", description=a**b, color=0x3498db, timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed)

#Channel Commands

@bot.command()
async def create_channel(ctx, args):
    guild = ctx.author.guild
    if user.guild_permissions.administrator:
        creating = await ctx.send("Creating text channel...")
        channel = await guild.create_text_channel(args)
        await creating.edit(content="Done. Check the channels to see if I created a channel for you.")

@bot.command()
async def create_category(ctx, args):
    guild = ctx.author.guild
    if user.guild_permissions.administrator:
        creating = await ctx.send("Creating category...")
        channel = await guild.create_category(args)
        await creating.edit(content="Done. Check the channels to see if I created a category for you.")

bot.run("NDkzOTI2NDc4ODI5MDYwMDk5.DsRzmw.1VqEZQG8TS0JZgEv7txZQA-IDTw")
