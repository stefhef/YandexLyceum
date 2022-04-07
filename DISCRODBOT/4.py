import asyncio
import random
from dotenv import load_dotenv
import discord
import os
import logging

load_dotenv()
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

smiles = ['\u1F68', '\u263A', '\u2639', '\u263B', '\u1F60']
smiles_buffer = smiles.copy()
score = {"user": 0, "bot": 0}


class YLBotClient(discord.Client):
    def __init__(self):
        super().__init__()
        self.is_game = False

    async def on_ready(self):
        for guild in self.guilds:
            channel = guild.system_channel
            await channel.send("Для начала игры введите /start. Для окончания /stop")

    async def on_message(self, message):
        global smiles_buffer

        if message.author == client.user:
            return
        if message.content == "/stop":
            smiles_buffer = smiles.copy()
            score["user"] = 0
            score["bot"] = 0
            self.is_game = False
            await message.channel.send("Пока!")
        elif message.content == "/start":
            await message.channel.send("Игра началась!")
            self.is_game = True
        elif self.is_game:
            try:
                card = int(message.content)
                user_turn = smiles_buffer.pop(card % len(smiles_buffer))
                bot_turn = smiles_buffer.pop(random.randint(0, 100) % len(smiles_buffer))
                if user_turn > bot_turn:
                    score["user"] += 1
                else:
                    score["bot"] += 1
                await message.channel.send(f"Your emoji: {user_turn}\nBot emoji: {bot_turn}\nScore: You - {score['user']}, Bot - {score['bot']}")
            except ZeroDivisionError:
                winner = "user" if score["user"] > score["bot"] else "bot"
                await message.channel.send(f"{winner} win! Игра завершилась!")
                self.is_game = False

    async def wait_task(self, timer_str):
        hours, minutes, seconds = map(int, timer_str.split(":"))
        await asyncio.sleep(seconds + minutes * 60 + hours * 3600)


client = YLBotClient()
client.run(os.getenv("DISCORD_TOKEN"))
