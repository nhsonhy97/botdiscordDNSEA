from discord.ext import commands, tasks
import discord
from myreq import popup, my_soup, req_by_num

BOT_TOKEN = "MTE2MzcwMTY2MjM2NDQ3OTUwOQ.GI-f0-.oXcrdk-jguKTM9EQUvZaD9QwXHa3BMps1rETPU"
CHANNEL_ID = 537700344713445406

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@tasks.loop(seconds=60)
async def loop_test():
    channel = bot.get_channel(CHANNEL_ID)
    if "Game service resumed" in my_soup(req_by_num(1140)):
        await channel.send("Cập nhật xong rồi! <@&1163726805711200277>")
    # await channel.send("Chưa cập nhật xong đâu <@&1163726805711200277>")

@bot.event
async def on_ready():
    loop_test.start()



bot.run(BOT_TOKEN)