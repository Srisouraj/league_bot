import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def top(ctx):
    champion_top = ["Aatrox", "Camille", "Cho'Gath", "Darius", "Dr.Mundo", "Fiora", "Galio", "Gangplank", "Garen", "Gnar", "Illaoi", "Irelia", "Jax", "Jayce", "Kayle", "Kennen", "Kled", "Malphite", "Maokai", "Mordekaiser", "Nasus", "Ornn", "Pantheon", "Poppy", "Quinn", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Shen", "Singed", "Sion", "Teemo", "Trundle", "Tryndamere", "Udyr", "Urgot", "Vladimir", "Volibear", "Wukong", "Yorick"]
    await ctx.send(f'{random.choice(champion_top)}')

@client.command()
async def jungle(ctx):
    champion_jungle = ["Amumu", "Brand", "Camille", "Diana", "Dr.Mundo", "Elise", "Evelynn", "Fiddlesticks", "Gragas", "Hecarim", "Ivern", "Jaravan IV", "Jax", "Karthus", "Kayn", "Kha'Zix", "Kindred", "Lee Sin", "Malphite", "Master Yi", "Nidalee", "Nocturne", "Nunu", "Olaf", "Pantheon", "Qiyana", "Rammus", "Rek'Sai", "Rengar", "Sejuani", "Shaco", "Shyvana", "Sion", "Skarner", "Taliyah", "Trundle", "Twitch", "Udyr", "Vi", "Volibear", "Warwick", "Wukong", "Xin Zhao", "Zac"]
    await ctx.send(f'{random.choice(champion_jungle)}')

@client.command()
async def mid(ctx):
    champion_mid = ["Ahri", "Akali", "Anivia", "Annie", "Aurelion Sol", "Azir", "Brand", "Cassiopeia", "Corki", "Diana", "Ekko", "Fizz", "Galio", "Gangplank", "Heimerdinger", "Irelia", "Jayce", "Karthus", "Kassadin", "Katarina", "Kayle", "LeBlanc", "Lissandra", "Lucian", "Lux", "Malphite", "Malzahar", "Morgana", "Neeko", "Nocturne", "Orianna", "Pantheon", "Qiyana", "Rumble", "Ryze", "Swain", "Sylas", "Syndra", "Taliyah", "Talon", "Tristana", "Twisted Fate", "Varus", "Veigar", "Vel'Koz", "Viktor", "Vladimir", "Xerath", "Yasuo", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra"]
    await ctx.send(f'{random.choice(champion_mid)}')

@client.command()
async def adc(ctx):
    champion_adc = ["Aphelios", "Ashe", "Caitlyn", "Draven", "Ezreal", "Heimerdinger", "Jhin", "Jinx", "Kai'Sa", "Kog'Maw", "Lucian", "Miss Fortune", "Sivir", "Tristana", "Twitch", "Varus", "Vayne", "Xayana", "Yasuo", "Ziggs"]
    await ctx.send(f'{random.choice(champion_adc)}')

@client.command()
async def support(ctx):
    champion_support = ["Anivia", "Alistar", "Bard", "Blitzcrank", "Brand", "Braum", "Fiddlesticks", "Janna", "Karma", "Leona", "Lulu", "Lux", "Malphite", "Morgana", "Nami", "Nautilus", "Pyke", "Rakan", "Senna", "Shaco", "Sona", "Soraka", "Tahm Kench", "Taric", "Thresh", "Vel'Koz", "Xerath", "Yuumi", "Zilean", "Zyra"]
    await ctx.send(f'{random.choice(champion_support)}')

client.run('NjU3NTEwOTkxNzU5OTMzNDQw.XfyQ3Q.cfTylGU6MAM0I6KTLQmpR7rSqZ0')