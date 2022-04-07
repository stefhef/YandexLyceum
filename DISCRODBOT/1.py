import os
import logging
import aiohttp
from dotenv import load_dotenv
import discord

load_dotenv()
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


class YLBotClient(discord.Client):
    async def on_ready(self):
        logger.info(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            logger.info(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')
            chanel = guild.system_channel
            # await chanel.send('Готов показать случайного котика (или пёсика!)')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if 'кот' in message.content.lower():
            # async with aiohttp.ClientSession() as session:
            #     async with session.get('https://thiscatdoesnotexist.com/') as resp:
                    # img = await resp.
            await message.channel.send('https://thiscatdoesnotexist.com/')
                # await message.channel.send("Вот вам котик", file=img)


client = YLBotClient()
client.run(os.getenv('DISCORD_TOKEN'))
