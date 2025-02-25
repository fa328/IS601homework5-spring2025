'''App function'''
from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

class App: # pylint: disable=too-few-public-methods
    '''class App'''
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def start(self):
        '''start function'''
        # Register commands here
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtrat", SubtractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())

        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())

if __name__ == "__main__":
    app = App()
    app.start()
