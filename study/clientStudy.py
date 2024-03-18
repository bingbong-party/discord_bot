import discord
from key import BOT_SETTING

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event # 봇이 실행되는 동안 발생하는 이벤트
async def on_ready():
    print('We have logged in as {0.user}'.format(client))  # 봇이 실행되면 콘솔창에 표시

@client.event
async def on_message(message):
    if message.author == client.user:  # 봇 자신이 보내는 메세지는 무시
        return

    if message.content == '$hello':  # 만약 채팅이 '$hello'라면
        await message.channel.send('Hello!')  # Hello!라고 보내기

    if message.content == '홍석안녕':  # 만약 채팅이 '$hello'라면
        await message.channel.send('안녕 홍석 나는 lemon zyan이야')  # Hello!라고 보내기

client.run(BOT_SETTING['token'])