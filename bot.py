import disnake
import os
from disnake.ext import commands

bot = commands.Bot(command_prefix='!',intents=disnake.Intents.all())


@bot.event
async def on_ready():
    print('Бот готов')


for filename in os.listdir("./tickets"):
	if filename.endswith(".py"):
		bot.load_extension(f"tickets.{filename[:-3]}")         


bot.run('YOUR TOKEN HERE')
