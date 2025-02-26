'''divide funtion'''
import sys
from app.commands import Command


class DivideCommand(Command):
    '''DividetCommand'''
    def execute(self):
        print('I will divide a number')

    def undo(self):
        '''Undo fuction'''
        print('Undo the divide')
