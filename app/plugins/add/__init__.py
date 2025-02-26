'''add funtion'''
import sys
from app.commands import Command


class AddCommand(Command):
    '''AddCommand'''
    def execute(self):
        print('I will add the number')

    def undo(self):
        '''Undo fuction'''
        print('Undo the add')
