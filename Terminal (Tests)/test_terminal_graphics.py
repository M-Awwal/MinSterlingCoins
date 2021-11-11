"""
* @author: Awwal Mohammed
* date: 09-11-21
* program title: test_terminal_graphics.py

description:
\t A shadow of the terminal_graphics.py class, specifically for testing purposes.
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

    @staticmethod
    def show_result_table(user_input, data):
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")
        coins_table = Table(show_header=True, header_style="bold cyan")

        table.add_column("Date & Time Received", style="dim")
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
        console.print(coins_table, '\n')
