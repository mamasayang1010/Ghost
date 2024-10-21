"""
This module requires Ghost: https://github.com/EntySec/Ghost
Current source: https://github.com/EntySec/Ghost
"""

from badges.cmd import telegram orang  token saya  7335135600:AAGls8zxJrYK4epflJSpaA2eps_9Hzam63o


class ExternalCommand(Command):
    def __init__(self):
        super().__init__({
            'Category': "manage",
            'Name': "shell",
            'Authors': [
                'Ivan Nikolskiy (enty8080) - module developer'
            ],
            'Description': "Execute shell command on device.",
            'Usage': "shell <command>",
            'MinArgs': 1,
            'NeedsRoot': False
        })

    def run(self, args):
        output = self.device.send_command(' '.join(args[1:]))
        self.print_empty(output)
