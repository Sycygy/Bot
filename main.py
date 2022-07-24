import os
import discord
import requests
import json
import random
from discord.ext import commands

##from keep_alive import keep_alive  # para mantener al bot online

client = discord.Client()

sad_words = ['suspenso', 'mal', 'agobiado']
starter_encouragments = ['Ánimo!', 'Todo irá bien!']


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return (quote)


@client.event
async def on_ready():  # mierda que hay que poner
    print('We have logged in as {0.user}'.format(client))

    guild_name = client.guilds[0]
    print(guild_name)
    text_channel = guild_name.text_channels
    print(len(text_channel))

    for i in range(0, len(text_channel)):
        var = 0

        if 'configuracion-pomodoro' == str(text_channel[i]):
            # no se por que no funciona esta linea -> faltaba el str(), porque no son del mismo tipo
            var = var + 1
            break

    if var == 0:
        await guild_name.create_text_channel('configuracion-pomodoro')


@client.event
async def on_message(message):  # funcion para los comandos
    if message.author == client.user:
        return

    if message.content.startswith('Hola pomo'):
        await message.channel.send('Hola!')

    elif message.content.startswith('Adios pomo'):
        await message.channel.send('Adiós!')

    elif message.content.startswith('!inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    for w in message.content.split(
    ):  # split separa por los espacios en blanco
        if w in sad_words:
            await message.channel.send(random.choice(starter_encouragments))

    if message.content.startswith('start'):
        channel = ctx.author.voice.channel
        await channel.connect()


#@bot.command()
#async def leave(ctx):
#    await ctx.voice_client.disconnect()

##keep_alive()
client.run(os.environ['TOKEN'])  # para correr el bot
