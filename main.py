import os
import discord
import requests
import json
import random

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


##keep_alive()
client.run(os.environ['TOKEN'])  # para correr el bot