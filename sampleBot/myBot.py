import discord
from discord.ext import commands
from secretProperties import BOT_SETTING
from function import randomDice

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='~', intents=intents)


@bot.event  # 봇이 실행되는 동안 발생하는 이벤트
async def on_ready():
    print('BOT ON [ {0.user} ]'.format(bot))  # 봇이 실행되면 콘솔창에 표시

@bot.command()
async def 주사위(ctx):
    result, barColor, botNumber, userNumber = randomDice.getRandomDiceNumber()

    embed = discord.Embed(title=':game_die: 주사위 게임 결과', color=barColor)
    embed.add_field(name='BOT', value=botNumber, inline=True)  # inline (true-옆으로 배열 false-필드마다 줄바꿈)
    embed.add_field(name='YOU', value=userNumber, inline=True)  # inline (true-옆으로 배열 false-필드마다 줄바꿈)
    embed.set_footer(text='결과는 [{}]입니다'.format(result))

    await ctx.send(embed=embed)

bot.run(BOT_SETTING['token'])