import os
import discord
import requests
import json
import random
from discord.ext import commands

##from keep_alive import keep_alive  # para mantener al bot online
bot = commands.Bot(command_prefix='!')

client = discord.Client()

sad_words = ['suspenso', 'mal', 'agobiado']
starter_encouragments = ['Ánimo!', 'Todo irá bien!']


#Comandos
@bot.command()
async def hola(ctx):
    print('hola')


@bot.command()
async def crear_canal(ctx):
    guild = ctx.guild
    print(guild)
    channel = await guild.create_text_channel('ejmplo')


#Eventos
@bot.event
async def on_ready():  # mierda que hay que poner
    print('We have logged in as {0.user}'.format(bot))

    guild_name = bot.guilds[0]
    print(guild_name)
    text_channel = guild_name.text_channels

    for i in range(0, len(text_channel)):
        var = 0

        if 'configuracion-pomodoro' == str(text_channel[i]):
            var = var + 1
            break

    if var == 0:
        await guild_name.create_text_channel('configuracion-pomodoro')


@bot.listen()
async def on_message(message):  # funcion para los comandos
    if message.author == client.user:
        return

    if message.channel.name == 'configuracion-pomodoro':

        if message.content.startswith('Hola pomo'):
            await message.channel.send('Hola!')

        elif message.content.startswith('Adios pomo'):
            await message.channel.send('Adiós!')

        for w in message.content.split(
        ):  # split separa por los espacios en blanco
            if w in sad_words:
                await message.channel.send(random.choice(starter_encouragments)
                                           )

        if message.content.startswith('!start'):
            channel = message.author.voice
            print(channel)
            await channel.connect()

    #await bot.process_commands(message)


bot.run(os.environ['TOKEN'])  # para correr el bot
