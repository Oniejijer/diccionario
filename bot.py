import discord
import random
from bot_logic import gen_pass, info_1
from bot_logic import flip_coin
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def inf(ctx):
    await ctx.send(info_1())

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hola, soy un bot, {ctx.author}, para más ayuda, use $help")

@bot.command()
async def bye(ctx):
    await ctx.send(f"Adios {ctx.author}")

@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def gen(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def cal(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(f"Respuesta es {left + right}")

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

bot.run("YOUR SECRET CODE")
