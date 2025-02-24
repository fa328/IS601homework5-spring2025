from abc import ABC, abstractmethod

from app.commands import add, divide, multiply, subtract
from tests.test_operations import Calculations


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """ Look before you leap (LBYL) - Use when its less likely to work
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"No such command: {command_name}")
        """
        """Easier to ask for forgiveness than permission (EAFP) - Use when its going to most likely work"""
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")

# add, subtract, multiply, and divide Command Classes
class AddCommand(Command):
    def execute(self, a: float, b: float):
        calculation = Calculations(a, b, add)
        return calculation.get_result()
    
class SubtractCommand(Command):
    def execute(self,a: float, b: float):
        calculation = Calculations(a, b, subtract)
        return calculation.get_result()

class MultiplyCommand(Command):
    def execute(self, a: float, b: float):
        calculation = Calculations(a, b, multiply)
        return calculation.get_result()
    
class DivideCommand(Command):
    def execute(self, a: float, b: float):
        if b == 0:
            return "Error: Division by zero"
        calculation = Calculations(a, b, divide)
        return calculation.get_result()
