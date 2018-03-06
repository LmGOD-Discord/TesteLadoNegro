import discord
import asyncio
import os

client = discord.Client()

is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    token = os.environ.get('TOKEN')
else:
    import secreto
    token = secreto.token

@client.event
async def on_ready():
    print(' Olá mundo, estou online!')
    print(' NOME: ', client.user.name)
    print(' ID: ', client.user.id)
    print('=============LM===========')

@client.event
async def on_message(message):
    if message.content.lower().startswith('!ola'):
        await client.send_message(message.channel, 'Olá!')

client.run(token)