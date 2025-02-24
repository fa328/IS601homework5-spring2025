import sys
from app.commands import Command


class AddCommand(Command):
    def execute(self):
        print(f'I will add the number')
