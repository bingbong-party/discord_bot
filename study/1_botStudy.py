import random

import discord
from discord.ext import commands
from secretProperties import BOT_SETTING

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='~', intents=intents)


@bot.event  # 봇이 실행되는 동안 발생하는 이벤트
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))  # 봇이 실행되면 콘솔창에 표시


@bot.command()
async def lemon(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def 전적(ctx, arg):
    await ctx.send(arg + '의 전적을 검색 중입니다')


@bot.command()
async def 주사위(ctx):
    embed = discord.Embed(title='주사위 게임 결과', description='설명', color=discord.Color.green())
    embed.add_field(name='필드이름1', value='필드설명1', inline=True) # inline (true-옆으로 배열 false-필드마다 줄바꿈)
    embed.add_field(name='필드이름2', value='필드설명2', inline=True) # inline (true-옆으로 배열 false-필드마다 줄바꿈)
    embed.set_footer(text='footer')
    await ctx.send(embed=embed)

    await ctx.send('주사위를 굴립니다.')

    a = random.randrange(1, 6)
    b = random.randrange(1, 6)

    if a > b:
        await ctx.send('=== 패배 ===')
        await ctx.send('Bot - ' + str(a) + '\nYou - ' + str(b))
    elif a == b:
        await ctx.send('=== 무승부 ===')
        await ctx.send('Bot - ' + str(a) + '\nYou - ' + str(b))
    elif a < b:
        await ctx.send('=== 승리 ===')
        await ctx.send('Bot - ' + str(a) + '\nYou - ' + str(b))


@bot.event
async def on_command_error(ctx, error):  # 정의되지 않은 명령어를 입력했을 때
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('명령어를 찾지 못했습니다.')


bot.run(BOT_SETTING['token'])