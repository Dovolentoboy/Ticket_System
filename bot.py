import disnake
import os
from disnake.ext import commands

bot = commands.Bot(command_prefix='!',intents=disnake.Intents.all())


@bot.event
async def on_ready():
    print('Бот готов')


@commands.command(name='reload')
async def reload(ctx,extension):
    try:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'cogs.{extension} reloaded')
    except Exception:
          await ctx.send(Exception)

    

for filename in os.listdir("./staff"):
	if filename.endswith(".py"):
		bot.load_extension(f"staff.{filename[:-3]}")

for filename in os.listdir("./tickets"):
	if filename.endswith(".py"):
		bot.load_extension(f"tickets.{filename[:-3]}")         


bot.run('MTEyNjk3NjM1MDc1NDk3OTk1Mw.GVB1Fh.llaeTxEpcyzmAUQRuVk54aH70_BPYhPjnEwXYE')
