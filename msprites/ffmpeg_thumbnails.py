import os
import tempfile
from msprites.command import Command
from msprites.settings import Settings
from msprites.constants import FFMPEG_THUMBNAIL_IMAGES


class FFmpegThumbnails(Settings):

    def __init__(self, filename, output_directory):
        self.filename = filename
        self.dir = output_directory

    @property
    def dest(self):
        return os.path.join(self.dir.name, self.FILENAME_FORMAT.format(ext=self.EXT))

    def generate(self):
        cmd = FFMPEG_THUMBNAIL_IMAGES.format(
            input=self.filename, ips=self.IPS, width=self.WIDTH,
            height=self.HEIGHT, output=self.dest,
        )
        result = Command.execute(cmd=cmd)

    @classmethod
    def from_media(cls, path, output_dir):
        thumbs = FFmpegThumbnails(filename=path, output_dir=output_dir)
        thumbs.generate()
        return thumbs
