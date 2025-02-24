import sys
from app.commands import Command


class DivideCommand(Command):
    def execute(self):
        print(f'I will divide a number')
