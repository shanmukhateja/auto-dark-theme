import subprocess
import shutil


class Spawner:
    def __init__(self):
        self.lookandfeeltool_path = shutil.which('lookandfeeltool')
        if self.lookandfeeltool_path is None:
            # FIXME: This happens before we try to switch themes; It should be triggered on init
            raise Exception('Unable to locate "lookandfeeltool" in $PATH')

    def spawn_tool(self, theme_name: str):
        proc = subprocess.Popen(
            executable=self.lookandfeeltool_path,
            args=[
                "-a",
                theme_name
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        proc.wait()
        (out, err) = proc.communicate()
        # FIXME: Better error handling for stdout
        if err or "Usage" in out.decode():
            raise Exception(err.decode() or out.decode())
