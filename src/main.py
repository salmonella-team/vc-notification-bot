import os
import discord
import setting


BOT_TOKEN = setting.BOT_TOKEN
LOG_CHANNEL_ID = int(setting.LOG_CHANNEL_ID)
UEKI_CHANNEL_ID = int(setting.UEKI_CHANNEL_ID)


client = discord.Client()

@client.event
async def on_ready():
    channel = client.get_channel(UEKI_CHANNEL_ID)
    await channel.send('うえきちゃんが起動しました')


@client.event
async def on_voice_state_update(member, before, after):
    channel = client.get_channel(LOG_CHANNEL_ID)

    # afterの中身がNoneであれば退室、afterのチャンネルネームとbeforeのチャンネルネームが同じであればミュート判定
    if after.channel == None:
        await channel.send(member.name + " が退出しました")
    elif after.channel == before.channel:
        if after.self_mute:
            await channel.send(member.name + " がミュートしました")
        elif after.self_mute == False:
            await channel.send(member.name + " がミュートを解除しました")
        return
    else:
        await channel.send(member.name + " が" + after.channel.name + " に入室しました")

client.run(BOT_TOKEN)

