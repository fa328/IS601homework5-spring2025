'''Multiply funtion'''
import sys
from app.commands import Command


class MultiplyCommand(Command):
    '''ultiplyCommand'''
    def execute(self):
        print('I will multiply a number')

    def undo(self):
        '''Undo fuction'''
        print('Undo the Multiply')
