import discord
from discord.ext import commands
import webbrowser
import os
import random
intents = discord.Intents.default()
intents.message_content = True
Mistake = []

frases = [
    "Preserve a natureza: ela é a casa de todos nós.",
    "Cada árvore plantada é um futuro mais verde.",
    "Economize água; cada gota faz diferença.",
    "Reduza, reutilize e recicle.",
    "Cuide do planeta hoje para garantir o amanhã.",
    "Menos lixo, mais vida.",
    "Respeite os animais e proteja seus habitats.",
    "Pequenas atitudes podem gerar grandes mudanças.",
    "Prefira caminhar, pedalar ou usar transporte público.",
    "Proteja a Terra para as próximas gerações."
]
bot = commands.Bot(command_prefix='!', intents=intents)
memes = ["imagen/ursinho.jpg", "imagen/vei.jpg",
         "imagen/benicio.jpg", "imagen/kevin.jpg",
         "imagen/resenha.jpg", "imagen/orelhudo.jpg",
         "imagen/abner.jpg"]


@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')


@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def oi(ctx, x: int):
    await ctx.send("oi" * x)


@bot.command()
async def meme(ctx):
    meme = random.choice(memes)
    with open(meme, "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)


@bot.command()
async def frase(ctx):
    dica = random.choice(frases)
    await ctx.send(dica)


@bot.command()
async def mistake(ctx):
    await ctx.send(Mistake)

bot.run()
