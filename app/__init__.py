'''App function'''
import os
import pkgutil
import importlib
import logging
import logging.config
import sys
from dotenv import load_dotenv # type: ignore
from app.commands import CommandHandler
from app.commands import Command


class App: # pylint: disable=too-few-public-methods
    '''class App'''
    def __init__(self): # Constructor
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'TESTING')
        self.command_handler = CommandHandler()

    def configure_logging(self):
        '''Confing Logging'''
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s'
            )
        logging.info("Logging configured.")

    def load_environment_variables(self):
        """Environment Variables"""
        settings = dict(os.environ.items())
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        """Get Environment Variables"""
        return self.settings.get(env_var, None)

    def load_plugins(self):
        '''plugins Directory'''
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.','/')]):
            if is_pkg: # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command,)): # BaseCommand
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue #if item is not class or unrelated class, just ignore

    def register_plugin_commands(self, plugin_module, plugin_name):
        '''Register plugin commands'''
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                # Command names are now explicitly set to the plugin's folder name
                self.command_handler.register_command(plugin_name, item())
                logging.info("Command '%s' from plugin '%s' registered.", plugin_name, plugin_name)

    def start(self):
        '''start function'''
        self.load_plugins()
        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())


if __name__ == "__main__":
    app = App()
    app.start()
