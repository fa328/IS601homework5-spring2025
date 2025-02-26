'''add funtion'''
import sys
from app.commands import Command


class MenuCommand(Command):
    '''MenuCommand'''

    def execute(self):
        print('I will add a menu')

    def show_menu(self):
        '''to show the menu option'''
        print('list of available options.')

    def add_option(self, option):
        '''to add munu option'''
        print(f'Adding menu option: {option}')
