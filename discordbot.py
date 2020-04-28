from discord.ext import commands
import os
import traceback

import discord 

import asyncio
import random
import sys
import os
import botFunction.functions as f

func_list = {
    '名言': f.random_meigen,
    '迷言': f.random_meigen,
    '武器': f.random_splat_buki,
    'ブキ': f.random_splat_buki,
    'help': f.help,
    'ヘルプ': f.help
}

client = discord.Client()

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

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

@bot.event
async def on_message(message):
    '''
    特定のメッセージを受け取って処理する\n
    今はメンションを送るとランダムに名言を返す
    '''
    try:
        if client.user.id in message.content:
            for k in func_list:
                if k in str(message.content):
                    await func_list[k](client, message)
                    break
            else:
                await f.random_reply(client, message)
    except:
        print(sys.exc_info())    
    
    
    
bot.run(token)
