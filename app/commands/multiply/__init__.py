import sys
from app.commands import Command


class MultiplyCommand(Command):
    def execute(self):
        print(f'I will multiply a number')
