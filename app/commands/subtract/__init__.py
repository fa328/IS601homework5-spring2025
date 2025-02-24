import sys
from app.commands import Command


class SubtractCommand(Command):
    def execute(self):
        print(f'I will subtract a number')
