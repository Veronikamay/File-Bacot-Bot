#(©)Codexbotz

import pyromod.listen
from pyrogram import Client
import sys

from config import 2450885f0ec6631a0aa8aaca8155d774, 6724627,  1900012138, 1939396716:AAEOydBf3e2wBQNGqaZtpYwn3YRvgum6j_o, 1900012138, -1001214394771, -1001464689297

class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()

        if FORCE_SUB_CHANNEL:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                self.invitelink = link
            except:
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning("COBA CEK UDAH DOJADIIN ADMIN LOM BOTNYA?")
                self.LOGGER(__name__).info("\nBot BERHENTI UNTUK BANTUAN https://t.me/K4N3N")
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning("Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value")
            self.LOGGER(__name__).info("\nBot BERHENTI UNTUK BANTUAN https://t.me/K4N3N")
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by @K4N3N \nhttps://t.me/Suryapro69")
        self.username = usr_bot_me.username

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot BERHENTI.")
