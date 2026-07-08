import argparse
import asyncio

import logging
logging.basicConfig(level=logging.INFO)

from telethon import TelegramClient

from config import API_ID, API_HASH
from uploader import TelegramUploader


parser = argparse.ArgumentParser(
    description="Telegram Video Uploader"
)

parser.add_argument(
    "directory",
    help="Directory containing videos"
)

args = parser.parse_args()


client = TelegramClient(
    "telegram_uploader",
    API_ID,
    API_HASH
)


async def main():

    await client.start()

    me = await client.get_me()

    print(f"Logged in as {me.first_name}")

    uploader = TelegramUploader(client)

    await uploader.run(args.directory)

    await client.disconnect()


asyncio.run(main()) 