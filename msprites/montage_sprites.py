import os
import shutil
from msprites.command import Command
from msprites import FFmpegThumbnails
from msprites.settings import Settings
from msprites.constants import THUMBNAIL_SPRITESHEET
from msprites.webvtt import WebVTT


class MontageSprites(Settings):

    def __init__(self, thumbs, sprite_filename):
        self.thumbs: FFmpegThumbnails = thumbs
        self.sprite_filename = sprite_filename

    def generate(self, sprite_file_name):
        cmd = THUMBNAIL_SPRITESHEET.format(
            rows=self.ROWS,
            cols=self.COLS,
            width=self.WIDTH,
            height=self.HEIGHT,
            input=self.thumbs.dir,
            output=self.sprite_filename,
        )
        Command.execute(cmd)

        return self

    def to_webvtt(self, output_dir):
        if not output_dir:
            return
        webvtt = WebVTT(self, output_dir=output_dir)
        webvtt.generate()

        return self

    @classmethod
    def from_media(cls, video_path, thumbs_dir, sprite_filename):
        thumbs = FFmpegThumbnails.from_media(
            video_path,
            output_dir=thumbs_dir,
        )

        MontageSprites(
            thumbs,
        ).generate(
            sprite_filename,
        ).to_webvtt(
            thumbs_dir
        )

        return
