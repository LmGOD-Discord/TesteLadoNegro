import discord
import asyncio

import config #Apenas importei isso para não mostrar o meu token

client = discord.Client()

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

client.run(config.token)