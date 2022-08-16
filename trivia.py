import random
import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime

bot_prefix="BOT_PREFIX" #you can change bot prefix from here what u want
bot_token="BOT_TOKEN" #paste ur bot token here

daman = commands.Bot(command_prefix = bot_prefix)

@daman.event
async def on_ready():
	print("========================")
	print("Bot Name :- " + daman.user.name)
	print(f"Bot Id :- {daman.user.id}")
	print("========================")
	

@daman.command(aliases=["accuracy"])
async def acc(ctx,gameName=None,time=None,accuracy=None,winAmt=None,*,status=None):
        author=ctx.message.author
        server = ctx.message.guild
        await ctx.send("@everyone")
        acc=discord.Embed(title="**The Result of This Game!!**\n**======================**", description="**🥂╭・Game: {}**\n**🥂┃・Timing: {}**\n**🥂┃・Accuracy: {}**\n**🥂┃・Winning Amount: {}**\n**🥂╰・Status: {}**".format(gameName,time,accuracy,winAmt,status),colour=random.randint(0x000000,0xfffff))
        acc.add_field(name=f"**======================**", value=f"**We hope you all won and enjoyed Thanks you playing with us  **",inline=True)
        acc.set_author(name=f"{ctx.guild.name}", icon_url=server.icon_url)
        acc.set_thumbnail(url = server.icon_url)
        acc.set_footer(text=f"Thanks to {ctx.message.author}|{ctx.guild.name}", icon_url=author.avatar_url)
        message = await ctx.channel.send(embed=acc)
        
        await message.add_reaction('✅') #u can change ur emoji what u want
        await message.add_reaction('🤑')#u can change ur emoji what u want
        await message.add_reaction('🤪')#u can change ur emoji what u want
        await message.add_reaction('🤠')#u can change ur emoji what u want
        
@daman.command(aliases=["gamealert","galert"])
async def gm(ctx,gameName=None,time=None,prizeAmt=None):
        author=ctx.message.author
        server = ctx.message.guild
        await ctx.send("@everyone")
        acc=discord.Embed(title="Game alert!!\n**======================**", description="**🜲╭・Game: {}**\n**🜲┃・Timing: {}**\n**🜲╰・Prize Amount: {}**".format(gameName,time,prizeAmt),colour=random.randint(0x000000,0xfffff))
        acc.add_field(name=f"**======================**", value=f"```Alert By :-{ctx.guild.name}```",inline=True)
        
        message = await ctx.channel.send(embed=acc)
        
        await message.add_reaction('🤩')#u can change ur emoji what u want
        await message.add_reaction('😘')#u can change ur emoji what u want
        await message.add_reaction('😎')#u can change ur emoji what u want
        await message.add_reaction('📱')#u can change ur emoji what u want
        
@daman.command(aliases=["question","qalert"])
async def q(ctx,*,qnumber):
        
        await ctx.message.delete()
        author=ctx.message.author
        server = ctx.message.guild
        embed=discord.Embed(title=f"Questions.{qnumber} Is Coming On Your Screen",description=f"",colour=random.randint(0x000000,0xfffff))

        await ctx.send(embed=embed)

@daman.command()
async def alert(ctx,*,message):
        await ctx.send(f"@everyone**it's {message} time come fast to play with us.**")
        await ctx.send(f"@everyone**it's {message} time come fast to play with us.**")
        await ctx.send(f"@everyone**it's {message} time come fast to play with us.**")
        await ctx.send(f"@everyone**it's {message} time come fast to play with us.**")
        await ctx.send(f"@everyone**it's {message} time come fast to play with us.**")
  
    

    
daman.run(bot_token)
