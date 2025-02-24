from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.subtrat import SuntractCommand
from app.commands.multiply import MltiplyCommand
from app.commands.divide import DivideCommand

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()


    def start(self):
        # Register commands here
        self.command_handler.register_command("add", AddCommand())
        self.command_handler.register_command("subtrat", SubractCommand())
        self.command_handler.register_command("multiply", MultiplyCommand())
        self.command_handler.register_command("divide", DivideCommand())

        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())