import asyncio
import os
import discord
from dotenv import load_dotenv
import logging

load_dotenv()
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


class YLBotClient(discord.Client):
    async def on_ready(self):
        for guild in self.guilds:
            channel = guild.system_channel
            await channel.send("Готов создать таймер!")

    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.startswith("set_timer"):
            timer_str = message.content.split(" ")[-1]
            await self.wait_task(timer_str)
            await message.channel.send("⏰ Time X has come!")

    async def wait_task(self, timer_str):
        hours, minutes, seconds = map(int, timer_str.split(":"))
        await asyncio.sleep(seconds + minutes * 60 + hours * 3600)


client = YLBotClient()
client.run(os.getenv('DISCORD_TOKEN'))
