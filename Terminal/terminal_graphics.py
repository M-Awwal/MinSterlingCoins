"""
* @author: Awwal Mohammed
* date: 09-11-21
* program title: terminal_graphics.py

description:
\t A small class to encapsulate stylish designs and rich text in the terminal.
 \t The idea is to mimic the feel and look of a web application in a console application.
"""

from termcolor import colored
from pyfiglet import Figlet
from rich.console import Console
from rich.table import Table
from time import ctime


class MinSterlingTerminal:
    figlet = Figlet(font='standard')

    def __init__(self):
        pass

    def show_welcome_msg(self):
        """
        prints a stylized text in the console.
        :return: None
        """
        print(colored(self.figlet.renderText('Welcome to Minimum Sterling Coin Evaluator!'), 'green'))

    @staticmethod
    def show_result_table(user_input, data):
        """
        shows two tables describing coins processed based on input data.

        :param user_input:
        :param data:
        :return: None
        """
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")
        coins_table = Table(show_header=True, header_style="bold cyan")

        table.add_column("Datet & Time Received", style="dim")
        table.add_column("Amount Received")
        table.add_column("Coin(s) Processed")
        table.add_row(
            f"{ctime()}",
            f"{user_input}",
            f"{sum(data.values())}"
        )
        for c in data:
            if data[c] != 0:
                coins_table.add_column(f"{data[c]} {c} {'Coins' if data[c]>1 else 'Coin'}", style="dim")
        console.print(table)
        console.print(coins_table)
