from telethon import TelegramClient
from telethon.tl.types import DocumentAttributeVideo

from config import CHANNEL
from utils import (
    get_video_files,
    get_video_metadata,
    generate_thumbnail,
    delete_thumbnail,
)
from progress_callback import UploadProgress


class TelegramUploader:

    def __init__(self, client: TelegramClient):
        self.client = client

    async def run(self, directory):

        videos = get_video_files(directory)

        print(f"\nFound {len(videos)} videos.\n")

        for index, video in enumerate(videos, start=1):

            print(f"\n[{index}/{len(videos)}] {video.name}")

            await self.upload_video(video)

    async def upload_video(self, video):

        progress = UploadProgress(video.name)

        metadata = get_video_metadata(video)
        thumbnail = generate_thumbnail(video)

        try:
            await self.client.send_file(
                entity=CHANNEL,
                file=str(video),

                thumb=str(thumbnail),

                supports_streaming=True,

                attributes=[
                    DocumentAttributeVideo(
                        duration=metadata["duration"],
                        w=metadata["width"],
                        h=metadata["height"],
                        supports_streaming=True,
                    )
                ],

                progress_callback=progress.update,
            )

            print("\n✅ Uploaded\n")

        finally:
            delete_thumbnail(thumbnail)