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

    def generate(self):
        cmd = THUMBNAIL_SPRITESHEET.format(
            rows=self.ROWS,
            cols=self.COLS,
            width=self.WIDTH,
            height=self.HEIGHT,
            input=self.thumbs.dir,
            output=self.sprite_filename,
        )
        Command.execute(cmd)

    def to_webvtt(self, webvtt_filename):
        if not webvtt_filename:
            return
        webvtt = WebVTT(self, filename=webvtt_filename)
        webvtt.generate()

    @classmethod
    def from_media(cls, video_path, thumbs_dir, sprite_filename, webvtt_filename=None):
        thumbs = FFmpegThumbnails.from_media(video_path, output_dir=thumbs_dir)
        sprites = MontageSprites(
            thumbs,
            sprite_filename=sprite_filename,
        )
        sprites.generate()
        sprites.to_webvtt(webvtt_filename)

        return sprites
