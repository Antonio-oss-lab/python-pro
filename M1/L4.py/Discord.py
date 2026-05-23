import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True 
intents.members = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Conectado como {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')
@bot.command()
async def heh(ctx, count: int = 100):
    await ctx.send("he" * count)
bot.run("MTQ1NzA1MzYzMjQ1NjU1NjU1Ng.Gr1Z-N.tTa8mVkduGfyVSmRoIHGX1hQxuTOyGi1YCa20k")
