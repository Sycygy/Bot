import os
import discord
import random
import asyncio
from discord.ext import commands

##from keep_alive import keep_alive  # para mantener al bot online
bot = commands.Bot(command_prefix='!')

client = discord.Client()

sad_words = ['suspenso', 'mal', 'agobiado']
starter_encouragments = ['Ánimo!', 'Todo irá bien!']


#Comandos
@bot.command()
async def start(ctx, study_time, rest_time):
    if str(ctx.message.channel) == 'configuracion-pomodoro':
        channel = ctx.author.voice.channel
        await channel.connect()
        while ctx.voice_client != None:
          if ctx.voice_client != None:
            await ctx.message.channel.send(
                  'INICIANDO POMODORO DE {} MINUTOS'.format(study_time))
            await asyncio.sleep(int(
                  study_time))  # falta multiplicar por 60 para que sean minutos
          else: break
          
          if ctx.voice_client != None:
            await ctx.message.channel.send(
                  'INICIANDO DESCANSO DE {} MINUTOS'.format(rest_time))
            await asyncio.sleep(
                  int(rest_time))  # falta multiplicar por 60 para que sean minutos
          else: break


@bot.command()
async def end(ctx):
    if str(ctx.message.channel) == 'configuracion-pomodoro':
        await ctx.voice_client.disconnect()
        
        # aqui da un error, tenemos que gestionar una excepción 


#Eventos
@bot.event
async def on_ready():  # mierda que hay que poner
    print('We have logged in as {0.user}'.format(bot))

    guild_name = bot.guilds[0]
    text_channel = guild_name.text_channels

    for i in range(0, len(text_channel)):
        var = 0

        if 'configuracion-pomodoro' == str(text_channel[i]):
            var = var + 1
            break

    if var == 0:
        await guild_name.create_text_channel('configuracion-pomodoro')


@bot.listen()
async def on_message(message):
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

    #await bot.process_commands(message)


bot.run(os.environ['TOKEN'])  # para correr el bot
