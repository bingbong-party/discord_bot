import discord
from discord.ext import commands
from key import BOT_SETTING

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='~', intents=intents)

@bot.event # 봇이 실행되는 동안 발생하는 이벤트
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))  # 봇이 실행되면 콘솔창에 표시

@bot.command()
async def lemon(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def h(ctx, arg):
    await ctx.send(arg + '의 전적을 검색 중입니다')

bot.run(BOT_SETTING['token'])