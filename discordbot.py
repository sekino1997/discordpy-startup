from discord.ext import commands
import os
import traceback
import discord

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
    
@client.event
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

client.run(os.environ.get('ENV_VAR_DISCORD_ID'))

bot.run(token)
