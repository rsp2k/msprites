import shlex
import subprocess

class Command:

    @classmethod
    def shell(cls, command):
        cmd = shlex.split(command)
        result = subprocess.run(cmd, timeout=60*180)

        return result

    @staticmethod
    def execute(cmd):
        return Command.shell(cmd)