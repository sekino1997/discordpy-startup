from discord.ext import commands
import os
import traceback

import discord 


client = discord.Client()
TOKEN = 'DISCORD_BOT_TOKEN'
client = discord.Client()


bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_ready():
    '''
    起動時に呼ばれるメソッド
    '''
    print('-----Logged in info-----')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')    

bot.run(token)
