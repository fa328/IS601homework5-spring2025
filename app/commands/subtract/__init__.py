'''subtrat funtion'''
import sys
from app.commands import Command


class SubtractCommand(Command):
    '''SubtractCommand'''
    def execute(self):
        print('I will subtract a number')

    def undo(self):
        '''Undo fuction'''
        print('Undo the subtraction')
