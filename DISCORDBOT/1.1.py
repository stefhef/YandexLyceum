import aiohttp
import discord
import os
import logging
from dotenv import load_dotenv

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
            await channel.send("Готов показать котика или песика!")

    async def on_message(self, message):
        if message.author == client.user:
            return
        if "кот" in message.content.lower():
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.thecatapi.com/v1/images/search") as resp:
                    json_cat = await resp.json()
                    image_url = json_cat[0]["url"]
                    await message.channel.send(image_url)
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://dog.ceo/api/breeds/image/random") as resp:
                    json_dog = await resp.json()
                    image_url = json_dog["message"]
                    await message.channel.send(image_url)


client = YLBotClient()
client.run(os.getenv("DISCORD_TOKEN"))
